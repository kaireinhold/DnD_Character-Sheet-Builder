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
