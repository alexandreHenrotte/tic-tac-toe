from abc import ABC, abstractmethod


class Marker (ABC):

    def __init__(self, player, color, width):
        self.player = player
        self.color = color
        self.width = width


    @abstractmethod
    def draw(self, screen, square):
        pass