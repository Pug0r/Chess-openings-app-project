import chess
import json

board = chess.Board()
move_number = 0

queens_gambit = {0: ('d2d4'), 1: ('d7d5'), 2: ('c2c4'), 3: ('d5c4')}


def is_valid_move(start_square, end_square):
    """ Validates the move that player wants to make AND proceeds with it (but only in the engine's board), if valid """
    global move_number
    start_square = chess.parse_square(start_square)
    end_square = chess.parse_square(end_square)
    move = chess.Move(start_square, end_square)
    print(board)
    if move in board.legal_moves:
        board.push(move)
        move_number += 1
        print(board)
        return True
    return False


def is_correct_move(opening, start_square, end_square):
    start_square = chess.parse_square(start_square)
    end_square = chess.parse_square(end_square)
    move = str(chess.Move(start_square, end_square))
    if move in opening[move_number]:
        print("Correct move!")
        return True
    else:
        print("Nope.")
        return False


is_correct_move(queens_gambit, 'd2', 'd4')


