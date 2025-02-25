#Created by Kai Reinhold (kaireinhold on GitHub)

#SCRAPPED

import random
import time
import DnD_function_library

dict_Name = {}
def new_Character():
    name = input("What would you like to call this character? ").strip()
    dict_Name = name.replace(" ", "_")
    print("Opening " + dict_Name + "...")
    dict_Name = {
        "Name": name,
        "Class": input("What is their class? ").strip(),
        "Race": input("What is their race? ").strip(),
        "Level": input("What is their level? ").strip(),
        }
    print(dict_Name)
    return dict_Name
def edit_Character():
    edit_Q = input("What character would you like to edit? (replace spaces with _) ").lower().strip()
    print(dict_Name == edit_Q)
    edit_Item = input("""What would you like to edit?
 (N)ame
 (C)lass
 (R)ace
 (L)evel
 (E)xit
 """).lower().strip()

