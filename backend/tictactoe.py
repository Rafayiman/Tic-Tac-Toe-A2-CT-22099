# tictactoe.py

# Define players
HUMAN = 'O'
AI = 'X'
EMPTY = ''

def check_winner(board):
    """Check rows, columns, and diagonals for a winner."""
    win_states = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    
    if [AI, AI, AI] in win_states:
        return AI
    elif [HUMAN, HUMAN, HUMAN] in win_states:
        return HUMAN
    
    if EMPTY not in board:
        return "Tie"
    
    return None

def minimax(board, is_maximizing):
    """Minimax algorithm to evaluate the best move."""
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def minimax_alpha_beta(board, is_maximizing, alpha, beta):
    """Minimax algorithm with alpha-beta pruning."""
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax_alpha_beta(board, False, alpha, beta)
                board[i] = EMPTY
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax_alpha_beta(board, True, alpha, beta)
                board[i] = EMPTY
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def best_move(board, use_alpha_beta):
    """Determine the best move for AI."""
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            if use_alpha_beta:
                score = minimax_alpha_beta(board, False, -float('inf'), float('inf'))
            else:
                score = minimax(board, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move
