🧩 Python Tic Tac Toe GUI

A simple yet complete Tkinter-based Tic Tac Toe game featuring multiple difficulty levels, clean UI, and intuitive gameplay.

🎮 Features
✔ Player vs Player

Two people can play on the same computer, taking turns on a 3×3 board.

✔ Easy Mode

AI selects completely random moves. A great mode for beginners.

✔ Medium Mode

AI uses a mix of random choice and simple strategy (optional depending on your build).

✔ Hard Mode (Unbeatable)

AI uses the classic Minimax algorithm, making it impossible to beat.
Perfect mode to demonstrate algorithmic strategy and recursion.

✔ Tkinter GUI

Simple and beginner-friendly interface, using clean buttons and multiple windows.

✔ Multi-Window Navigation

Main Menu

PvP Mode

Easy Mode

Medium Mode

Hard Mode

All windows cleanly hide and restore the menu as needed.

📁 Project Structure
project/
│
├── main.py               # Main menu GUI
├── modes/
│   ├── pvp.py            # Player vs Player mode
│   ├── easy.py           # Easy AI mode
│   ├── medium.py         # Medium AI mode
│   ├── hard.py           # Hard Minimax AI mode
│   └── history_functions.py  # (unused if you removed history features)
│
└── README.md

▶️ How to Run
Requirements

Python 3.8+

Tkinter (included with most Python installations)

Run the game
python main.py


The main menu will open automatically, allowing you to choose a game mode.

🧠 Minimax Overview (Hard Mode)

The unbeatable AI uses the Minimax algorithm, which:

Simulates every possible move

Evaluates each board state

Maximizes AI advantage (O)

Minimizes opponent advantage (X)

Ensures perfect play

This mode provides a great example of recursion and algorithmic decision-making.

🎨 Screenshots (Optional)

You can add images like:

![Main Menu](screenshots/menu.png)
![Gameplay](screenshots/gameplay.png)

💡 Future Improvements

Add game history + replay viewer

Add sound effects

Add score tracking

Improve UI with custom graphics

Add animations for winning lines