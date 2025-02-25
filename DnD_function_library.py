#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time

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
        #self.

    # Function to simulate rolling dice with output shown
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
            self.rolls.append(self.roll_output)  # Add roll to instance list

        return self.rolls, self.roll_output  # Return the rolls for the current instance
    
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
            self.rolls.append(self.roll_output)  # Add roll to instance list

        return self.rolls, self.roll_output  # Return the rolls for the current instance


    # Function to simulate rolling stats for a character (ability scores)
    def stat_roll(self, u_class=None):
        # Loop to generate the 6 stats (Str, Dex, Con, Int, Wis, Cha)
        while self.for_stats < 6:
            # Roll stats by rolling a d6 5 times (standard stat rolling)
            while self.roll_stats > 0:
                self.roll_stats -= 1  # Decrease the number of rolls remaining for this stat
                self.roll_no_output("d6")  # Call the function to roll a d6 (side effect: updates `rolls`)
            
                # If a roll is a 1, discard it and roll again (penalizing bad rolls)
                if self.rolls[-1] == 1:
                    self.rolls.pop()  # Remove the 1 from the rolls list
                    self.roll_stats += 1  # Increase the roll count to redo this roll
                elif len(self.rolls) == 4:
                    # After 4 valid rolls, discard the lowest roll and sum the rest
                    self.rolls.remove(min(self.rolls))  # Remove the smallest value
                    self.stats.append(sum(self.rolls))  # Append the sum of the remaining 3 rolls to `stats`
                    self.rolls = []  # Reset the rolls list for the next stat
                    self.for_stats += 1  # Increment the stat count
                    if self.for_stats >= 6:
                        break  # Stop once all 6 stats are rolled
                    self.roll_stats = 5  # Reset the roll count for the next stat

        # Special stat assignment for specific character names (Easter egg for certain characters)
        if self.char_name.lower() == "z" or self.char_name.lower() == "zurulien":
            self.stats.sort()  # Sort stats for this character
            self.stat_types = {"Str": self.stats[4], "Dex": self.stats[0], "Con": self.stats[1], "Int": self.stats[5], "Wis": self.stats[3], "Cha": self.stats[2]}  # Assign stats
        elif self.char_name.lower() == "andrew" or self.char_name.lower() == "luca" or self.char_name.lower() == "kai":
            # Special Easter egg for friends/fellow DMs
            self.stats = [20]  # Assign max value (20) to all stats
            self.stat_types = {"Str": self.stats[0], "Dex": self.stats[0], "Con": self.stats[0], "Int": self.stats[0], "Wis": self.stats[0], "Cha": self.stats[0]}  # Set all stats to 20
        elif u_class == None or u_class == "":
            # If no class is specified, just assign stats in order
            self.stat_types = {"Str": self.stats[0], "Dex": self.stats[1], "Con": self.stats[2], "Int": self.stats[3], "Wis": self.stats[4], "Cha": self.stats[5]}
        else:
            # Assign stats based on the selected class (this part handles class-specific stat priorities)
            if u_class[0].lower() == "barbarian":
                self.stats.sort()  # Sort stats in ascending order
                self.stat_types = {"Str": self.stats[5], "Dex": self.stats[3], "Con": self.stats[4], "Int": self.stats[0], "Wis": self.stats[2], "Cha": self.stats[1]}  # Assign stats based on class
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
                # Default stat assignment if no specific class is selected
                self.stat_types = {"Str": self.stats[0], "Dex": self.stats[1], "Con": self.stats[2], "Int": self.stats[3], "Wis": self.stats[4], "Cha": self.stats[5]}
    
        # Return the dictionary of final stat assignments
        return self.stat_types

    # Function to handle stat increases based on user choice
    def stat_increase(self, inc_amount = None):
        # If no input is provided for how to increase the stats, ask the user
        if inc_amount == None:
            inc_amount = int(input(""" How do you want to increase your stats?
(1) Increase 1 stat by 2 points
(2) Increase 2 stats by 1 point each
"""))
    
        # Case 1: Increase 1 stat by 2 points
        if inc_amount == 1:
            # Ask the user which stat they want to increase
            stat_to_inc = input("What stat do you want to increase? (Choose 1: Str, Dex, Con, Int, Wis, Cha) ")
            counter = [1]  # Loop counter, only runs once because we are only increasing one stat
            for x in counter:
                # Check the stat the user chose and increase it by 2 points
                if stat_to_inc.lower().strip() == "str":
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

        # Case 2: Increase 2 stats by 1 point each
        elif inc_amount == 2:
            # Ask the user which two stats they want to increase
            stats_to_inc = input("What stats do you want to increase? (Choose 2, separate by a comma: Str, Dex, Con, Int, Wis, Cha) ")
            inc_list = stats_to_inc.split(",")  # Split the input string into a list of stats to increase
            # If more than two stats are chosen, only take the first two
            if len(inc_list) > 2:
                incs = inc_list
                inc_list = [incs[0], incs[1]]
        
            # Increase each of the chosen stats by 1 point
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

        # Print the updated stat values after the increase
        print(self.stat_types)
    
        # Return the updated dictionary of stats
        return self.stat_types

    # Function to set the character's level and apply stat increases based on the level
    def set_level(self):
        
        # Ask the user to input their character's level
        self.user_level = int(input("What level is your character? (number) "))
        
        # Apply stat increases based on the user's character level
        # The higher the level, the more stat increases the character gets
        if self.user_level > 20:
            self.stat_increase(), self.stat_increase(), self.stat_increase(), self.stat_increase()
            for level in range(19, self.user_level+1, 4):
                self.stat_increase()
        if self.user_level >= 19:
            # If level is 19 or higher, apply five stat increases
            self.stat_increase(), self.stat_increase(), self.stat_increase(), self.stat_increase(), self.stat_increase()
        elif self.user_level >= 16:
            # If level is between 16 and 18, apply four stat increases
            self.stat_increase(), self.stat_increase(), self.stat_increase(), self.stat_increase()
        elif self.user_level >= 12:
            # If level is between 12 and 15, apply three stat increases
            self.stat_increase(), self.stat_increase(), self.stat_increase()
        elif self.user_level >= 8:
            # If level is between 8 and 11, apply two stat increases
            self.stat_increase(), self.stat_increase()
        elif self.user_level >= 4:
            # If level is between 4 and 7, apply one stat increase
            self.stat_increase()
    
        # Return the user's level to be used elsewhere in the program
        return self.user_level


    # Function to set the character's race and apply race-specific stat bonuses
    def set_race(self, race = None):
        
       # Ask the user for their character's race if not provided
        if race == None:
            self.user_race = input("What race is your character? (Dwarf, Half-orc, Elf, Halfling, Human, Dragonborn, Gnome, Half-elf, Tiefling, Aasimar, Changeling, Kenku, Warforged, Arachne, Shifter, Aarakocra, Kobold, Fire Genasi, Air Genasi, Earth Genasi, Water Genasi, Goliath) ")
        else:
            self.user_race = race  # Use the provided race if passed as an argument

        # Apply race-specific stat bonuses, movement speed, darkvision, and languages
        # Each race has different attributes that get applied here
        if self.user_race.lower().strip() == "dwarf":
            self.stat_types["Con"] += 2  # Dwarfs gain +2 Constitution
            self.movement_speed = 25  # Dwarfs have a movement speed of 25
            self.darkvision = True  # Dwarfs have darkvision
            self.languages = ["Common", "Dwarvish"]  # Dwarfs speak Common and Dwarvish
        elif self.user_race.lower().strip() == "half-orc":
            self.stat_types["Str"] += 2  # Half-orcs gain +2 Strength
            self.stat_types["Con"] += 1  # Half-orcs gain +1 Constitution
            self.movement_speed = 30  # Half-orcs have a movement speed of 30
            self.darkvision = True  # Half-orcs have darkvision
            self.languages = ["Common", "Orc"]  # Half-orcs speak Common and Orc
        elif self.user_race.lower().strip() == "elf":
            self.stat_types["Dex"] += 2  # Elves gain +2 Dexterity
            self.movement_speed = 30  # Elves have a movement speed of 30
            self.darkvision = True  # Elves have darkvision
            self.languages = ["Common", "Elven"]  # Elves speak Common and Elven
        elif self.user_race.lower().strip() == "halfling":
            self.stat_types["Dex"] += 2  # Halflings gain +2 Dexterity
            self.movement_speed = 25  # Halflings have a movement speed of 25
            self.darkvision = False  # Halflings do not have darkvision
            self.languages = ["Common", "Halfling"]  # Halflings speak Common and Halfling
        elif self.user_race.lower().strip() == "human":
            # Humans gain +1 to all stats
            self.stat_types["Str"] += 1
            self.stat_types["Dex"] += 1
            self.stat_types["Con"] += 1
            self.stat_types["Int"] += 1
            self.stat_types["Wis"] += 1
            self.stat_types["Cha"] += 1
            self.movement_speed = 30  # Humans have a movement speed of 30
            self.darkvision = False  # Humans do not have darkvision
            self.languages = ["Common", input("Choose 1 language other than Common: ")]  # Humans speak Common and one other language
        elif self.user_race.lower().strip() == "dragonborn":
            self.stat_types["Str"] += 2  # Dragonborn gain +2 Strength
            self.stat_types["Cha"] += 1  # Dragonborn gain +1 Charisma
            self.movement_speed = 30  # Dragonborn have a movement speed of 30
            self.darkvision = False  # Dragonborn do not have darkvision
            self.languages = ["Common", "Draconic"]  # Dragonborn speak Common and Draconic
        elif self.user_race.lower().strip() == "gnome":
            self.stat_types["Int"] += 2  # Gnomes gain +2 Intelligence
            self.movement_speed = 25  # Gnomes have a movement speed of 25
            self.darkvision = True  # Gnomes have darkvision
            self.languages = ["Common", "Gnomish"]  # Gnomes speak Common and Gnomish
        elif self.user_race.lower().strip() == "half-elf":
            self.stat_types["Cha"] += 2  # Half-elves gain +2 Charisma
            self.stat_increase(2)  # Half-elves also get two stat increases
            self.movement_speed = 30  # Half-elves have a movement speed of 30
            self.darkvision = True  # Half-elves have darkvision
            self.languages = ["Common", "Elven", input("Choose 1 language other than Common and Elven: ")]  # Half-elves speak Common, Elven, and one other language
        elif self.user_race.lower().strip() == "tiefling":
            self.stat_types["Cha"] += 2  # Tieflings gain +2 Charisma
            self.movement_speed = 30  # Tieflings have a movement speed of 30
            self.darkvision = True  # Tieflings have darkvision
            self.languages = ["Common", "Infernal"]  # Tieflings speak Common and Infernal
        # Many additional races with specific attributes
        elif self.user_race.lower().strip() == "aasimar" or self.user_race.lower().strip() == "changeling" or self.user_race.lower().strip() == "kenku" or self.user_race.lower().strip() == "shifter" or self.user_race.lower().strip() == "aarakocra" or self.user_race.lower().strip() == "kobold" or self.user_race.lower().strip() == "fire genasi" or self.user_race.lower().strip() == "air genasi" or self.user_race.lower().strip() == "water genasi" or self.user_race.lower().strip() == "earth genasi":
            self.stat_types[input("Choose 1 score to increase by 1 (Str, Dex, Con, Int, Wis, Cha) TYPE EXACTLY: ").strip()] += 1  # Choose 1 stat to increase by 1
            inc_2 = int(input("Would you like to increase one score by 2 points (1), or 2 scores by 1 point each (2)? ").strip())  # Choose if one stat should increase by 2 or two stats by 1 each
            if inc_2 == 1:
                self.stat_increase(1)  # Apply 1 stat increase
            elif inc_2 == 2:
                self.stat_increase(2)  # Apply 2 stat increases
            if self.user_race.lower().strip() == "air genasi":
                self.movement_speed = 35  # Air Genasi move faster (35)
            else:
                self.movement_speed = 30  # Other races move at a normal speed (30)
            self.darkvision = True  # Most of these races have darkvision
            self.languages = ["Common", input("What language other than Common have you agreed on with your DM? ")]  # Ask for a DM-approved language
        elif self.user_race.lower().strip() == "warforged":
            self.stat_types["Con"] += 2  # Warforged gain +2 Constitution
            self.stat_types[input("Choose 1 score to increase by 1 (Str, Dex, Con, Int, Wis, Cha) TYPE EXACTLY: ").strip()] += 1  # Warforged get to increase another stat by 1
            self.movement_speed = 30  # Warforged have a movement speed of 30
            self.darkvision = False  # Warforged do not have darkvision
            self.languages = ["Common", input("Choose 1 language other than Common: ")]  # Warforged speak Common and one other language
        elif self.user_race.lower().strip() == "arachne":
            self.stat_types["Dex"] += 2  # Arachne gain +2 Dexterity
            self.stat_types["Wis"] += 1  # Arachne gain +1 Wisdom
            self.movement_speed = 30  # Arachne have a movement speed of 30
            self.darkvision = True  # Arachne have darkvision
            self.languages = ["Common", "Undercommon"]  # Arachne speak Common and Undercommon
        elif self.user_race.lower().strip() == "goliath":
            self.stat_types["Str"] += 2
            self.stat_types["Con"] += 1
            self.movement_speed = 30
            self.darkvision = True
            self.languages = ["Common", "Giant"]
        elif self.user_race.lower().strip() == "starling" or self.user_race.lower().strip() == "bloodling" or self.user_race.lower().strip() == "core starling" or self.user_race.lower().strip() == "shadeling" or self.user_race.lower().strip() == "crystalling" or self.user_race.lower().strip() == "symbioling" or self.user_race.lower().strip() == "pure starling":
            current_race = self.user_race  # Store current race to handle complex starling-related logic
            if self.user_race.lower().strip() != "pure starling":
                prev_race = input("What race were you before? ")  # Get previous race if not pure starling
                self.set_race(prev_race)  # Call set_race to apply the previous race
                self.movement_speed += 10  # Increase movement speed for certain starlings
            else:
                self.set_race("human")  # If pure starling, reset to human race
                self.movement_speed += 15  # Increase movement speed for pure starling
            self.user_race = current_race  # Restore the current race
            self.stat_increase(2)  # Apply two stat increases
            self.darkvision = True  # Starling races have darkvision
            self.languages.append("Sangulect")  # Starling races speak Sangulect
        else:
            # Default case for any unrecognized races
            self.movement_speed = 30  # Default movement speed
            self.darkvision = False  # Default: no darkvision
            self.languages = ["Common"]  # Default language is Common
        
        # Output the character's stats for verification
        print(self.stat_types)

    def calc_hit_points(self, level=1, u_class=None, con_modifier=1):
        # Check if the user's class is a list (multiclass character)
        if isinstance(u_class, list): 
            for var in u_class:  # Iterate through each class in the list
                # If class is None or empty, assume default hit dice (d8)
                if var == None or var == "":
                    self.hp_max += 8 + con_modifier  # Base HP for level 1
                    for num in range((level - 1) // len(u_class)):  # Roll hit dice for remaining levels
                        self.hp_max += con_modifier  # Add Constitution modifier
                        self.roll_no_output("d8")  # Roll a d8 hit die
                        self.hp_max += self.rolls[len(self.rolls)-1]  # Add the rolled result
                else:
                    # Check if the class belongs to the d8 hit dice group
                    if var.lower().strip() in ["artificer", "bard", "druid", "cleric", "monk", "rogue", "warlock"]:
                        self.hp_max += 8 + con_modifier  # Base HP for level 1
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):  # Roll hit dice for remaining levels
                                self.hp_max += con_modifier
                                self.roll_no_output("d8")  # Roll a d8
                                self.hp_max += self.rolls[len(self.rolls)-1]
                
                    # Check if the class belongs to the d10 hit dice group
                    elif var.lower().strip() in ["fighter", "paladin", "ranger"]:
                        self.hp_max += 10 + con_modifier  # Base HP for level 1
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d10")  # Roll a d10
                                self.hp_max += self.rolls[len(self.rolls)-1]

                    # Check if the class belongs to the d6 hit dice group
                    elif var.lower().strip() in ["sorcerer", "wizard"]:
                        self.hp_max += 6 + con_modifier  # Base HP for level 1
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d6")  # Roll a d6
                                self.hp_max += self.rolls[len(self.rolls)-1]

                    # Check if the class is a Barbarian (d12 hit dice)
                    elif var.lower().strip() == "barbarian":
                        self.hp_max += 12 + con_modifier  # Base HP for level 1
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d12")  # Roll a d12
                                self.hp_max += self.rolls[len(self.rolls)-1]

                    # Default case (unknown class), assume d8 hit dice
                    else:
                        self.hp_max += 12 + con_modifier
                        if level != 1:
                            for num in range((level - 1) // len(u_class)):
                                self.hp_max += con_modifier
                                self.roll_no_output("d8")  # Roll a d8
                                self.hp_max += self.rolls[len(self.rolls)-1]

        # If the class is None or an empty string (assume default d8 hit dice)
        elif u_class == None or u_class == "":
            self.hp_max += 8 + con_modifier  # Base HP for level 1
            for num in range((level - 1) // len(u_class)):
                self.hp_max += con_modifier
                self.roll_no_output("d8")  # Roll a d8
                self.hp_max += self.rolls[len(self.rolls)-1]

        return self.hp_max  # Return the final calculated max HP

    def background(self, char_class=None, char_race=None):
        pass
    def skill_proficiency(self, char_class=None, char_race=None):
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
