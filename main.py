import chess
from minimax_ab import *
from AIchess import *
from negamax import NegamaxEngine
from negamaxab import NegamaxAbEngine
from mtdf import MTDfEngine
from negascout import NegaScoutEngine

import mcts
def main():
    board = chess.Board()

    player1 = AIChess() #minimaxab
    player1.board = board
    player1.minimaxDepth = 3

    # player2 = NegamaxAbEngine(board, 3)

    # player2 = NegaScoutEngine(board, 3)

    player2 = MTDfEngine(board, 4)

    # player1 = NegamaxAbEngine(board, 3)
    #
    while not board.is_game_over():
        print(board)

        move1 = player1.chessAIMove()[0]
        if (move1 == "claim_draw"):
            break
        player1.makeChessMove(move1)
        print(move1)
        print(f"Player 1 moves: {move1}")

        print(board)

        if (board.is_game_over()): break
        print(board.is_game_over())
        move2 = player2.search_controller()
        print(move2)
        board.push(move2)
        print(f"Player 2 moves: {move2}")


    if(board.is_game_over() ):
        if str(board.result()) == '0-1':
            print("player2 win")
        elif str(board.result()) == '1-0':
            print("player1 win")
        else:
            print('Draw!')

if __name__ == "__main__":
    main()

