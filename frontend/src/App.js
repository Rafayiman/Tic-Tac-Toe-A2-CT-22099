import React, { useState } from "react";
import Board from "./components/Board";
import "./App.css";
import axios from "axios";

// Set the base URL for the backend API
axios.defaults.baseURL = "http://localhost:5000";

function App() {
  const [board, setBoard] = useState(Array(9).fill(''));
  const [isPlayerTurn, setIsPlayerTurn] = useState(true);
  const [winner, setWinner] = useState(null);
  const [useAlphaBeta, setUseAlphaBeta] = useState(true);
  const [timeTaken, setTimeTaken] = useState(null);

  const handleClick = async (index) => {
    if (!isPlayerTurn || board[index] || winner) return;

    // Make a copy of the board and update it with the player's move
    const newBoard = [...board];
    newBoard[index] = 'O';
    setBoard(newBoard);
    setIsPlayerTurn(false);

    // Send the updated board to the backend to check for a winner
    let res = await axios.post("/check", { board: newBoard });
    if (res.data.winner) {
      setWinner(res.data.winner);  
      return;
    }

    // If no winner yet, make AI's move
    let moveRes = await axios.post("/move", {
      board: newBoard,
      use_alpha_beta: useAlphaBeta
    });

    const aiBoard = [...newBoard];
    if (moveRes.data.index !== null) {
      aiBoard[moveRes.data.index] = 'X';
    }
    setBoard(aiBoard);
    setTimeTaken(moveRes.data.time_taken);

    // Check the board again after AI's move
    res = await axios.post("/check", { board: aiBoard });
    if (res.data.winner) {
      setWinner(res.data.winner);  
    } else {
      setIsPlayerTurn(true);  
    }
  };

  const resetGame = () => {
    setBoard(Array(9).fill(''));
    setIsPlayerTurn(true);
    setWinner(null);
    setTimeTaken(null);
  };

  return (
    <div className="container">
      <h1>Tic Tac Toe AI</h1>
      <div className="toggle">
        <label>Use Alpha-Beta Pruning: </label>
        <input 
          type="checkbox"
          checked={useAlphaBeta}
          onChange={() => setUseAlphaBeta(!useAlphaBeta)}
        />
      </div>
      <Board squares={board} onClick={handleClick} />
      {winner && <div className="result">{winner === 'Tie' ? "It's a Tie!" : `Winner: ${winner}`}</div>}
      {timeTaken > 0 && <div className="time">AI move time: {timeTaken.toFixed(5)}s</div>}
      <button className="reset-btn" onClick={resetGame}>Reset Game</button>
    </div>
  );
}

export default App;
