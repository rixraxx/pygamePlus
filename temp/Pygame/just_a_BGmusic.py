import pygame

# Game constants
WIDTH, HEIGHT = 640, 480
TITLE = 'Some caption'
FPS = 60
BG_COLOR = 'white'

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        pygame.mixer.music.load('BG_music/Journey Across the Blue.ogg')
        pygame.mixer.music.play(-1)

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.screen.fill(BG_COLOR)
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()