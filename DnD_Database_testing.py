import sqlite3
import pandas as pd
import os
import pprint
import sys
import DnD_function_library

if os.path.exists("DnD_Database.db"):
    os.remove("DnD_Database.db")

conn = sqlite3.connect("DnD_Database.db")
cursor = conn.cursor()

# Characters Table
cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS Characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        class TEXT NOT NULL,
        race TEXT NOT NULL,
        background TEXT,
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
        FOREIGN KEY (class) REFERENCES Classes(name),
        FOREIGN KEY (race) REFERENCES Races(name),
        FOREIGN KEY (background) REFERENCES Backgrounds(name)
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

# Table to Track Character Skill Proficiencies
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        skill TEXT NOT NULL UNIQUE,
        proficiency INTEGER DEFAULT 0,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY (skill) REFERENCES Skills(name) ON DELETE CASCADE
    );
""") # 0 = Not Proficient, 1 = Proficient, 2 = Expertise

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

# Character Inventory Table (Connects Characters to Equipment)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        equipment TEXT NOT NULL,
        quantity INTEGER DEFAULT 1,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY (equipment) REFERENCES Equipment(name) ON DELETE CASCADE
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

# Character Spells Table (Associates Spells with Characters)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Character_Spells (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        spell TEXT NOT NULL,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE,
        FOREIGN KEY (spell) REFERENCES Spells(name) ON DELETE CASCADE
    );
""")

conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in database:")
pprint.pprint(tables)


def add_character(char_name, char_race, char_class, char_background, char_level):
    conn = sqlite3.connect("DnD_Database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM Characters WHERE name = ?", (char_name,))
    existing_character = cursor.fetchone()
    
    if existing_character:
        print(f"Error: A character with the name '{char_name}' already exists.")
    else:
        cursor.execute("INSERT INTO Characters (name, race, class, background, level) VALUES (?, ?, ?, ?, ?)",
                       (char_name, char_race, char_class, char_background, char_level))
        conn.commit()
        print(f"Character '{char_name}' added successfully.")

    conn.close()

#add_character("Gandalf", "Elf", "Wizard", "Acolyte", 20)

def get_characters():
    conn = sqlite3.connect("DnD_Database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Characters")
    rows = cursor.fetchall()
    
    for row in rows:
        pprint.pprint(row)

#get_characters()


def update_character_level(name, new_level):
    conn = sqlite3.connect("DnD_Database.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE Characters SET level = ? WHERE name = ?", (new_level, name))
    
    conn.commit()
    
#update_character_level("Gandalf", 25)

def delete_character(name):
    conn = sqlite3.connect("DnD_Database.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM Characters WHERE name = ?", (name,))
    
    conn.commit()

#delete_character("Luna")


def get_characters_df():
    conn = sqlite3.connect("DnD_Database.db")
    df = pd.read_sql_query("SELECT * FROM Characters", conn)

    return df

#pprint.pprint(get_characters_df())

conn.close()
