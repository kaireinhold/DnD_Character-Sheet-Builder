#Created by Kai Reinhold (kaireinhold on GitHub)

import math
import random
import time
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import os
import json
import DnD_function_library
from DnD_function_library import Dnd

dnd = Dnd()

def Build_Character_Sheet():
    dnd.rolls = []  
    start = input("Start? (y/n) ").lower().strip()  
    if start == "y":
        username = os.getlogin()  
        save = input("Would you like to save your character to a text file? (y/n) ")  
        if save.lower().strip() == "y":
            save_type = input("Would you like to overwrite a file that was already made (or make a new file) (1), or add to a file that was already made (2)? ").lower().strip()
        dnd.char_name = input("What is your character's name? ").strip().title()
        if dnd.char_name.lower() != "andrew" and dnd.char_name.lower() != "luca" and dnd.char_name.lower() != "kai" and dnd.char_name.lower() != "z" and dnd.char_name.lower() != "zurulien":
            dnd.user_class = input("What class do you choose? (Barbarian, Fighter, Wizard, Rogue, Bard, Druid, Paladin, Cleric, Monk, Ranger, Sorcerer, Warlock, Artificer. If you choose multiple, it will automatically distribute your levels evenly between them. Separate with a space. Put priority class first.) ").title().strip().split(" ")
        else:
            dnd.user_class = [""]
        dnd.roll_stats = 4
        dnd.stat_roll(dnd.user_class)
        print(dnd.stat_types)
        if dnd.char_name.lower().strip() == "z" or dnd.char_name.lower().strip() == "zurulien":
            dnd.set_race("Pure Starling")
            dnd.user_class = ["Barbarian", "Wizard"]
            dnd.user_race = "Eye of Mind"
        else:
            dnd.set_race()
        dnd.set_level()

        mod_str = (dnd.stat_types["Str"] - 10) // 2
        mod_dex = (dnd.stat_types["Dex"] - 10) // 2
        mod_con = (dnd.stat_types["Con"] - 10) // 2
        mod_int = (dnd.stat_types["Int"] - 10) // 2
        mod_wis = (dnd.stat_types["Wis"] - 10) // 2
        mod_cha = (dnd.stat_types["Cha"] - 10) // 2
        
        dnd.calc_hit_points(dnd.user_level, dnd.user_class, mod_con)
        proficiency_bonus = math.ceil(dnd.user_level/4) + 1
        alignment = input("What is your alignment? (Chaotic Good, Neutral Good, Lawful Good, Lawful Neutral, True Neutral, Chaotic Neutral, Lawful Evil, Neutral Evil, Chaotic Evil) ").title()

    else:
        sys.exit()
    if save.lower().strip() == "n":
        if dnd.char_name.lower() == "andrew" or dnd.char_name.lower() == "luca" or dnd.char_name.lower() == "kai" or dnd.char_name.lower() == "z" or dnd.char_name.lower() == "zurulien":
            print(f"""You are {dnd.char_name}!
You are a {' '.join([str(x) for x in [*dnd.user_class]]).title()}!
Your level is {dnd.user_level}!
Your Hit Point Maximum is {dnd.hp_max}!
Your Initiative Bonus is {mod_dex}!
Your Proficiency Bonus is {proficiency_bonus}!
Your stats are:
Strength: {dnd.stat_types["Str"]} ({mod_str})
Dexterity: {dnd.stat_types["Dex"]} ({mod_dex})
Constitution: {dnd.stat_types["Con"]} ({mod_con})
Intelligence: {dnd.stat_types["Int"]} ({mod_int})
Wisdom: {dnd.stat_types["Wis"]} ({mod_wis})
Charisma: {dnd.stat_types["Cha"]} ({mod_cha})
""")
    
        elif dnd.user_class[0].lower() == "artificer":
            print(f"""You are {dnd.char_name}!
You are an {' '.join([str(x) for x in [*dnd.user_class]]).title()}!
Your level is {dnd.user_level}!
Your Hit Point Maximum is {dnd.hp_max}!
Your Initiative Bonus is {mod_dex}!
Your Proficiency Bonus is {proficiency_bonus}!
Your stats are:
Strength: {dnd.stat_types["Str"]} ({mod_str})
Dexterity: {dnd.stat_types["Dex"]} ({mod_dex})
Constitution: {dnd.stat_types["Con"]} ({mod_con})
Intelligence: {dnd.stat_types["Int"]} ({mod_int})
Wisdom: {dnd.stat_types["Wis"]} ({mod_wis})
Charisma: {dnd.stat_types["Cha"]} ({mod_cha})
""")
    
        elif dnd.user_class == None or dnd.user_class == "" or dnd.user_class[0].lower() != 'barbarian' and dnd.user_class[0].lower() != 'fighter' and dnd.user_class[0].lower() != 'wizard' and dnd.user_class[0].lower() != 'rogue' and dnd.user_class[0].lower() != 'bard' and dnd.user_class[0].lower() != 'druid' and dnd.user_class[0].lower() != 'paladin' and dnd.user_class[0].lower() != 'cleric' and dnd.user_class[0].lower() != 'monk' and dnd.user_class[0].lower() != 'ranger' and dnd.user_class[0].lower() != 'sorcerer' and dnd.user_class[0].lower() != 'warlock' and dnd.user_class[0].lower() != 'artificer':
            print(f"""You are {dnd.char_name}!
Your level is {dnd.user_level}!
Your Hit Point Maximum is {dnd.hp_max}!
Your Initiative Bonus is {mod_dex}!
Your Proficiency Bonus is {proficiency_bonus}!
Your stats are:
Strength: {dnd.stat_types["Str"]} ({mod_str})
Dexterity: {dnd.stat_types["Dex"]} ({mod_dex})
Constitution: {dnd.stat_types["Con"]} ({mod_con})
Intelligence: {dnd.stat_types["Int"]} ({mod_int})
Wisdom: {dnd.stat_types["Wis"]} ({mod_wis})
Charisma: {dnd.stat_types["Cha"]} ({mod_cha})
""")
    
        else:
            print(f"""You are {dnd.char_name}!
You are a {' '.join([str(x) for x in [*dnd.user_class]]).title()}!
Your level is {dnd.user_level}!
Your Hit Point Maximum is {dnd.hp_max}!
Your Initiative Bonus is {mod_dex}!
Your Proficiency Bonus is {proficiency_bonus}!
Your stats are:
Strength: {dnd.stat_types["Str"]} ({mod_str})
Dexterity: {dnd.stat_types["Dex"]} ({mod_dex})
Constitution: {dnd.stat_types["Con"]} ({mod_con})
Intelligence: {dnd.stat_types["Int"]} ({mod_int})
Wisdom: {dnd.stat_types["Wis"]} ({mod_wis})
Charisma: {dnd.stat_types["Cha"]} ({mod_cha})
""")
        print(f"Your alignment is {alignment}!")

        if dnd.user_race.lower().strip() == "aasimar" or dnd.user_race.lower().strip() == "air genasi" or dnd.user_race.lower().strip() == "arachne" or dnd.user_race.lower().strip() == "aarakocra" or dnd.user_race.lower().strip() == "earth genasi" or dnd.user_race.lower().strip() == "elf":
            print(f"You are an {dnd.user_race.title()}!")
        else:
            print(f"You are a {dnd.user_race.title()}!")
        print(f"Your movement speed is {dnd.movement_speed}!")

        if dnd.darkvision == True:
            print("You have darkvision!")
        print(f"You know these languages:")
        for x in dnd.languages:
            print("-", x.title())

    elif save.lower().strip() == "y":

        divider1 = "\n✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏\n"
        divider2 = "\n•───────•°•❀•°•───────•\n"
        divider3 = "\n︵‿︵‿୨♡୧‿︵‿︵\n"
        divider4 = "\n✿　.　˚　. 　 ˚　✿.\n"
        divider5 = "\n⊹˚₊‧───────────────‧₊˚⊹\n"
        divider6 = "\n⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆\n"
        divider7 = "\n➽───────────────❥\n"
        divider8 = "\n· • —– ٠ ✤ ٠ —– • ·\n"
        divider9 = "\n⋅•⋅⋅•⋅⊰⋅•⋅⋅•⋅⋅•⋅⋅•⋅∙∘☽༓☾∘∙•⋅⋅⋅•⋅⋅⊰⋅•⋅⋅•⋅⋅•⋅⋅•⋅\n"
        divider10 = "\n•─────⋅☾ ☽⋅─────•\n"

        divider_choice = input("""What divider would you like to use?
(1) ✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏
(2) •───────•°•❀•°•───────•
(3) ︵‿︵‿୨♡୧‿︵‿︵
(4) ✿　.　˚　. 　 ˚　✿.
(5) ⊹˚₊‧───────────────‧₊˚⊹
(6) ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆ ⋆⁺₊⋆
(7) ➽───────────────❥
(8) · • —– ٠ ✤ ٠ —– • ·
(9) ⋅•⋅⋅•⋅⊰⋅•⋅⋅•⋅⋅•⋅⋅•⋅∙∘☽༓☾∘∙•⋅⋅⋅•⋅⋅⊰⋅•⋅⋅•⋅⋅•⋅⋅•⋅
(10) •─────⋅☾ ☽⋅─────•
(0) None
""") 
        
        folder_path = f"C:\\Users\\{username}\\Documents\\character_sheets"

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = f"{dnd.char_name}_character_sheet.txt"
        full_path = os.path.join(folder_path, file_name)

        if save_type == "1":
            with open(full_path, "w+", encoding="utf-8") as file:
                file.write(f"""
Name: {dnd.char_name}
Class: {' '.join([str(x) for x in [*dnd.user_class]]).title()}
Race: {dnd.user_race.title()}
Level: {dnd.user_level}
Alignment: {alignment}

Initiative Bonus: {mod_dex}

Hit Point Maximum: {dnd.hp_max}

Stats:
Strength: {dnd.stat_types["Str"]} ({mod_str})
Dexterity: {dnd.stat_types["Dex"]} ({mod_dex})
Constitution: {dnd.stat_types["Con"]} ({mod_con})
Intelligence: {dnd.stat_types["Int"]} ({mod_int})
Wisdom: {dnd.stat_types["Wis"]} ({mod_wis})
Charisma: {dnd.stat_types["Cha"]} ({mod_cha})

Proficiency Bonus: {proficiency_bonus}

Movement Speed: {dnd.movement_speed}\n""")

                if dnd.darkvision == True:
                    file.write("""Darkvision\n""")
    
                file.write("\nLanguages:\n")
                for x in dnd.languages:
                    file.write(f"- {x.title()}\n")

                if divider_choice.strip() == "0" or divider_choice.strip() not in range(1,11):
                    None
                else:
                    file.write(eval(f"divider{divider_choice}"))
                    
                root = tk.Tk()
                root.withdraw()
                root.attributes('-topmost', True)
                messagebox.showinfo("Success", f"Character sheet saved to {dnd.char_name}_character_sheet.txt!")
                root.attributes('-topmost', False)
                root.destroy()
                file.seek(0)
                print(file.read())
                print(f'Absolute path to the file: {full_path}')
                file.close()

        if save_type == "2":
            with open(full_path, "a+", encoding="utf-8") as file:
                file.write(f"""
Name: {dnd.char_name}
Class: {' '.join([str(x) for x in [*dnd.user_class]]).title()}
Race: {dnd.user_race.title()}
Level: {dnd.user_level}
Alignment: {alignment}

Initiative Bonus: {mod_dex}

Hit Point Maximum: {dnd.hp_max}

Stats:
Strength: {dnd.stat_types["Str"]} ({mod_str})
Dexterity: {dnd.stat_types["Dex"]} ({mod_dex})
Constitution: {dnd.stat_types["Con"]} ({mod_con})
Intelligence: {dnd.stat_types["Int"]} ({mod_int})
Wisdom: {dnd.stat_types["Wis"]} ({mod_wis})
Charisma: {dnd.stat_types["Cha"]} ({mod_cha})

Proficiency Bonus: {proficiency_bonus}

Movement Speed: {dnd.movement_speed}\n""")

                if dnd.darkvision == True:
                    file.write("""Darkvision\n""")
    
                file.write("\nLanguages:\n")
                for x in dnd.languages:
                    file.write(f"- {x.title()}\n")

                if divider_choice.strip() == "0" or divider_choice.strip() not in range(1,11):
                    None
                else:
                    file.write(eval(f"divider{divider_choice}"))

                root = tk.Tk()
                root.withdraw()
                root.attributes('-topmost', True)
                messagebox.showinfo("Success", f"Character sheet saved to {dnd.char_name}_character_sheet.txt!")
                root.attributes('-topmost', False)
                root.destroy()
                file.seek(0)
                print(file.read())
                print(f'Absolute path to the file: {full_path}')
                file.close()
                
    char_data = {
        "name": dnd.char_name,
        "class": dnd.user_class,
        "race": dnd.user_race,
        "level": dnd.user_level,
        "alignment": alignment,
        "stats": {
            "Str": dnd.stat_types["Str"],
            "Dex": dnd.stat_types["Dex"],
            "Con": dnd.stat_types["Con"],
            "Int": dnd.stat_types["Int"],
            "Wis": dnd.stat_types["Wis"],
            "Cha": dnd.stat_types["Cha"]
        },
        "modifiers": {
            "Str": mod_str,
            "Dex": mod_dex,
            "Con": mod_con,
            "Int": mod_int,
            "Wis": mod_wis,
            "Cha": mod_cha
        },
        "hp_max": dnd.hp_max,
        "proficiency_bonus": proficiency_bonus,
        "movement_speed": dnd.movement_speed,
        "darkvision": dnd.darkvision,
        "languages": dnd.languages
    }
    
    save_to_json_file(char_data, username, dnd.char_name)

def save_to_json_file(character_data, username, char_name):
    folder_path = f"C:\\Users\\{username}\\Documents\\character_sheets"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "characters.json")

    # Load existing data
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {
                    "Characters": [],
                    "Character_Skills": [],
                    "Character_Inventory": [],
                    "Character_Spells": []
                }
    else:
        data = {
            "Characters": [],
            "Character_Skills": [],
            "Character_Inventory": [],
            "Character_Spells": []
        }

    # Remove old character data if it exists
    data["Characters"] = [c for c in data["Characters"] if c["name"] != char_name]
    data["Character_Skills"] = [s for s in data["Character_Skills"] if s["character_name"] != char_name]
    data["Character_Inventory"] = [i for i in data["Character_Inventory"] if i["character_name"] != char_name]
    data["Character_Spells"] = [s for s in data["Character_Spells"] if s["character_name"] != char_name]

    # Add updated data
    data["Characters"].append(character_data["character"])  # base profile
    data["Character_Skills"].extend(character_data.get("skills", []))
    data["Character_Inventory"].extend(character_data.get("inventory", []))
    data["Character_Spells"].extend(character_data.get("spells", []))

    # Write updated data back
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

while True:
    Build_Character_Sheet()

'''
Features to be added!

TBA races:
    Homebrew:
        -Core Starling
        -Starling
        -Shadeling
        -Crystalling
        -Bloodling
        -Pure Starling
        -Symbioling
        Silenced
        Starved


TBA features (numbers = priority/difficulty estimate):
    Spells (5)
    Skills (4)
    AC (3)
    Level up characters without making whole new character sheet instance (6)
    Background (1)
    Equipment (2)
'''
