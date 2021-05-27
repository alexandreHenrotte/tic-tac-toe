import pygame
from GameLogic import GameColors

class Square (pygame.Rect):

    def __init__(self, pos_x, pos_y, width, height, border_size=8):
        super().__init__(pos_x, pos_y, width, height)
        self.color = GameColors.ORANGE
        self.border_size = border_size
        self.marker = None

    def place_marker(self, marker):
        self.marker = marker

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self, self.border_size)