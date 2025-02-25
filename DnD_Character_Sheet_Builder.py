#Created by Kai Reinhold (kaireinhold on GitHub)

# Importing necessary libraries
import random  # For generating random numbers
import time    # For adding delays between actions
import sys     # Provides access to some variables used by the interpreter
import tkinter as tk  # Tkinter for creating GUI components
from tkinter import ttk, messagebox  # Importing specific Tkinter widgets
import os      # For interacting with the operating system
import DnD_function_library
from DnD_function_library import Dnd

dnd = Dnd()
# Initialize dictionary to assign proficiency bonus
proficiency = {1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 5}

while True:
    dnd.rolls = []  # Initialize a list to store the rolls
    start = input("Start? (y/n) ").lower().strip()  # Ask the user to start the character creation process
    if start == "y":
        username = os.getlogin()  # Get the current user's login name
        save = input("Would you like to save your character to a text file? (y/n) ")  # Ask if the user wants to save the character
        if save.lower().strip() == "y":
            save_type = input("Would you like to overwrite a file that was already made (or make a new file) (1), or add to a file that was already made (2)? ").lower().strip()  # Ask how the user wants to save the file
        dnd.char_name = input("What is your character's name? ").strip()  # Get the character's name
        if dnd.char_name.lower() != "andrew" and dnd.char_name.lower() != "luca" and dnd.char_name.lower() != "kai" and dnd.char_name.lower() != "z" and dnd.char_name.lower() != "zurulien":
            dnd.user_class = input("What class do you choose? (Barbarian, Fighter, Wizard, Rogue, Bard, Druid, Paladin, Cleric, Monk, Ranger, Sorcerer, Warlock, Artificer. If you choose multiple, it will automatically distribute your levels evenly between them. Separate with a space. Put priority class first.) ").strip().split(" ")  # Get the character's class
        else:
            dnd.user_class = [""]  # Special case for certain character names, no class assigned
        dnd.roll_stats = 4  # Number of dice to roll for stats (could be defined elsewhere)
        dnd.stat_roll(dnd.user_class)  # Call the function to roll stats based on the class
        print(dnd.stat_types)  # Print the rolled stats
        if dnd.char_name.lower().strip() == "z" or dnd.char_name.lower().strip() == "zurulien":
            dnd.set_race("Pure Starling")  # Assign the race "Pure Starling" for specific names
            dnd.user_class = ["Barbarian", "Wizard"]
            dnd.user_race = "Eye of Mind"
        else:
            dnd.set_race()  # Set race for other characters
        dnd.set_level()  # Set the character's level

        mod_str = (dnd.stat_types["Str"] - 10) // 2
        mod_dex = (dnd.stat_types["Dex"] - 10) // 2
        mod_con = (dnd.stat_types["Con"] - 10) // 2
        mod_int = (dnd.stat_types["Int"] - 10) // 2
        mod_wis = (dnd.stat_types["Wis"] - 10) // 2
        mod_cha = (dnd.stat_types["Cha"] - 10) // 2
        
        dnd.calc_hit_points(dnd.user_level, dnd.user_class, mod_con)
        if dnd.user_level >= 17:
            proficiency_bonus = 6
        else:
            proficiency_bonus = proficiency[dnd.user_level]
        alignment = input("What is your alignment? (Chaotic Good, Neutral Good, Lawful Good, Lawful Neutral, True Neutral, Chaotic Neutral, Lawful Evil, Neutral Evil, Chaotic Evil) ")  # Get the character's alignment

    else:
        break  # Exit the program if the user doesn't want to start
    if save.lower().strip() == "n":
        if dnd.char_name.lower() == "andrew" or dnd.char_name.lower() == "luca" or dnd.char_name.lower() == "kai" or dnd.char_name.lower() == "z" or dnd.char_name.lower() == "zurulien":
            # If character name matches predefined names, print their stats in a specific format
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
    
        elif dnd.user_class[0].lower() == "artificer":
            # Special case for Artificer class, print their stats
            print(f"""You are an {dnd.user_class}!
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
            # Print stats for a non-specific class (or undefined class)
            print(f"""Your level is {dnd.user_level}!
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
            # General case for valid classes, print their stats
            print(f"""You are a {dnd.user_class}!
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
        print(f"Your alignment is {alignment}!")  # Output the character's alignment

        # Print the race and movement speed information
        if dnd.user_race.lower().strip() == "aasimar" or dnd.user_race.lower().strip() == "air genasi" or dnd.user_race.lower().strip() == "arachne" or dnd.user_race.lower().strip() == "aarakocra" or dnd.user_race.lower().strip() == "earth genasi" or dnd.user_race.lower().strip() == "elf":
            print(f"You are an {dnd.user_race}!")  # Special case for certain races
        else:
            print(f"You are a {dnd.user_race}!")  # General case for other races
        print(f"Your movement speed is {dnd.movement_speed}!")  # Output the character's movement speed

        # Check if the character has darkvision and print the information
        if dnd.darkvision == True:
            print("You have darkvision!")
        print(f"You know these languages:")  # Print the languages the character knows
        for x in dnd.languages:
            print("-", x)

    elif save.lower().strip() == "y":

        # Initialize dividers
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

        # Ask user what divider they want to use, if any.
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
        
        # Define the absolute path where the character sheet will be saved
        folder_path = f"C:\\Users\\{username}\\Documents\\character_sheets"  # Path where the file will be stored

        # Check if the folder exists, if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = f"{dnd.char_name}_character_sheet.txt"  # Define the filename
        full_path = os.path.join(folder_path, file_name)  # Create the full file path

        if save_type == "1":
            # If save_type is 1, overwrite the existing file or create a new one
            with open(full_path, "w+", encoding="utf-8") as file:
                file.write(f"""
Name: {dnd.char_name}
Class: {dnd.user_class}
Race: {dnd.user_race}
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

                # If the character has darkvision, write it to the file
                if dnd.darkvision == True:
                    file.write("""Darkvision\n""")
    
                file.write("\nLanguages:\n")  # Write the languages known by the character
                for x in dnd.languages:
                    file.write(f"- {x}\n")

                if divider_choice.strip() == "0": #if user inputted '0', no divider.
                    None
                else:
                    file.write(eval(f"divider{divider_choice}")) #write user-chosen divider to file and divider to separate
                    
                # Display a success message to the user using tkinter
                root = tk.Tk()
                root.withdraw()  # Hide the tkinter root window
                root.attributes('-topmost', True)  # Make the messagebox topmost
                messagebox.showinfo("Success", f"Character sheet saved to {dnd.char_name}_character_sheet.txt!")  # Show the success message
                root.attributes('-topmost', False)  # Reset the topmost attribute
                root.destroy()  # Destroy the tkinter window
                file.seek(0)  # Move the file pointer to the beginning before reading
                print(file.read())  # Read and print the file contents
                print(f'Absolute path to the file: {full_path}')  # Print the file's absolute path
                file.close()

        if save_type == "2":
            # If save_type is 2, append to an existing file
            with open(full_path, "a+", encoding="utf-8") as file:
                file.write(f"""
Name: {dnd.char_name}
Class: {dnd.user_class}
Race: {dnd.user_race}
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
    
                file.write("\nLanguages:\n")  # Write the languages known by the character
                for x in dnd.languages:
                    file.write(f"- {x}\n")

                if divider_choice.strip() == "0": # If user inputted '0', no divider.
                    None
                else:
                    file.write(eval(f"divider{divider_choice}")) # Write user-chosen divider to file and divider to separate

                # Display a success message to the user using tkinter
                root = tk.Tk()
                root.withdraw()  # Hide the tkinter root window
                root.attributes('-topmost', True)  # Make the messagebox topmost
                messagebox.showinfo("Success", f"Character sheet saved to {dnd.char_name}_character_sheet.txt!")  # Show the success message
                root.attributes('-topmost', False)  # Reset the topmost attribute
                root.destroy()  # Destroy the tkinter window
                file.seek(0)  # Move the file pointer to the beginning before reading
                print(file.read())  # Read and print the file contents
                print(f'Absolute path to the file: {full_path}')  # Print the file's absolute path
                file.close()

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
