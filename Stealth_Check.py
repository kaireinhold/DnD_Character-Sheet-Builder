# Created by Andrew86-lab and KaiReinhold

import math
import random
import DnD_function_library
from DnD_function_library import Dnd

dnd = Dnd()

class Game:
    def __init__(self):
        self.user_advantage = "None"
        self.enemy_perception = 1
        self.stealth_check = 1
        self.dice = 1
    
    def advantage(self=__init__):
        self.user_advantage = "None"

        dnd.rolls = []
        self.user_advantage = input("Do you have Advantage or Disadvantage? (A, D, or None) ")
        if self.user_advantage.lower().strip() == 'a':
            dnd.roll_no_output("2d20")
            print(dnd.rolls)
            self.dice = max(dnd.rolls)
        elif self.user_advantage.lower().strip() == 'd':
            dnd.roll_no_output("2d20")
            print(dnd.rolls)
            self.dice = min(dnd.rolls)
        else:
            dnd.roll_no_output("1d20")
            print(dnd.rolls)
            self.dice = dnd.rolls[-1]
    
    def user_check(self=__init__):
        self.stealth_check = 1

        user_level = input("What is your character's level? ")
        if user_level == "" or "1234567890" not in user_level:
            user_level = 1

        proficiency_bonus = math.ceil((int(user_level) / 4) + 1)

        is_user_dex = input("Do you know your character's dexterity modifier? (Y/N) ").lower().strip()
        if is_user_dex not in ['y', 'n']:
            is_user_dex = 'n'

        stealth_proficiency = input("Do you have proficiency in the Stealth skill? (Y/N) ").lower().strip()
        if stealth_proficiency not in ['y', 'n']:
            stealth_proficiency = 'n'
        stealth_expertise = "n"
        if stealth_proficiency == "y":
            stealth_expertise = input("Do you have expertise in the Stealth skill? (Y/N) ").lower().strip()
            if stealth_expertise not in ['y', 'n']:
                stealth_expertise = 'n'

        user_dexterity = 1
        if is_user_dex == "y":
                user_dexterity = input("What is your character's dexterity modifier? ").strip()
                if user_dexterity == "" or "1234567890" not in user_dexterity:
                    user_dexterity = 1

        elif is_user_dex == "n":
                dex_score = input("What is your character's dexterity score? ").strip()
                if dex_score == "" or "1234567890" not in dex_score:
                    dex_score = 1
                user_dexterity = (int(dex_score) - 10) // 2

        print(f"You rolled a {self.dice}")

        self.stealth_check = self.dice + int(user_dexterity)
        if stealth_expertise == "y":
            self.stealth_check += (proficiency_bonus * 2)
        elif stealth_proficiency == "y":
            self.stealth_check += proficiency_bonus

        print(f"Your stealth check is {self.stealth_check}.")
        
        return self.stealth_check
    
    def enemy_check(self=__init__):
        self.enemy_perception = 1

        is_enemy_check = input("Do you know the enemy's perception check? (Y/N) ").lower().strip()
        if is_enemy_check not in ['y', 'n']:
            is_enemy_check = "n"

        if is_enemy_check == "n":
            enemy_challenge_rating = input("What is the challenge rating of the enemy? ").strip()
            if enemy_challenge_rating == "" or "1234567890" not in enemy_challenge_rating:
                enemy_challenge_rating = 0

            if float(enemy_challenge_rating) == 0:
                enemy_bonus = 2
            elif float(enemy_challenge_rating) > 0:
                enemy_bonus = math.ceil(float(enemy_challenge_rating) / 4) + 1


            dnd.rolls = []
            if self.user_advantage.lower().strip() == 'd':
                dnd.roll_no_output("2d20")
                print(dnd.rolls)
                enemy_dice = max(dnd.rolls)
            elif self.user_advantage.lower().strip() == 'a':
                dnd.roll_no_output("2d20")
                print(dnd.rolls)
                enemy_dice = min(dnd.rolls)
            else:
                dnd.roll_no_output("1d20")
                print(dnd.rolls)
                enemy_dice = dnd.rolls[-1]

            
            enemy_wis = input("Do you know the enemy's wisdom modifier? (Y/N) ").lower().strip()
            if enemy_wis not in ['y', 'n']:
                enemy_wis = 'n'

            if enemy_wis == "y":
                enemy_wisdom = input("What is the enemy's wisdom modifier? ").strip()
                if enemy_wisdom == "" or "1234567890" not in enemy_wisdom:
                    enemy_wisdom = 1
            elif enemy_wis == "n":
                enemy_wisdom = input("What is your enemy's wisdom score? ").strip()
                if enemy_wisdom == "" or "1234567890" not in enemy_wisdom:
                    enemy_wisdom = 1
                enemy_wisdom = (int(enemy_wisdom) - 10) // 2

            self.enemy_perception = enemy_dice + int(enemy_wisdom) + enemy_bonus

            print(f"The enemy rolled a {enemy_dice} and the enemy's perception check is {self.enemy_perception}.")
        elif is_enemy_check == "y":
                self.enemy_perception = int(input("What is the enemy's perception check? ").strip())
                if self.enemy_perception == "" or "1234567890" not in self.enemy_perception:
                    self.enemy_perception = 1
        return self.enemy_perception

game = Game()

while True:
    game.advantage()
    game.user_check()
    game.enemy_check()
    if game.stealth_check > game.enemy_perception:
        print("You are hidden from the enemy.")
    else:
        print("You failed the stealth check.")
