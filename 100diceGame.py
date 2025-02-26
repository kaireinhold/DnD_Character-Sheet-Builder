#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import sys
import math
import DnD_function_library
from DnD_function_library import Dnd

dice = Dnd()

play = False

while True:
    dice.rolls = []
    start = input("Start? (y/n) ").lower().strip()
    if start == "y":
        version = input("""Which version do you want to play?
(1) Roll until 1 is rolled
(2) Roll until 1 or a duplicate is rolled
""")
        dice_to_roll = input("What type of dice would you like to roll for this game? (ex: d100, d20, d6) ")
        if version == "2":
            duplicates = input("How many duplicates do you want to allow? ")
        player_1 = int(input("How many rolls do you think there will be, Player 1? "))
        player_2 = int(input("How many rolls do you think there will be, Player 2? "))
        play = True
    else:
        play = False
        sys.exit()
    
    while play == True:
            dice.roll_no_output(dice_to_roll)
            if version == "1":
                if dice.rolls[-1] == 1:
                    if player_1 == len(dice.rolls) and player_2 == len(dice.rolls):
                        print(f"Congratulations! You both guessed the number correctly! The answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif player_1 == len(dice.rolls):
                        print(f"Congratulations, Player 1! You guessed the number correctly! The answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif player_2 == len(dice.rolls):
                        print(f"Congratulations, Player 2! You guessed the number correctly! The answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif math.isclose(player_1, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_2, len(dice.rolls), abs_tol = 10) == False:
                        print(f"Congratulations, Player 1! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif math.isclose(player_2, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_1, len(dice.rolls), abs_tol = 10) == False:
                        print(f"Congratulations, Player 2! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif math.isclose(player_1, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_2, len(dice.rolls), abs_tol = 10) == True:
                        print(f"Congratulations! You were both within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    else:
                        if abs(player_1 - len(dice.rolls)) < abs(player_2 - len(dice.rolls)):
                            print(f"Congratulations, Player 1! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif abs(player_2 - len(dice.rolls)) < abs(player_1 - len(dice.rolls)):
                            print(f"Congratulations, Player 2! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif abs(player_1 - len(dice.rolls)) == abs(player_2 - len(dice.rolls)):
                            print(f"Congratulations! You were both the same amount away from the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                    break
            elif version == "2":
                if dice.rolls[-1] == 1:
                    if player_1 == len(dice.rolls) and player_2 == len(dice.rolls):
                        print(f"Congratulations! You both guessed the number correctly! The answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif player_1 == len(dice.rolls):
                        print(f"Congratulations, Player 1! You guessed the number correctly! The answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif player_2 == len(dice.rolls):
                        print(f"Congratulations, Player 2! You guessed the number correctly! The answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif math.isclose(player_1, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_2, len(dice.rolls), abs_tol = 10) == False:
                        print(f"Congratulations, Player 1! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif math.isclose(player_2, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_1, len(dice.rolls), abs_tol = 10) == False:
                        print(f"Congratulations, Player 2! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    elif math.isclose(player_1, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_2, len(dice.rolls), abs_tol = 10) == True:
                        print(f"Congratulations! You were both within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                        print(dice.rolls)
                    else:
                        if abs(player_1 - len(dice.rolls)) < abs(player_2 - len(dice.rolls)):
                            print(f"Congratulations, Player 1! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif abs(player_2 - len(dice.rolls)) < abs(player_1 - len(dice.rolls)):
                            print(f"Congratulations, Player 2! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif abs(player_1 - len(dice.rolls)) == abs(player_2 - len(dice.rolls)):
                            print(f"Congratulations! You were both the same amount away from the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                    break
                elif dice.rolls[-1] in dice.rolls[0:-1]:
                    if dice.rolls.count(dice.rolls[-1]) >= int(duplicates):
                        if player_1 == len(dice.rolls) and player_2 == len(dice.rolls):
                            print(f"Congratulations! You both guessed the number correctly! The answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif player_1 == len(dice.rolls):
                            print(f"Congratulations, Player 1! You guessed the number correctly! The answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif player_2 == len(dice.rolls):
                            print(f"Congratulations, Player 2! You guessed the number correctly! The answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif math.isclose(player_1, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_2, len(dice.rolls), abs_tol = 10) == False:
                            print(f"Congratulations, Player 1! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif math.isclose(player_2, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_1, len(dice.rolls), abs_tol = 10) == False:
                            print(f"Congratulations, Player 2! You were within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        elif math.isclose(player_1, len(dice.rolls), abs_tol = 10) == True and math.isclose(player_2, len(dice.rolls), abs_tol = 10) == True:
                            print(f"Congratulations! You were both within 10 of the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                            print(dice.rolls)
                        else:
                            if abs(player_1 - len(dice.rolls)) < abs(player_2 - len(dice.rolls)):
                                print(f"Congratulations, Player 1! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                                print(dice.rolls)
                            elif abs(player_1 - len(dice.rolls)) < abs(player_1 - len(dice.rolls)):
                                print(f"Congratulations, Player 2! You were closer to the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                                print(dice.rolls)
                            elif abs(player_1 - len(dice.rolls)) == abs(player_2 - len(dice.rolls)):
                                print(f"Congratulations! You were both the same amount away from the answer! Player 1 guessed {player_1}, Player 2 guessed {player_2}, and the answer was {len(dice.rolls)}!")
                                print(dice.rolls)
                    else:
                        continue
                    break
