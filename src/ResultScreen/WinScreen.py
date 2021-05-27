import pygame_menu


class WinScreen (pygame_menu.Menu):

    def __init__(self, main_menu, winner):
        super().__init__("Tic Tac Toe", 900, 600, theme=pygame_menu.themes.THEME_BLUE)
        self.add.label("Winner is \"" + winner.name + "\"")
        self.add.button('Back to main menu', self.go_back_to_main_menu)
        self.main_menu = main_menu

    def go_back_to_main_menu(self):
       self.main_menu.mainloop(self.main_menu.application.screen)