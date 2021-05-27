
class Game:

    def __init__(self, board, players):
        self.running = False
        self.board = board
        self.players = players
        self.current_player = self.players[0]
        self.winner = None
    

    def start(self):
        self.current_player = self.players[0]
        self.running = True

    def stop(self):
        self.running = False


    def has_winner(self):
        return self.winner is not None

    def show_winner(self):
        print("Winner is : ", self.current_player.name)

    def is_draw(self):
        if self.board.is_full_of_markers() and self.winner == None:
            return True

    def draw_scenario(self):
        print("It's a draw")



    def play_turn(self, player_click_position):
        self.player_plays(player_click_position)
        self.check_winner()
    
    def player_plays(self, player_click_position):
        for row_index in range(self.board.nb_rows):
            for column_index in range(self.board.nb_columns):
                square = self.board.grid[row_index][column_index]
                if square.collidepoint(player_click_position) and square.marker == None:
                    self.current_player.place_marker_in_square(square)

    
    def check_winner(self):
        for row_index in range(self.board.nb_rows):
            for column_index in range(self.board.nb_columns):
                square = self.board.grid[row_index][column_index]
                if square.marker is not None:
                    if (column_index + 2) < self.board.nb_columns:
                        self.check_horizontal_win(row_index, column_index)
                        
                    if (row_index + 2) < self.board.nb_rows:
                        self.check_vertical_win(row_index, column_index)

                    if (row_index + 2) < self.board.nb_rows and (column_index + 2) < self.board.nb_columns:
                        self.check_diagonal_win_left_to_right(row_index, column_index)
                    
                    if (row_index + 2) < self.board.nb_rows and (column_index - 2) >= 0:
                        self.check_diagonal_win_right_to_left(row_index, column_index)

    def check_horizontal_win(self, start_square_row_index, start_square_column_index):
        three_squares = (
            self.board.grid[start_square_row_index][start_square_column_index],
            self.board.grid[start_square_row_index][start_square_column_index + 1],
            self.board.grid[start_square_row_index][start_square_column_index + 2]
        )

        if self.all_squares_belong_to_a_player(three_squares, self.current_player):
            self.winner = self.current_player
    
    def check_vertical_win(self, start_square_row_index, start_square_column_index):
        three_squares = (
            self.board.grid[start_square_row_index][start_square_column_index],
            self.board.grid[start_square_row_index + 1][start_square_column_index],
            self.board.grid[start_square_row_index + 2][start_square_column_index]
        )

        if self.all_squares_belong_to_a_player(three_squares, self.current_player):
            self.winner = self.current_player

    def check_diagonal_win_left_to_right(self, start_square_row_index, start_square_column_index):
        three_squares_left_to_right = (
            self.board.grid[start_square_row_index][start_square_column_index],
            self.board.grid[start_square_row_index + 1][start_square_column_index + 1],
            self.board.grid[start_square_row_index + 2][start_square_column_index + 2]
        )

        if self.all_squares_belong_to_a_player(three_squares_left_to_right, self.current_player):
            self.winner = self.current_player

    def check_diagonal_win_right_to_left(self, start_square_row_index, start_square_column_index):
        three_squares_right_to_left = (
            self.board.grid[start_square_row_index][start_square_column_index],
            self.board.grid[start_square_row_index + 1][start_square_column_index - 1],
            self.board.grid[start_square_row_index + 2][start_square_column_index - 2]
        )

        if self.all_squares_belong_to_a_player(three_squares_right_to_left, self.current_player):
                self.winner = self.current_player
    
    def all_squares_belong_to_a_player(self, squares, player):
        for square in squares:
            if square.marker is None or square.marker.player is not player:
                return False

        return True



    def next_player_turn(self):
        current_player_index = self.players.index(self.current_player)

        if (current_player_index == len(self.players) - 1):
            next_player_index = 0
        else:
            next_player_index = current_player_index + 1

        self.current_player = self.players[next_player_index]