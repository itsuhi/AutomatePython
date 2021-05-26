"""
Write a function named isValidChessBoard() that takes a dictionary argument and
returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be
on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
The piece names begin with either a 'w' or 'b' to represent white or black, followed by
'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
This function should detect when a bug has resulted in an improper chess board.
"""


def isValidChessboard(chessboard):
    """

    :param chessboard: a dictionary of the form {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
                                                 '5h': 'bqueen', '3e': 'wking'}
    :return: boolean; whether chessboard is a valid or not
    """

    proper_chessboard = [digit + alpha for digit in "12345678" for alpha in "abcdefgh"]
    pos = chessboard.keys()
    pieces = chessboard.values()
    chess = {"king": 1, "queen": 1, "bishop": 2, "knight": 2, "rook": 2, "pawn": 8}
    white = {}
    black = {}

    # Dictionary does not allow duplicate keys
    # if len(set(pos)) != len(pos):
    #     print("duplicate position found")
    #     return False

    if not set(pos).issubset(set(proper_chessboard)):
        print("Invalid Chessboard")
        return False

    for piece in pieces:
        if piece.startswith("w"):
            if piece[1:] in white:
                white[piece[1:]] += 1
            else:
                white[piece[1:]] = 1
        else:
            if piece[1:] in black:
                black[piece[1:]] += 1
            else:
                black[piece[1:]] = 1

    if (sum(white.values()) > 16) or (sum(black.values()) > 16):
        return False

    for key, value in white.items():
        if value > chess[key]:
            return False

    for key, value in black.items():
        if value > chess[key]:
            return False

    return True


test = {'6h': 'bking', '6c': 'bqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessboard(test))

#=======================================================================================================================

