import pygame
import pygame_menu
import time
from GameLogic.Game import Game
from GameLogic.Board import Board
from GameLogic.GameInformation import GameInformation
from GameLogic.Player import Player
from GameLogic.Markers.CrossMarker import CrossMarker
from  GameLogic.Markers.CircleMarker import CircleMarker
from GameLogic import GameColors


class MainMenu (pygame_menu.Menu):

    def __init__(self, application):
        super().__init__("Tic Tac Toe", 900, 600, theme=pygame_menu.themes.THEME_BLUE)
        self.application = application
        self.add.button('Play', self.start_game)
        self.add.button('Quit', pygame_menu.events.EXIT)


    def start_game(self):
        board = Board()
        game_information = GameInformation()

        board.assign_screen(self.application.screen)
        game_information.assign_screen(self.application.screen)

        player1 = Player("Player 1")
        player2 = Player("Player 2")
        players = [player1, player2]

        cross = CrossMarker(player1, GameColors.RED)
        circle = CircleMarker(player2, GameColors.BLUE)

        player1.assign_marker(cross)
        player2.assign_marker(circle)
        
        game_information.set_lines(
        [
            {
                "text": players[0].name,
                "color": players[0].marker.color,
                "position": (game_information.x_start, game_information.y_start)
            },
            {
                "text": players[1].name,
                "color": players[1].marker.color,
                "position": (game_information.x_start, game_information.y_start + 40)
            }
        ])

        game = Game(board, game_information, players)

    
        game.start()
        while game.running:
            # User key events
            for event in pygame.event.get():

                # Close window button
                if event.type == pygame.QUIT:
                    game.stop()

                # On keyboard
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game.stop()

                # On mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left mouse button
                        game.play_turn(event.pos)     

                        if game.has_winner():
                            game.show_winner()

                        elif game.is_draw():
                            game.draw_scenario()

                        else:
                            game.next_player_turn()

            # Draw board and players markers
            game.board.draw_board_and_markers(game.players)

            # Draw game information
            game.game_information.draw()

            # Update screen
            pygame.display.update()

            if game.has_winner() or game.is_draw():
                time.sleep(3)
                game.stop()