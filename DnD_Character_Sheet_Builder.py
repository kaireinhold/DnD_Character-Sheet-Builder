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

def save_to_json_file(character_data, username, char_name):
    folder_path = f"C:\\Users\\{username}\\Documents\\character_sheets"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "DnD_Database.json")  # adjust name if needed

    # Load existing JSON
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

    # Remove existing character (by matching the key)
    data["Characters"] = [
        c for c in data["Characters"] if dnd.char_name not in c
    ]
    data["Character_Skills"] = [
        s for s in data["Character_Skills"] if dnd.char_name not in s
    ]
    data["Character_Inventory"] = [
        i for i in data["Character_Inventory"] if dnd.char_name not in i
    ]
    data["Character_Spells"] = [
        s for s in data["Character_Spells"] if dnd.char_name not in s
    ]

    # Add the new character
    data["Characters"].append({dnd.char_name: character_data["character"]})
    data["Character_Skills"].append({f"{dnd.char_name}_skills": character_data.get("skills", [])})
    data["Character_Inventory"].append({f"{dnd.char_name}_inventory": character_data.get("inventory", [])})
    data["Character_Spells"].append({f"{dnd.char_name}_spells": character_data.get("spells", [])})

    # Save updated data
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

while True:
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
    "Characters": [
        {
        dnd.char_name : {
        "race": dnd.user_race,
        "class": ' '.join([str(x) for x in [*dnd.user_class]]).title(),
        "level": dnd.user_level,
        "background": None,  # TO BE ADDED LATER
        "str": dnd.stat_types["Str"],
        "dex": dnd.stat_types["Dex"],
        "con": dnd.stat_types["Con"],
        "int": dnd.stat_types["Int"],
        "wis": dnd.stat_types["Wis"],
        "cha": dnd.stat_types["Cha"],
        "str_mod": mod_str,
        "dex_mod": mod_dex,
        "con_mod": mod_con,
        "int_mod": mod_int,
        "wis_mod": mod_wis,
        "cha_mod": mod_cha,
        "proficiency_bonus": math.ceil(dnd.user_level / 4) + 1,
        "hp_max": dnd.hp_max,
        }
    }
    ],
    "Character_Skills": [
        {
            f"{dnd.char_name}_skills" : {
            "Acrobatics" : { "proficiency": False, "score" : mod_dex + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Acrobatics"]["proficiency"] == True else mod_dex},
            "Animal Handling" : { "proficiency": False, "score" : mod_wis + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Animal Handling"]["proficiency"] == True else mod_wis},
            "Arcana" : { "proficiency": False, "score" : mod_int + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Arcana"]["proficiency"] == True else mod_int},
            "Athletics" : { "proficiency": False, "score" : mod_str + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Athletics"]["proficiency"] == True else mod_str},
            "Deception" : { "proficiency": False, "score" : mod_cha + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Deception"]["proficiency"] == True else mod_cha},
            "History" : { "proficiency": False, "score" : mod_int + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["History"]["proficiency"] == True else mod_int},
            "Insight" : { "proficiency": False, "score" : mod_wis + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Insight"]["proficiency"] == True else mod_wis},
            "Intimidation" : { "proficiency": False, "score" : mod_cha + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Intimidation"]["proficiency"] == True else mod_cha},
            "Investigation" : { "proficiency": False, "score" : mod_int + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Investigation"]["proficiency"] == True else mod_int},
            "Medicine" : { "proficiency": False, "score" : mod_wis + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Medicine"]["proficiency"] == True else mod_wis},
            "Nature" : { "proficiency": False, "score" : mod_int + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Nature"]["proficiency"] == True else mod_int},
            "Perception" : { "proficiency": False, "score" : mod_wis + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Perception"]["proficiency"] == True else mod_wis},
            "Performance" : { "proficiency": False, "score" : mod_cha + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Performance"]["proficiency"] == True else mod_cha},
            "Persuasion" : { "proficiency": False, "score" : mod_cha + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Persuasion"]["proficiency"] == True else mod_cha},
            "Religion" : { "proficiency": False, "score" : mod_int + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Religion"]["proficiency"] == True else mod_int},
            "Sleight of Hand" : { "proficiency": False, "score" : mod_dex + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Sleight of Hand"]["proficiency"] == True else mod_dex},
            "Stealth" : { "proficiency": False, "score" : mod_dex + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Stealth"]["proficiency"] == True else mod_dex},
            "Survival" : { "proficiency": False, "score" : mod_wis + proficiency_bonus if char_data["Character_Skills"][f"{dnd.char_name}_skills"]["Survival"]["proficiency"] == True else mod_wis},
            }
        }
    ],      # TO DO: ADD NON-HARDCODED PROFICIENCY
    "Character_Inventory": [
        {
            f"{dnd.char_name}_inventory" : {
                "example_equipment" : {
                "quantity": 1
                }
            }
        }
    ],   # TO DO: ADD EQUIPMENT BASED ON BACKGROUND
    "Character_Spells": [
        {
            f"{dnd.char_name}_spells" : {
            ["example_spell_1", "example_spell_2"],
            }
        }
    ]      # TO DO: ADD SPELL SELECTION AND SUCH BASED ON CLASS AND LEVEL
}

    
    save_to_json_file(char_data, username, dnd.char_name)


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
