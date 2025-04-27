from flask import Flask, request, jsonify
import time
from flask_cors import CORS
from tictactoe import best_move, check_winner  

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  

@app.route("/move", methods=["POST"])
def move():
    """Endpoint to get AI's best move."""
    data = request.json
    board = data['board']
    use_alpha_beta = data['use_alpha_beta']
    
    start_time = time.time()
    index = best_move(board, use_alpha_beta)  
    elapsed_time = time.time() - start_time
    
    return jsonify({
        "index": index,
        "time_taken": elapsed_time
    })

@app.route("/check", methods=["POST"])
def check():
    """Endpoint to check for a winner."""
    data = request.json
    board = data['board']
    winner = check_winner(board)  
    return jsonify({
        "winner": winner
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000) 
