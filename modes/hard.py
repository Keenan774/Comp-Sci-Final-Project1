import tkinter as tk
from tkinter import messagebox
from modes.minmax_logic import best_move, check_winner



def start_hard(parent):
    '''Starts Hard Difficulty'''
    parent.withdraw()
    window = tk.Toplevel()
    
    board = [[" ", " ", " "], 
             [" ", " ", " "], 
             [" ", " ", " "]]
    buttons = []
    moves = []

    def flat():
        return [board[r][c] for r in range(3) for c in range(3)]

    def check():
        return check_winner(flat())

    def is_full():
        for row in board:
            for col in row:
                if col == " ":
                    return False
        return True

    def click(r, c):
        if board[r][c] != " ":
            return

        # Player move
        board[r][c] = "X"
        moves.append(("X", r, c))
        buttons[r][c]["text"] = "X"

        result = check()
        if result == "X":
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
        index = best_move(flat())
        ai_r = index // 3
        ai_c = index % 3

        board[ai_r][ai_c] = "O"
        moves.append(("O", ai_r, ai_c))
        buttons[ai_r][ai_c]["text"] = "O"

        result = check()
        if result == "O":
            messagebox.showinfo("Game Over", "AI wins!")
            window.destroy()
            parent.deiconify()
            return

        if is_full():
            messagebox.showinfo("Game Over", "Draw!")
            window.destroy()
            parent.deiconify()
            return

    # GUI setup
    for r in range(3):
        row_buttons = []
        for c in range(3):
            btn = tk.Button(
                window,
                text=" ",
                font=("Arial", 24),
                width=3,
                height=1,
                command=lambda r=r, c=c: click(r, c)
            )
            btn.grid(row=r, column=c)
            row_buttons.append(btn)
        buttons.append(row_buttons)

