import customtkinter as ctk
import os
from DnD_function_library import Dnd
# from DnD_Character_Sheet_Builder import Build_Character_Sheet

# build = Build_Character_Sheet()
dnd = Dnd()

# Create the main window
root = ctk.CTk()

# Set the window title
root.title("CustomTkinter GUI")

# Set the window size
root.geometry("400x300")

# Create a label widget
label = ctk.CTkLabel(root, text="Hello, World!", font=("Arial", 20))
label.pack(pady=20)

# Function to update the label text
def update_label():
    label.configure(text="Button Clicked!")

# Create a button widget
button = ctk.CTkButton(root, text="Click Me", command=update_label)
button.pack(pady=20)

# Run the application
root.mainloop()
