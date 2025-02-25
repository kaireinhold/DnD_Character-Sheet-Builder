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

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Characters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        race TEXT NOT NULL,
        class TEXT NOT NULL,
        background TEXT,
        level INTEGER DEFAULT 1
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        hit_die TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Races (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        ability_bonus TEXT,
        features TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Backgrounds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        skill_proficiencies TEXT,
        starting_equipment TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ability_Scores (
        character_id INTEGER PRIMARY KEY,
        Str INTEGER DEFAULT 10 NOT NULL,
        Dex INTEGER DEFAULT 10 NOT NULL,
        Con INTEGER DEFAULT 10 NOT NULL,
        Int INTEGER DEFAULT 10 NOT NULL,
        Wis INTEGER DEFAULT 10 NOT NULL,
        Cha INTEGER DEFAULT 10 NOT NULL,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id INTEGER,
        item_name TEXT NOT NULL,
        quantity INTEGER DEFAULT 1,
        FOREIGN KEY (character_id) REFERENCES Characters(id) ON DELETE CASCADE
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
    
    # Check if the character name already exists
    cursor.execute("SELECT id FROM Characters WHERE name = ?", (char_name,))
    existing_character = cursor.fetchone()
    
    if existing_character:
        print(f"Error: A character with the name '{char_name}' already exists.")
    else:
        # Insert the new character if the name is unique
        cursor.execute("INSERT INTO Characters (name, race, class, background, level) VALUES (?, ?, ?, ?, ?)",
                       (char_name, char_race, char_class, char_background, char_level))
        conn.commit()
        print(f"Character '{char_name}' added successfully.")

    conn.close()

# Example usage
#add_character("Gandalf", "Elf", "Wizard", "Acolyte", 20)

def get_characters():
    conn = sqlite3.connect("DnD_Database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Characters")
    rows = cursor.fetchall()
    
    for row in rows:
        pprint.pprint(row)

# Example usage
#get_characters()


def update_character_level(name, new_level):
    conn = sqlite3.connect("DnD_Database.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE Characters SET level = ? WHERE name = ?", (new_level, name))
    
    conn.commit()
    
# Example usage
#update_character_level("Gandalf", 25)

def delete_character(name):
    conn = sqlite3.connect("DnD_Database.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM Characters WHERE name = ?", (name,))
    
    conn.commit()

# Example usage
#delete_character("Luna")


def get_characters_df():
    conn = sqlite3.connect("DnD_Database.db")
    df = pd.read_sql_query("SELECT * FROM Characters", conn)

    return df

# Example usage
#pprint.pprint(get_characters_df())

conn.close()
