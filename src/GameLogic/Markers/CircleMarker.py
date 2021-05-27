import pygame
from .Marker import Marker

class CircleMarker (Marker):

    def __init__(self, player, color, width=15):
        super().__init__(player, color, width)
        self.radius = 85

    def draw(self, screen, square):
        try:
            pygame.draw.circle(screen, self.color, square.center, self.radius, self.width)
        except Exception as e:
            print(e)