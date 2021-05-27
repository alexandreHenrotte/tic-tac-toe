from GameLogic import GameColors
from GameLogic.Square import Square

class Board:

    def __init__(self):
        self.screen = None
        self.nb_rows = 3
        self.nb_columns = 3
        self.square_size = 200
        self.grid = self._make_grid(self.nb_rows, self.nb_columns, self.square_size)
    

    def _make_grid(self, nb_rows, nb_columns, square_size):
        grid = []

        for row_index in range(nb_rows):
            row = []
            for column_index in range(nb_columns):
                square_x_pos = column_index * square_size
                square_y_pos = row_index * square_size
                square = Square(square_x_pos, square_y_pos, square_size, square_size) # Square(pos_x, pos_y, width, height)
                row.append(square)
            grid.append(row)
            
        return grid
    
    def draw_board_and_markers(self, players):
        self.screen.fill(GameColors.WHITE)
        self._draw_markers(players)
        self._draw_board()

    def _draw_board(self):
        for row in self.grid:
            for square in row:
                square.draw(self.screen)

    def _draw_markers(self, players):
        for player in players:
            for square in player.squares:
                square.marker.draw(self.screen, square)
    

    def is_full_of_markers(self):
        for row in self.grid:
            for square in row:
                if square.marker is None:
                    return False
        
        return True

    def get_size(self):
        height = self.nb_rows * self.square_size
        width = self.nb_columns * self.square_size

        return (height, width)

    def assign_screen(self, screen):
        self.screen = screen