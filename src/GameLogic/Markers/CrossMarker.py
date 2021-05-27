import pygame
from .Marker import Marker

class CrossMarker (Marker):

    def __init__(self, player, color, width=10):
        super().__init__(player, color, width)

    def draw(self, screen, square):
        try:
            pygame.draw.line(screen, self.color, square.topleft, square.bottomright, self.width)
            pygame.draw.line(screen, self.color, square.topright, square.bottomleft, self.width)
        except Exception as e:
            print(e)