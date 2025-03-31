import random

dice_chosen = input("What dice are you rolling (D[number])? ").strip().lower()

if "d" not in dice_chosen:
    raise ValueError("Invalid input. Please use D to indicate the dice type.")
parts = dice_chosen.split("d")
