import sqlite3
import pandas as pd
import re

# Connect to your .db file
conn = sqlite3.connect("DnD_Database.db")  # Use your correct path here

# Load name mappings for interactive input display
class_names = pd.read_sql_query("SELECT id, name FROM Classes", conn).set_index("id")["name"].to_dict()
race_names = pd.read_sql_query("SELECT id, name FROM Races", conn).set_index("id")["name"].to_dict()
backgrounds_data = pd.read_sql_query("SELECT id, name, skill_proficiencies FROM Backgrounds", conn)

def calculate_modifier(score):
    return (score - 10) // 2

def calculate_proficiency_bonus(level):
    return 2 + (level - 1) // 4

def create_character():
    print("🛠️ Create a New D&D Character\n")

    name = input("Character name: ")

    print("\nChoose a Class:")
    # Sort and display classes in alphabetical order with visible selection number
    class_df = pd.read_sql_query("SELECT id, name FROM Classes", conn).sort_values("name").reset_index(drop=True)

    print("\nChoose a Class:")
    for i, row in class_df.iterrows():
        print(f"{i + 1}: {row['name']}")
    class_id = int(input("Enter class ID: "))
    class_id = class_df.loc[class_choice, "id"]


    print("\nChoose a Race:")
    for id, rname in race_names.items():
        print(f"{id}: {rname}")
    race_id = int(input("Enter race ID: "))

    print("\nChoose a Background:")
    for _, row in backgrounds_data.iterrows():
        print(f"{row['id']}: {row['name']} ({row['skill_proficiencies']})")
    background_id = int(input("Enter background ID: "))

    level = int(input("\nLevel (1–20): "))
    str_score = int(input("Strength: "))
    dex_score = int(input("Dexterity: "))
    con_score = int(input("Constitution: "))
    int_score = int(input("Intelligence: "))
    wis_score = int(input("Wisdom: "))
    cha_score = int(input("Charisma: "))

    # Calculate modifiers and proficiency
    modifiers = {stat: calculate_modifier(score) for stat, score in
                 zip(["str", "dex", "con", "int", "wis", "cha"],
                     [str_score, dex_score, con_score, int_score, wis_score, cha_score])}
    prof_bonus = calculate_proficiency_bonus(level)

    # Insert into Characters table
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Characters (name, class_id, race_id, background_id, level,
        str, dex, con, int, wis, cha,
        str_mod, dex_mod, con_mod, int_mod, wis_mod, cha_mod,
        proficiency_bonus)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name, class_id, race_id, background_id, level,
        str_score, dex_score, con_score, int_score, wis_score, cha_score,
        modifiers["str"], modifiers["dex"], modifiers["con"],
        modifiers["int"], modifiers["wis"], modifiers["cha"],
        prof_bonus
    ))
    character_id = cursor.lastrowid

    # Handle skill proficiencies from background
    skills_str = backgrounds_data.loc[backgrounds_data["id"] == background_id, "skill_proficiencies"].values[0]

    # Extract skill names (either straight list or "2: ..." pick-list style)
    if "2:" in skills_str:
        print("\nChoose 2 skills from the following list:")
        skill_names = [s.strip() for s in skills_str.split("2:")[1].split(",")]
        for i, skill in enumerate(skill_names, 1):
            print(f"{i}: {skill}")
        chosen = input("Enter 2 numbers separated by commas: ").split(",")
        skill_names = [skill_names[int(i.strip()) - 1] for i in chosen]
    else:
        skill_names = [s.strip() for s in skills_str.split(",")]

    # Map skill names to IDs
    skills_df = pd.read_sql_query("SELECT id, name FROM Skills", conn)
    skill_id_map = dict(zip(skills_df["name"].str.lower(), skills_df["id"]))

    for skill in skill_names:
        skill_id = skill_id_map.get(skill.lower())
        if skill_id:
            cursor.execute(
                "INSERT INTO Character_Skills (character_id, skill_id, proficiency) VALUES (?, ?, ?)",
                (character_id, skill_id, 1)
            )

    conn.commit()
    print(f"\n✅ Character '{name}' created successfully with ID {character_id}!")

# To use it, just run:
create_character()
