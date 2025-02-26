#Created by Kai Reinhold (kaireinhold on GitHub)

import DnD_function_library
from DnD_function_library import Dnd

dice = Dnd()

while True:
    roll_a_dice = input("Would you like to roll a dice? (y/n) ").lower().strip()
    if roll_a_dice == "y" or roll_a_dice == "yes":
        roll_type = input("Would you like to see roll outputs as they go? (y/n) ").lower().strip()
        dice.rolls = []
        if roll_type == "y":
            dice.roll()
        else:
            dice.roll_no_output()
        print(dice.rolls)
    else:
        print("Goodbye!")
        break
