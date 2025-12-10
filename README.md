Python Tic Tac Toe GUI

    A simple but complete Tkinter-based Tic Tac Toe game featuring multiple difficulty levels, a clean interface, and intuitive gameplay. Designed for beginner to intermediate Python users looking to explore GUI programming and basic game AI.

Features
    Player vs Player
        Two players alternate turns on a standard 3×3 grid.

    Easy Mode

        Computer chooses moves completely at random.

    Medium Mode

        The AI mixes random choice with minimax AI.

    Hard Mode (Unbeatable)

        Implements the Minimax algorithm to evaluate all possible outcomes, making optimal decisions every turn. This mode demonstrates recursion, decision trees, and algorithmic game logic.

Tkinter GUI

    Graphical interface built using Tkinter with clear buttons and layout. All modes launch from a main menu window.

    Multi-Window Navigation

    Includes separate scripts for:

        Main Menu

        Player vs Player

        Easy Mode

        Medium Mode

        Hard Mode

        Each mode opens in its own window while the main menu is hidden and restored appropriately.

Project Structure:

project/
│
├── main.py                     # Main menu GUI
├── modes/
│   ├── pvp.py                  # Player vs Player logic and UI
│   ├── easy.py                 # Easy AI logic
│   ├── medium.py               # Medium AI logic
│   ├── hard.py                 # Hard AI (Minimax algorithm)
│   └── history_functions.py    # Optional history system (unused if removed)
│
└── README.md

How to Run
    Requirements

        Python 3.8 or newer

        Tkinter (included with most Python installations)

Launching the Game

        python main.py


        The main menu window will appear, allowing you to select your desired game mode.

Minimax (Hard Mode Algorithm Overview)

    The Hard Mode AI uses the Minimax algorithm to ensure optimal play. It works by:

    Simulating every possible move.

    Evaluating board states recursively.

    Maximizing the computer's advantage.

    Minimizing the player's advantage.

    This guarantees that the AI cannot be defeated if played correctly.

Future Development Ideas:

    Implement game history and replay features

    Add sound or visual effects

    Create score tracking between rounds

    Improve interface with graphics or themed styling

    Animate winning lines
    
