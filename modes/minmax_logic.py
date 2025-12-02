import math


def check_winner(board):
    """Returns 'X', 'O', 'draw', or None based on the board."""
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "draw"

    return None


def score(board, depth):
    """Scoring system based on the article.
    AI = O  +10
    Player = X  -10
    Depth adjustment makes longer losses worse."""
    result = check_winner(board)

    if result == "O":
        return 10 - depth
    elif result == "X":
        return depth - 10
    else:
        return 0


def minmax(board, depth, is_maximizing):
    """Depth-aware recursive minimax (simple and beginner-friendly)."""
    result = check_winner(board)
    if result is not None:
        return score(board, depth)

    best_score = -math.inf if is_maximizing else math.inf

    for i in range(9):
        if board[i] == " ":

            # Simulate move
            board[i] = "O" if is_maximizing else "X"

            new_score = minmax(board, depth + 1, not is_maximizing)

            # Undo
            board[i] = " "

            if is_maximizing:
                if new_score > best_score:
                    best_score = new_score
            else:
                if new_score < best_score:
                    best_score = new_score

    return best_score


def best_move(board):
    """Finds the optimal move for AI (O)."""
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score_value = minmax(board, 0, False)
            board[i] = " "

            if score_value > best_score:
                best_score = score_value
                move = i

    return move  # index 08
