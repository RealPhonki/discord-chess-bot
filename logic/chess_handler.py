from PIL import Image, ImageDraw
from functools import cached_property
import chess
import chess.svg

class ChessHandler():
    def __init__(self) -> None:
        self.board = chess.Board
        self.square_size = 100
        self.board_size = self.square_size * 8
        self.board_color = [(238,238,210), (118,150,86)]

    # the cached property decorator means that it once it generates the return value it caches
    # it and sends it the next time the property is called
    @cached_property
    def checker_board(self) -> Image:
        # Returns the raw .png data of the board without pieces
        image = Image.new("RGB", (self.board_size, self.board_size), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        for row in range(8):
            for col in range(8):
                x1, y1 = col * self.square_size, row * self.square_size
                x2, y2 = x1 + self.square_size, y1 + self.square_size
                color = self.board_color[0] if (row + col) % 2 == 0 else self.board_color[1]
                draw.rectangle([x1, y1, x2, y2], fill = color)
        
        return image

    def get_board_png(self) -> Image:
        # Returns the raw .png data of the board
        image = self.checker_board
        for rank, row in enumerate(str(self.board).splitlines()):
            for col, tile in enumerate(row.split(' ')):
                if tile == ".": continue

                # self.draw_piece()
        pass

# svg processing pseudo code
# 
# @cached_property
# create_checkerboard():
#   loop through and create checkerboard for each tile
#   return generated image
#
# def generate_img
#   create_checkerboard()
#   go through pgn and add a piece for every position
#   return img