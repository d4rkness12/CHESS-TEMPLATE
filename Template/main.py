from pathlib import Path
from ValidMoves import *

import pyray as ray

board_state = [
    "r", "n", "b", "q", "k", "b", "n", "r",
    "p", "p", "p", "p", "p", "p", "p", "p",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    "P", "P", "P", "P", "P", "P", "P", "P",
    "R", "N", "B", "Q", "K", "B", "N", "R"
]

board_state1 = [
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", "R", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
]

board_state2 = [
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", "N", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
]

board_state3 = [
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", "B", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
]

board_state4 = [
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", "Q", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
]

board_state5 = [
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", "K", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", ".", ".",
]

black_pieces = [
    "rook_black.png",
    "knight_black.png",
    "bishop_black.png",
    "queen_black.png",
    "king_black.png",
    "pawn_black.png"
]

white_pieces = [
    "rook_white.png",
    "knight_white.png",
    "bishop_white.png",
    "queen_white.png",
    "king_white.png",
    "pawn_white.png"
]

square_size = 90
Trans = (255, 255, 255, 255)

def get_color(board, position):
    row, col = position
    piece = board[row * 8 + col]

    if piece == ".":
        return None

    if piece.isupper():
        return "white"

    return "black"

def draw_piece(texture, row, col):
    scale = 1
    piece_size = int(texture.width * scale)

    x = col * square_size + (square_size - piece_size) // 2
    y = row * square_size + (square_size - piece_size) // 2

    position = ray.Vector2(x, y)

    ray.draw_texture_ex(texture, position, 0, scale, Trans)

def iterate_pieces(black_textures, white_textures):

    for i in range(64):
        if board_state[i] != ".":
            piece = board_state[i]

            row = i // 8
            col = i % 8

            if piece.lower() == piece:
                if piece == "r":
                    draw_piece(black_textures[0], row, col)
                elif piece == "n":
                    draw_piece(black_textures[1], row, col)
                elif piece == "b":
                    draw_piece(black_textures[2], row, col)
                elif piece == "q":
                    draw_piece(black_textures[3], row, col)
                elif piece == "k":
                    draw_piece(black_textures[4], row, col)
                else:
                    draw_piece(black_textures[5], row, col)                   
            else:
                if piece == "R":
                    draw_piece(white_textures[0], row, col)
                elif piece == "N":
                    draw_piece(white_textures[1], row, col)
                elif piece == "B":
                    draw_piece(white_textures[2], row, col)
                elif piece == "Q":
                    draw_piece(white_textures[3], row, col)
                elif piece == "K":
                    draw_piece(white_textures[4], row, col)
                else:
                    draw_piece(white_textures[5], row, col)   


def get_piece(board, position):
    pieces = {
        "p": "pawn",
        "r": "rook",
        "n": "knight",
        "b": "bishop",
        "q": "queen",
        "k": "king"
    }

    x,y = position

    position = x * 8 + y

    return pieces.get(board[position].lower())

def get_valid_moves(board, position):
    piece = get_piece(board, position)
    color = get_color(board, position)
    moves = []

    for row in range(8):
        for col in range(8):
            end = (row, col)

            if end == position:
                continue

            destination_color = get_color(board, end)

            if destination_color == color:
                continue

            if piece == "knight":
                if ValidMoves.knight_valid_moves(board, position, end):
                    moves.append(end)

            elif piece == "rook":
                if ValidMoves.rook_valid_moves(board, position, end):
                    moves.append(end)

            elif piece == "bishop":
                if ValidMoves.bishop_valid_moves(board, position, end):
                    moves.append(end)

            elif piece == "queen":
                if ValidMoves.queen_valid_moves(board, position, end):
                    moves.append(end)

            elif piece == "king":
                if ValidMoves.king_valid_moves(board, position, end):
                    moves.append(end)

            elif piece == "pawn":
                if ValidMoves.pawn_valid_moves(board, position, end, color):
                    moves.append(end)

    return moves

def main():

    ray.init_window(720, 720, "Chess")

    pieces_path = Path(__file__).parent / "Pieces"

    black_textures = [
        ray.load_texture(str(pieces_path / piece))
        for piece in black_pieces
    ]

    white_textures = [
        ray.load_texture(str(pieces_path / piece))
        for piece in white_pieces
    ]

    selected_position = None
    moves = []
    turn = "white"

    while not ray.window_should_close():

        if ray.is_mouse_button_pressed(ray.MOUSE_BUTTON_LEFT):
            mouse_x = ray.get_mouse_x()
            mouse_y = ray.get_mouse_y()

            col = mouse_x // square_size
            row = mouse_y // square_size

            position = (row, col)

            if selected_position is None:
                piece_color = get_color(board_state, position)

                if piece_color == turn:
                    selected_position = position
                    moves = get_valid_moves(board_state, position)

            # Moving a selected piece
            elif position in moves:
                selected_index = selected_position[0] * 8 + selected_position[1]
                destination_index = position[0] * 8 + position[1]

                board_state[destination_index] = board_state[selected_index]
                board_state[selected_index] = "."

                selected_position = None
                moves = []

                # Switch turns
                if turn == "white":
                    turn = "black"
                else:
                    turn = "white"

            # Clicked somewhere that isn't a valid move
            else:
                selected_position = None
                moves = []

        ray.begin_drawing()
        ray.clear_background(ray.WHITE)

        for row in range(8):
            for col in range(8):

                color = ray.DARKGRAY

                x = col * square_size
                y = row * square_size

                if (row + col) % 2 == 0:
                    color = ray.LIGHTGRAY
                    
                ray.draw_rectangle(x, y, square_size, square_size, color)

        iterate_pieces(black_textures, white_textures)

        for row, col in moves:

            x = col * square_size
            y = row * square_size

            ray.draw_rectangle(x, y, square_size, square_size, ray.YELLOW)

        ray.end_drawing()

    ray.close_window()

if __name__ == "__main__":
    main()



        