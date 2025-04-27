# Tic-Tac-Toe-A2-CT-22099
Assignment 2 CT-22099 Section B

Tic-Tac-Toe AI Assignment with Minimax and Alpha-Beta Pruning Project Overview This project implements a classic Tic-Tac-Toe game with an AI opponent. The AI is built using the Minimax algorithm, which evaluates all possible moves and selects the optimal one. To improve the performance of the Minimax algorithm, Alpha-Beta Pruning is introduced to reduce the number of nodes evaluated, making the AI faster and more efficient.

Technologies Used: Frontend: React.js

Backend: Flask (Python)

AI Logic: Minimax algorithm and Alpha-Beta Pruning

Project Structure: Frontend: React.js handles the user interface and game logic, allowing the user to interact with the Tic-Tac-Toe board.

Backend: Flask API serves the game logic and processes AI moves, using the Minimax algorithm and Alpha-Beta Pruning.

Key Features: Tic-Tac-Toe Game: Classic 3x3 grid with interactive gameplay.

AI Opponent: The AI uses the Minimax algorithm to determine optimal moves.

Alpha-Beta Pruning: Optimizes the Minimax algorithm by pruning unnecessary branches of the search tree.

Game Flow: Player can play against the AI, and the game checks for a winner after every move. The game ends when there is a winner or a tie.

Core Game Logic

Tic-Tac-Toe Board: The game board is a 3x3 grid, represented as an array of 9 elements. Each element in the array holds a string value, either "O", "X", or an empty string (representing the cell's state).

Player vs AI: The player always plays "O", and the AI plays "X".

The player and AI alternate turns until there is a winner or a tie.

Minimax Algorithm: The AI uses the Minimax algorithm to make optimal decisions. The algorithm works by simulating every possible move, evaluating the board after each move, and choosing the best possible move that maximizes the AI's chances of winning. The evaluation function assigns scores to board states (win = +10, loss = -10, tie = 0), and the AI selects the move that results in the highest score.

Alpha-Beta Pruning: Alpha-Beta Pruning is an optimization technique for the Minimax algorithm. It eliminates the need to evaluate parts of the search tree that do not need to be explored because they cannot affect the final decision. This significantly reduces the time complexity of the Minimax algorithm.
