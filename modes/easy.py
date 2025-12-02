import tkinter as tk
from tkinter import messagebox
import random

# Easy mode player vs Simple ai which only picks random spaces 



def start_easy(parent):
    """Launch Easy Mode: AI makes random moves."""
    parent.withdraw()

    window = tk.Toplevel()
    window.title("Tic Tac Toe - Easy Mode")
    
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    moves = []
    buttons = []

    def check():
        '''Checks if a win condition has been met'''
        combos = [
            (board[0][0], board[0][1], board[0][2]),
            (board[1][0], board[1][1], board[1][2]),
            (board[2][0], board[2][1], board[2][2]),
            (board[0][0], board[1][0], board[2][0]),
            (board[0][1], board[1][1], board[2][1]),
            (board[0][2], board[1][2], board[2][2]),
            (board[0][0], board[1][1], board[2][2]),
            (board[0][2], board[1][1], board[2][0])
        ]
        for a, b, c in combos:
            if a == b == c and a != " ":
                return a
        return None

    def is_full():
        '''checks if the board is full'''
        for row in board:
            for col in row:
                if col == " ":
                    return False
        return True

    def ai():
        '''Defines how spots are chosen at random'''
        empty_spots = []
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    empty_spots.append((r, c))
        return random.choice(empty_spots)

    def click(r, c):
        if board[r][c] != " ":
            return

        # Player move
        board[r][c] = "X"
        moves.append(("X", r, c))
        buttons[r][c]["text"] = "X"

        result = check()
        if result:
            messagebox.showinfo("Game Over", "You win!")
            window.destroy()
            parent.deiconify()
            return

        if is_full():
            messagebox.showinfo("Game Over", "Draw!")
            window.destroy()
            parent.deiconify()
            return

        # AI move
        ai_pos = ai()
        if ai_pos is not None:
            a_r, a_c = ai_pos
            board[a_r][a_c] = "O"
            moves.append(("O", a_r, a_c))
            buttons[a_r][a_c]["text"] = "O"

        result = check()
        if result:
            messagebox.showinfo("Game Over", "AI wins!")
            window.destroy()
            parent.deiconify()
            return

    # Create 3x3 grid buttons
    for r in range(3):
        row_buttons = []
        for c in range(3):
            btn = tk.Button(window, text=" ", font=("Arial", 24), width=3, height=1,
                            command=lambda r=r, c=c: click(r, c))
            btn.grid(row=r, column=c)
            row_buttons.append(btn)
        buttons.append(row_buttons)
