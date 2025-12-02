import tkinter as tk
from tkinter import messagebox
import random
from modes.minmax_logic import best_move


def start_medium(parent):
    parent.withdraw()
    window = tk.Toplevel()
    window.title("Medium AI")

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    moves = []
    buttons = []

    def check_win():
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
        for row in board:
            for col in row:
                if col == " ":
                    return False
        return True

    def random_ai_move():
        empty_spots = []
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    empty_spots.append((r, c))
        return random.choice(empty_spots)

    def medium_ai():
        """50% random, 50% unbeatable minimax."""
        coin = random.random()

        if coin < 0.5:
            return random_ai_move()
        else:
            flat_board = [board[r][c] for r in range(3) for c in range(3)]
            index = best_move(flat_board)  # index 0–8
            return index // 3, index % 3

    def click(r, c):
        if board[r][c] != " ":
            return

        board[r][c] = "X"
        moves.append(("X", r, c))
        buttons[r][c]["text"] = "X"

        result = check_win()
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

        # AI TURN
        ai_r, ai_c = medium_ai()
        board[ai_r][ai_c] = "O"
        moves.append(("O", ai_r, ai_c))
        buttons[ai_r][ai_c]["text"] = "O"

        result = check_win()
        if result:
            messagebox.showinfo("Game Over", "AI wins!")
            window.destroy()
            parent.deiconify()
            return

        if is_full():
            messagebox.showinfo("Game Over", "Draw!")
            window.destroy()
            parent.deiconify()
            return
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


    
