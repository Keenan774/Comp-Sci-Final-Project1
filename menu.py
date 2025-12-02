import tkinter as tk
from tkinter import messagebox

#imports the different modes, by each game running each as a function, and that function is being imported 
#into the menu
from modes.pvp import start_pvp
from modes.easy import start_easy
from modes.medium import start_medium
from modes.hard import start_hard

# main_menu() builds a simple window with buttons, which are linked to the imported function, and when pressed run 
#the other modes with the main menu as a parent, closing the main menu window, and reopening it when 
#the other windows close


def main_menu():
    """opens main menu window."""
    root = tk.Tk()
    root.title("Tic Tac Toe - Main Menu")

    tk.Label(root, text="Tic Tac Toe", font=("Arial", 24)).pack(pady=20)

    tk.Button(root, text="Player vs Player", width=25, height=2,
              command=lambda: start_pvp(root)).pack(pady=5)

    tk.Button(root, text="Easy Difficulty", width=25, height=2,
              command=lambda: start_easy(root)).pack(pady=5)

    tk.Button(root, text="Medium Difficulty", width=25, height=2,
              command=lambda: start_medium(root)).pack(pady=5)

    tk.Button(root, text="Hard Difficulty", width=25, height=2,
              command=lambda: start_hard(root)).pack(pady=5)

    tk.Button(root, text="Quit", width=25, height=2,
              command=root.quit).pack(pady=20)
    

    root.mainloop()


if __name__ == "__main__":
    main_menu()