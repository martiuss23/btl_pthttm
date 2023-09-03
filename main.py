import chess
from negamax import NegamaxEngine
from negamaxab import NegamaxAbEngine
from mtdf import MTDfEngine
from negascout import NegaScoutEngine



def main():
    board = chess.Board()
    # player2 = NegamaxEngine(board, 3) #white
    player1 = NegamaxAbEngine(board, 3) #black
    # player1 = NegaScoutEngine(board, 3)
    player2 = MTDfEngine(board, 3)
    while not board.is_game_over():
        print(board)
        move1 = player1.search_controller()
        print(move1)
        board.push(move1)
        print(f"Player 1 moves: {move1}")

        print(board)
        if(board.is_game_over()) : break
        move2 = player2.search_controller()
        board.push(move2)
        print(f"Player 2 moves: {move2}")

    if(board.is_game_over()):
        if str(board.result()) == '0-1':
            print("player2 win")
        elif str(board.result()) == '1-0':
            print("player1 win")
        else:
            print('Draw!')

if __name__ == "__main__":
    main()

