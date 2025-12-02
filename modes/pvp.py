import tkinter as tk
from tkinter import messagebox

# pvp mode: two players use the same window and
# alternate turns. Moves are saved as (player, row, column) so the
# history viewer can replay them.

def start_pvp(parent):
    '''Starts player vs player mode'''
    parent.withdraw()

    window = tk.Toplevel()
    window.title("Tic Tac Toe - Player vs Player")

    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    moves = []
    buttons = []
    current_player = ["X"]

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
        '''Check if the board is full'''
        for row in board:
            for col in row:
                if col == " ":
                    return False
        return True

    def click(r, c):
        '''Defines Click and its result'''
        if board[r][c] != " ":
            return

        # Current player move
        board[r][c] = current_player[0]
        moves.append((current_player[0], r, c))
        buttons[r][c]["text"] = current_player[0]

        result = check()
        if result:
            messagebox.showinfo("Game Over", f"Player {current_player[0]} wins!")
            window.destroy()
            parent.deiconify()
            return

        if is_full():
            messagebox.showinfo("Game Over", "Draw!")
            window.destroy()
            parent.deiconify()
            return

        # Switch player
        if current_player[0] == "X":
            current_player[0] = "O"
        else:
            current_player[0] = "X"

    # Create buttons
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


