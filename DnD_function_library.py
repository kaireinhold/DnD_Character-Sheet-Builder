#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time
import os
import json

class Dnd:
    def __init__(self):
        self.rolls = []
        self.roll_output = 0
        self.for_stats = 0
        self.roll_stats = 5
        self.stats = []
        self.stat_types = {}
        self.char_name = ""
        self.user_level = 0
        self.user_race = ""
        self.movement_speed = 0
        self.darkvision = False
        self.languages = []
        self.hp_max = 0
        self.equipment = None
        self.user_background = None
        self.counter = 0

    def roll(self, di=None):
        """
        Simulate rolling dice with a specified number of sides and display the result.
    
        Input:
        - d<number> (str): A string where <number> represents the number of sides on the dice to roll, chosen by the user (e.g., 'd20' for a 20-sided die).
    
        Output:
        - str: A message indicating "Rolling d<number>..." followed by a wait of 1.5 seconds, and then another message displaying the rolled value (e.g., "d<number>: You rolled a <rolled value>!").
    
        Behavior:
        - Prompts the user to input a dice to roll (ie. 'd20' for a 20-sided dice.)
        - Rolls the specified dice and prints the result.
        - Waits for 1 seconds before displaying the result.
        - Detects if the rolled number should be preceded by 'an' (for example, 8 or 18) and adjusts the output message accordingly.
        - Appends the roll output for each roll to the list named 'rolls'

        Raises:
        - ValueError: If the input does not include the 'd' prefix, indicating the dice format.
        
        """
        
        if di is None:
            dice_chosen = input("What dice would you like to roll? (d[number]) ")
        else:
            dice_chosen = di

        dice_list = dice_chosen.lower().split()
        an_list = [11, 18]
        processed_dice = []
    
        for dice in dice_list:
            if "d" not in dice:
                raise ValueError("Value must have a 'd' in front to specify that it is a dice")
            parts = dice.split("d")
            if parts[0] == "":  
                num_rolls = 1
            else:
                num_rolls = int(parts[0])
            try:
                die_type = int(parts[1])
            except ValueError:
                raise ValueError(f"Invalid dice type in '{dice}'.")
            for _ in range(num_rolls):
                processed_dice.append(die_type)
                
        for die in processed_dice:
            print(f"Rolling d{die}...")
            time.sleep(1)
            self.roll_output = random.randint(1, die)
            output_str = str(self.roll_output)
            if self.roll_output in an_list or output_str.startswith("8"):
                print(f"d{die}: You rolled an {output_str}!")
            else:
                print(f"d{die}: You rolled a {output_str}!")

            time.sleep(0.5)
            self.rolls.append(self.roll_output)

        return self.rolls, self.roll_output

    def roll_no_output(self, di=None):
        """
        Simulate rolling dice with a specified number of sides and display the result.
    
        Input:
        - d<number> (str): A string where <number> represents the number of sides on the dice to roll, chosen by the user (e.g., 'd20' for a 20-sided die).
    
        Output:
        - None.
    
        Behavior:
        - Prompts the user to input a dice to roll (ie. 'd20' for a 20-sided dice.)
        - Rolls the specified dice and prints the result.
        - Appends the roll output for each roll to the list named 'rolls'

        Raises:
        - ValueError: If the input does not include the 'd' prefix, indicating the dice format.
        
        """
        
        if di is None:
            dice_chosen = input("What dice would you like to roll? (d[number]) ")
        else:
            dice_chosen = di

        dice_list = dice_chosen.lower().split()
        processed_dice = []
    
        for dice in dice_list:
            if "d" not in dice:
                raise ValueError("Value must have a 'd' in front to specify that it is a dice")
            parts = dice.split("d")
            if parts[0] == "":  
                num_rolls = 1
            else:
                num_rolls = int(parts[0])
            try:
                die_type = int(parts[1])
            except ValueError:
                raise ValueError(f"Invalid dice type in '{dice}'.")
            for _ in range(num_rolls):
                processed_dice.append(die_type)
                
        for die in processed_dice:
            self.roll_output = random.randint(1, die)
            self.rolls.append(self.roll_output)

        return self.rolls, self.roll_output

    def stat_roll(self, u_class=None):
        while self.for_stats < 6:
            while self.roll_stats > 0:
                self.roll_stats -= 1
                self.roll_no_output("d6")
            
                if self.rolls[-1] == 1:
                    self.rolls.pop()
                    self.roll_stats += 1
                elif len(self.rolls) == 4:
                    self.rolls.remove(min(self.rolls))
                    self.stats.append(sum(self.rolls))
                    self.rolls = []
                    self.for_stats += 1
                    if self.for_stats >= 6:
                        break
                    self.roll_stats = 5

        if self.char_name.lower() == "z" or self.char_name.lower() == "zurulien":
            self.stats.sort()
            self.stat_types = {"Str": self.stats[4], "Dex": self.stats[0], "Con": self.stats[1], "Int": self.stats[5], "Wis": self.stats[3], "Cha": self.stats[2]}
        elif self.char_name.lower() == "andrew" or self.char_name.lower() == "luca" or self.char_name.lower() == "kai":
            # Special Easter egg for friends/fellow DMs
            self.stats = [20]
            self.stat_types = {"Str": self.stats[0], "Dex": self.stats[0], "Con": self.stats[0], "Int": self.stats[0], "Wis": self.stats[0], "Cha": self.stats[0]}
        elif u_class == None or u_class == "":
            self.stat_types = {"Str": self.stats[0], "Dex": self.stats[1], "Con": self.stats[2], "Int": self.stats[3], "Wis": self.stats[4], "Cha": self.stats[5]}
        else:
            if u_class[0].lower() == "barbarian":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[5], "Dex": self.stats[3], "Con": self.stats[4], "Int": self.stats[0], "Wis": self.stats[2], "Cha": self.stats[1]}
            elif u_class[0].lower() == "fighter":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[5], "Dex": self.stats[1], "Con": self.stats[3], "Int": self.stats[4], "Wis": self.stats[0], "Cha": self.stats[2]}
            elif u_class[0].lower() == "wizard":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[4], "Con": self.stats[3], "Int": self.stats[5], "Wis": self.stats[2], "Cha": self.stats[1]}
            elif u_class[0].lower() == "rogue":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[5], "Con": self.stats[4], "Int": self.stats[1], "Wis": self.stats[2], "Cha": self.stats[3]}
            elif u_class[0].lower() == "bard":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[4], "Con": self.stats[3], "Int": self.stats[1], "Wis": self.stats[2], "Cha": self.stats[5]}
            elif u_class[0].lower() == "druid":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[3], "Con": self.stats[4], "Int": self.stats[2], "Wis": self.stats[5], "Cha": self.stats[1]}
            elif u_class[0].lower() == "paladin":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[5], "Dex": self.stats[1], "Con": self.stats[3], "Int": self.stats[0], "Wis": self.stats[2], "Cha": self.stats[4]}
            elif u_class[0].lower() == "cleric":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[3], "Dex": self.stats[2], "Con": self.stats[4], "Int": self.stats[1], "Wis": self.stats[5], "Cha": self.stats[0]}
            elif u_class[0].lower() == "monk":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[4], "Dex": self.stats[2], "Con": self.stats[3], "Int": self.stats[1], "Wis": self.stats[5], "Cha": self.stats[0]}
            elif u_class[0].lower() == "ranger":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[5], "Dex": self.stats[3], "Con": self.stats[4], "Int": self.stats[1], "Wis": self.stats[2], "Cha": self.stats[0]}
            elif u_class[0].lower() == "sorcerer":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[3], "Con": self.stats[4], "Int": self.stats[2], "Wis": self.stats[1], "Cha": self.stats[5]}
            elif u_class[0].lower() == "warlock":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[3], "Con": self.stats[4], "Int": self.stats[1], "Wis": self.stats[2], "Cha": self.stats[5]}
            elif u_class[0].lower() == "artificer":
                self.stats.sort()
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[3], "Con": self.stats[4], "Int": self.stats[5], "Wis": self.stats[2], "Cha": self.stats[1]}
            else:
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[1], "Con": self.stats[2], "Int": self.stats[3], "Wis": self.stats[4], "Cha": self.stats[5]}

        return self.stat_types

    def stat_increase(self, inc_amount = None):
        if inc_amount == None:
            inc_amount = int(input(""" How do you want to increase your stats?
(1) Increase 1 stat by 2 points
(2) Increase 2 stats by 1 point each
"""))
    
        if inc_amount == 1:
            stat_to_inc = input("What stat do you want to increase? (Choose 1: Str, Dex, Con, Int, Wis, Cha) ")
            inc_list = stat_to_inc.split(" ")
            if len(inc_list) > 1:
                incs = inc_list
                inc_list = [incs[0]]

            for stat in inc_list:
                if stat.lower().strip() == "str":
                    self.stat_types["Str"] += 2
                elif stat_to_inc.lower().strip() == "dex":
                    self.stat_types["Dex"] += 2
                elif stat_to_inc.lower().strip() == "con":
                    self.stat_types["Con"] += 2
                elif stat_to_inc.lower().strip() == "int":
                    self.stat_types["Int"] += 2
                elif stat_to_inc.lower().strip() == "wis":
                    self.stat_types["Wis"] += 2
                elif stat_to_inc.lower().strip() == "cha":
                    self.stat_types["Cha"] += 2
                else: self.counter -= 1

        elif inc_amount == 2:
            stats_to_inc = input("What stats do you want to increase? (Choose 2, separate by a comma: Str, Dex, Con, Int, Wis, Cha) ")
            inc_list = stats_to_inc.split(",")
            if len(inc_list) > 2:
                incs = inc_list
                inc_list = [incs[0], incs[1]]
        
            for stat in inc_list:
                if stat.lower().strip() == "str":
                    self.stat_types["Str"] += 1
                elif stat.lower().strip() == "dex":
                    self.stat_types["Dex"] += 1
                elif stat.lower().strip() == "con":
                    self.stat_types["Con"] += 1
                elif stat.lower().strip() == "int":
                    self.stat_types["Int"] += 1
                elif stat.lower().strip() == "wis":
                    self.stat_types["Wis"] += 1
                elif stat.lower().strip() == "cha":
                    self.stat_types["Cha"] += 1
                else: self.counter -= 1
        else: self.counter -= 1

        print(self.stat_types)
    
        return self.stat_types

    def set_level(self):
        self.user_level = int(input("What level is your character? (number) "))
        if self.user_level == 19:
            number = 20
        else:
            number = self.user_level

        self.counter = 0
        while self.counter < len(range(4, number+1, 4)):
            self.counter += 1
            self.stat_increase()
            print(self.counter)
    
        return self.user_level

    def set_race(self, race = None):
        
        if race == None:
            self.user_race = input("What race is your character? (Dwarf, Half-orc, Elf, Halfling, Human, Dragonborn, Gnome, Half-elf, Tiefling, Aasimar, Changeling, Kenku, Warforged, Arachne, Shifter, Aarakocra, Kobold, Fire Genasi, Air Genasi, Earth Genasi, Water Genasi, Goliath) ")
        else:
            self.user_race = race

        if self.user_race.lower().strip() == "dwarf":
            self.stat_types["Con"] += 2
            self.movement_speed = 25
            self.darkvision = True
            self.languages = ["Common", "Dwarvish"]
        elif self.user_race.lower().strip() == "half-orc":
            self.stat_types["Str"] += 2
            self.stat_types["Con"] += 1
            self.movement_speed = 30
            self.darkvision = True
            self.languages = ["Common", "Orc"]
        elif self.user_race.lower().strip() == "elf":
            self.stat_types["Dex"] += 2
            self.movement_speed = 30
            self.darkvision = True
            self.languages = ["Common", "Elven"]
        elif self.user_race.lower().strip() == "halfling":
            self.stat_types["Dex"] += 2
            self.movement_speed = 25
            self.darkvision = False
            self.languages = ["Common", "Halfling"]
        elif self.user_race.lower().strip() == "human":
            self.stat_types["Str"] += 1
            self.stat_types["Dex"] += 1
            self.stat_types["Con"] += 1
            self.stat_types["Int"] += 1
            self.stat_types["Wis"] += 1
            self.stat_types["Cha"] += 1
            self.movement_speed = 30
            self.darkvision = False
            self.languages = ["Common", input("Choose 1 language other than Common: ")]
        elif self.user_race.lower().strip() == "dragonborn":
            self.stat_types["Str"] += 2
            self.stat_types["Cha"] += 1
            self.movement_speed = 30
            self.darkvision = False
            self.languages = ["Common", "Draconic"]
        elif self.user_race.lower().strip() == "gnome":
            self.stat_types["Int"] += 2
            self.movement_speed = 25
            self.darkvision = True
            self.languages = ["Common", "Gnomish"]
        elif self.user_race.lower().strip() == "half-elf":
            self.stat_types["Cha"] += 2
            self.stat_increase(2)
            self.movement_speed = 30
            self.darkvision = True
            self.languages = ["Common", "Elven", input("Choose 1 language other than Common and Elven: ")]
        elif self.user_race.lower().strip() == "tiefling":
            self.stat_types["Cha"] += 2
            self.movement_speed = 30
            self.darkvision = True
            self.languages = ["Common", "Infernal"]
        elif self.user_race.lower().strip() == "aasimar" or self.user_race.lower().strip() == "changeling" or self.user_race.lower().strip() == "kenku" or self.user_race.lower().strip() == "shifter" or self.user_race.lower().strip() == "aarakocra" or self.user_race.lower().strip() == "kobold" or self.user_race.lower().strip() == "fire genasi" or self.user_race.lower().strip() == "air genasi" or self.user_race.lower().strip() == "water genasi" or self.user_race.lower().strip() == "earth genasi":
            self.stat_types[input("Choose 1 score to increase by 1 (Str, Dex, Con, Int, Wis, Cha) ").capitalize().strip()] += 1
            inc_2 = int(input("Would you like to increase one score by 2 points (1), or 2 scores by 1 point each (2)? ").strip())
            if inc_2 == 1:
                self.stat_increase(1)
            elif inc_2 == 2:
                self.stat_increase(2)
            if self.user_race.lower().strip() == "air genasi":
                self.movement_speed = 35
            else:
                self.movement_speed = 30
            if self.user_race.lower().strip() == "aarakocra":
                self.darkvision = False
            else:
                self.darkvision = True
            self.languages = ["Common", input("What language other than Common have you agreed on with your DM? ")]
        elif self.user_race.lower().strip() == "warforged":
            self.stat_types["Con"] += 2
            self.stat_types[input("Choose 1 score to increase by 1 (Str, Dex, Con, Int, Wis, Cha) ").capitalize().strip()] += 1
            self.movement_speed = 30
            self.darkvision = False
            self.languages = ["Common", input("Choose 1 language other than Common: ")]
        elif self.user_race.lower().strip() == "arachne":
            self.stat_types["Dex"] += 2
            self.stat_types["Wis"] += 1
            self.movement_speed = 30
            self.darkvision = True
            self.languages = ["Common", "Undercommon"]
        elif self.user_race.lower().strip() == "goliath":
            self.stat_types["Str"] += 2
            self.stat_types["Con"] += 1
            self.movement_speed = 30
            self.darkvision = True
            self.languages = ["Common", "Giant"]
        elif self.user_race.lower().strip() == "starling" or self.user_race.lower().strip() == "bloodling" or self.user_race.lower().strip() == "core starling" or self.user_race.lower().strip() == "shadeling" or self.user_race.lower().strip() == "crystalling" or self.user_race.lower().strip() == "symbioling" or self.user_race.lower().strip() == "pure starling":
            current_race = self.user_race
            if self.user_race.lower().strip() != "pure starling":
                prev_race = input("What race were you before? ")
                self.set_race(prev_race)
                self.movement_speed += 10
            else:
                self.set_race("human")
                self.movement_speed += 15
            self.user_race = current_race
            self.stat_increase(2)
            self.darkvision = True
            self.languages.append("Sangulect")
        else:
            self.movement_speed = 30
            self.darkvision = False
            self.languages = ["Common"]
        
        print(self.stat_types)

    def calc_hit_points(self, level=1, u_class=None, con_modifier=1):
        if isinstance(u_class, list): 
            for var in u_class:
                if var == None or var == "":
                    self.hp_max += 8 + con_modifier
                    for num in range((level - 1) // len(u_class)):
                        self.hp_max += con_modifier
                        self.roll_no_output("d8")
                        self.hp_max += self.rolls[len(self.rolls)-1]
                else:
                    if var.lower().strip() in ["artificer", "bard", "druid", "cleric", "monk", "rogue", "warlock"]:
                        self.hp_max += 8 + con_modifier 
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d8")
                                self.hp_max += self.rolls[len(self.rolls)-1]
                
                    elif var.lower().strip() in ["fighter", "paladin", "ranger"]:
                        self.hp_max += 10 + con_modifier
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d10")
                                self.hp_max += self.rolls[len(self.rolls)-1]

                    elif var.lower().strip() in ["sorcerer", "wizard"]:
                        self.hp_max += 6 + con_modifier
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d6")
                                self.hp_max += self.rolls[len(self.rolls)-1]

                    elif var.lower().strip() == "barbarian":
                        self.hp_max += 12 + con_modifier
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d12")
                                self.hp_max += self.rolls[len(self.rolls)-1]

                    else:
                        self.hp_max += 12 + con_modifier
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d8")
                                self.hp_max += self.rolls[len(self.rolls)-1]

        elif u_class == None or u_class == "":
            self.hp_max += 8 + con_modifier
            for num in range((level - 1) // len(u_class)):
                self.hp_max += con_modifier
                self.roll_no_output("d8")
                self.hp_max += self.rolls[len(self.rolls)-1]

        return self.hp_max

    def save_to_json_file(self, character_data, user_name, char_name):
        folder_path = f"C:\\Users\\{user_name}\\Documents\\GitHub\\DnD_Character-Sheet-Builder"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, "DnD_Database.json")

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
        char_key = char_name
        data["Characters"] = [c for c in data["Characters"] if char_key not in c]
        data["Character_Skills"] = [s for s in data["Character_Skills"] if f"{char_key}_skills" not in s]
        data["Character_Inventory"] = [i for i in data["Character_Inventory"] if f"{char_key}_inventory" not in i]
        data["Character_Spells"] = [s for s in data["Character_Spells"] if f"{char_key}_spells" not in s]


        character_info = character_data["Characters"][0][char_name]
        skills_block = character_data["Character_Skills"][0]
        inventory_block = character_data["Character_Inventory"][0]
        spells_block = character_data["Character_Spells"][0]

        # Add the new character
        data["Characters"].append({char_name: character_info})
        data["Character_Skills"].append(skills_block)
        data["Character_Inventory"].append(inventory_block)
        data["Character_Spells"].append(spells_block)

        # Save updated data
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def set_background(self, char_class=None, char_race=None):
        pass

    def skill_proficiency(self, char_class=None, char_race=None, char_background=None):
        pass

    def give_equipment(self,):
        pass

    def remove_equipment(self,):
        pass

    def armor_class_calc(self, u_armor, u_race):
        pass

    def spells(self, u_background, u_class, u_race):
        pass

    def level_up(self,):
        pass
