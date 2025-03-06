import sqlite3
import pandas as pd
import os
import pprint
import sys

# Import custom function library if needed
import DnD_function_library  

# Delete existing database if it exists (for testing purposes)
if os.path.exists("DnD_Database.db"):
    os.remove("DnD_Database.db")

# Connect to the database
conn = sqlite3.connect("DnD_Database.db")
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# Characters Table (Updated)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        class_id INTEGER NOT NULL,
        race_id INTEGER NOT NULL,
        background_id INTEGER,
        level INTEGER DEFAULT 1,
        str INTEGER DEFAULT 10,
        dex INTEGER DEFAULT 10,
        con INTEGER DEFAULT 10,
        int INTEGER DEFAULT 10,
        wis INTEGER DEFAULT 10,
        cha INTEGER DEFAULT 10,
        str_mod INTEGER DEFAULT 0,
        dex_mod INTEGER DEFAULT 0,
        con_mod INTEGER DEFAULT 0,
        int_mod INTEGER DEFAULT 0,
        wis_mod INTEGER DEFAULT 0,
        cha_mod INTEGER DEFAULT 0,
        proficiency_bonus INTEGER DEFAULT 2,
        FOREIGN KEY (class_id) REFERENCES Classes(id) ON DELETE CASCADE,
        FOREIGN KEY (race_id) REFERENCES Races(id) ON DELETE CASCADE,
        FOREIGN KEY (background_id) REFERENCES Backgrounds(id) ON DELETE CASCADE
    );
""")

# Classes Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        hit_die TEXT NOT NULL,
        primary_stat TEXT NOT NULL,
        saving_throws TEXT NOT NULL
    );
""")

# Races Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Races (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        ability_bonus TEXT,
        features TEXT
    );
""")

# Backgrounds Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Backgrounds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        skill_proficiencies TEXT NOT NULL,
        starting_equipment TEXT
    );
""")

# Immutable Skills Table (Predefined List of Skills)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );
""")

# Populate Skills Table (Improved)
def populate_skills():
    skills = [
        "Acrobatics", "Animal Handling", "Arcana", "Athletics",
        "Deception", "History", "Insight", "Intimidation",
        "Investigation", "Medicine", "Nature", "Perception",
        "Performance", "Persuasion", "Religion", "Sleight of Hand",
        "Stealth", "Survival"
    ]
    
    try:
        for skill in skills:
            cursor.execute("INSERT OR IGNORE INTO Skills (name) VALUES (?);", (skill,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting skills: {e}")

populate_skills()

# Table to Track Character Skill Proficiencies (Fixed)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        skill_id INTEGER,
        proficiency INTEGER DEFAULT 0,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY (skill_id) REFERENCES Skills(id) ON DELETE CASCADE
    );
""")

# Equipment Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Equipment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        type TEXT NOT NULL,
        description TEXT,
        weight INTEGER
    );
""")

# Character Inventory Table (Fixed Equipment Reference)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        equipment_id INTEGER NOT NULL,
        quantity INTEGER DEFAULT 1,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY (equipment_id) REFERENCES Equipment(id) ON DELETE CASCADE
    );
""")

# Spells Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Spells (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        level INTEGER NOT NULL,
        school TEXT NOT NULL,
        casting_time TEXT NOT NULL,
        range TEXT NOT NULL,
        components TEXT NOT NULL,
        duration TEXT NOT NULL,
        description TEXT
    );
""")

# Character Spells Table (Fixed Reference)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Spells (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        spell_id INTEGER,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY (spell_id) REFERENCES Spells(id) ON DELETE CASCADE
    );
""")

conn.commit()

# List all tables for verification
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:")
pprint.pprint(tables)

def add_character(char_name, class_id, race_id, background_id, char_level=1, 
                  strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10):

    # Check if character name already exists
    cursor.execute("SELECT id FROM Characters WHERE name = ?", (char_name,))
    existing_character = cursor.fetchone()
    
    if existing_character:
        print(f"Error: A character with the name '{char_name}' already exists.")
    else:
        # Calculate ability modifiers based on ability scores
        def ability_modifier(score):
            return (score - 10) // 2

        str_mod = ability_modifier(strength)
        dex_mod = ability_modifier(dexterity)
        con_mod = ability_modifier(constitution)
        int_mod = ability_modifier(intelligence)
        wis_mod = ability_modifier(wisdom)
        cha_mod = ability_modifier(charisma)

        # Calculate proficiency bonus based on level (D&D 5e rules)
        def calculate_proficiency_bonus(level):
            return 2 + (level - 1) // 4

        proficiency_bonus = calculate_proficiency_bonus(char_level)

        # Insert character into the database
        cursor.execute("""
            INSERT INTO Characters 
            (name, class_id, race_id, background_id, level, 
             str, dex, con, int, wis, cha, 
             str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, proficiency_bonus)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (char_name, class_id, race_id, background_id, char_level, 
              strength, dexterity, constitution, intelligence, wisdom, charisma, 
              str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod, proficiency_bonus))

        # Get the new character's ID
        cursor.execute("SELECT id FROM Characters WHERE name = ?", (char_name,))
        character_id = cursor.fetchone()[0]

        # Assign starting equipment from background
        cursor.execute("SELECT starting_equipment FROM Backgrounds WHERE id = ?", (background_id,))
        background_equipment = cursor.fetchone()

        if background_equipment:
            for item in background_equipment[0].split(', '):
                cursor.execute("""
                    INSERT INTO Character_Inventory (character_id, equipment_id, quantity)
                    SELECT ?, id, 1 FROM Equipment WHERE name = ?;
                """, (character_id, item))

        # Assign skill proficiencies from background
        cursor.execute("SELECT skill_proficiencies FROM Backgrounds WHERE id = ?", (background_id,))
        background_skills = cursor.fetchone()

        if background_skills:
            for skill in background_skills[0].split(', '):
                cursor.execute("""
                    INSERT INTO Character_Skills (character_id, skill_id, proficiency)
                    SELECT ?, id, 1 FROM Skills WHERE name = ?;
                """, (character_id, skill))

        # Assign starting weapons and armor from class
        cursor.execute("SELECT starting_equipment FROM Classes WHERE id = ?", (class_id,))
        class_equipment = cursor.fetchone()

        if class_equipment:
            for item in class_equipment[0].split(', '):
                cursor.execute("""
                    INSERT INTO Character_Inventory (character_id, equipment_id, quantity)
                    SELECT ?, id, 1 FROM Equipment WHERE name = ?;
                """, (character_id, item))

        conn.commit()
        print(f"Character '{char_name}' added successfully with class and background equipment, skill proficiencies, and proficiency bonus.")

# Function to retrieve all characters
def get_characters():    
    cursor.execute("SELECT * FROM Characters")
    rows = cursor.fetchall()
    
    for row in rows:
        pprint.pprint(row)

# Function to update character level
def update_character_level(name, new_level):
    cursor.execute("UPDATE Characters SET level = ? WHERE name = ?", (new_level, name))
    
    conn.commit()
    
# Function to delete a character
def delete_character(name):
    cursor.execute("DELETE FROM Characters WHERE name = ?", (name,))
    
    conn.commit()

# Function to return characters as a DataFrame
def get_characters_df():
    df = pd.read_sql_query("SELECT * FROM Characters", conn)
    return df

#add_character("Aragorn", class_id=2, race_id=1, background_id=3, char_level=5, 
#              strength=16, dexterity=14, constitution=14, intelligence=10, wisdom=12, charisma=14)



conn.close()
