from Menu.MainMenu import MainMenu
import pygame


class Application:

    def __init__(self):
        self.WINDOW_TITLE = "Tic Tac Toe"
        self.MAX_FPS = 60
        self.screen =  pygame.display.set_mode((900, 600))
        self.clock = pygame.time.Clock()
        self.running = False
        
    def run(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(self.WINDOW_TITLE)

        self.running = True
        while self.running:
            MainMenu(self).mainloop(self.screen)

            # Update screen
            pygame.display.update()

            # Limit max FPS ingame
            self.clock.tick(self.MAX_FPS)

        pygame.quit()


    def stop(self):
        self.running = False



if __name__ == "__main__":
    app = Application()
    app.run()