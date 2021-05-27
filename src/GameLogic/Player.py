
class Player:

    def __init__(self, name):
        self.name = name
        self.marker = None
        self.squares = []

    def place_marker_in_square(self, square):
        square.place_marker(self.marker)
        self.squares.append(square)
        
    def assign_marker(self, marker):
        self.marker = marker