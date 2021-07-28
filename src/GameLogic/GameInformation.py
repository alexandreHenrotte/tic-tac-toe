import pygame
from GameLogic import GameColors
from GameLogic.Player import Player

class GameInformation:

    def __init__(self):
        self.screen = None
        self.x_start = 625
        self.x_end = 875
        self.y_start = 25
        self.y_end = 575
        self.font = pygame.font.SysFont("comicsansbold", 30)
        self.lines = []
    
    def draw(self):
        for line in self.lines:
            label_line = self.font.render(line["text"], 1, line["color"])
            self.screen.blit(label_line, line["position"])
        
    def set_font(self, fontname="comicsansbold", fontsize=30):
        self.font = pygame.font.SysFont(fontname, fontsize)
    
    def set_lines(self, lines):
        self.lines = lines

    def append_line(self, line):
        self.lines.append(line)

    def assign_screen(self, screen):
        self.screen = screen
    