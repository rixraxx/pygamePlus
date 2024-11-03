import pygame
from math import ceil

# Game constants
WIDTH, HEIGHT = 640, 324
TITLE = 'Some caption'
FPS = 30
BG_COLOR = 'white'

class Scrolling_Backgeround:
    def __init__(self, image_path: str, screen: pygame.Surface, scrollSpeed: float = 7.5) -> None:
        self.image = pygame.image.load(image_path).convert()
        self.img_width = self.image.get_width()
        self.screen = screen
        self.screenWidth = self.screen.get_width()
        self.scroll_speed = scrollSpeed
        self.scroll:float = 0
        self.tiles = ceil(self.screenWidth / self.img_width ) + 1
    def draw(self):
        for i in range(self.tiles): self.screen.blit(self.image, (i * self.img_width + self.scroll, 0))
    def update(self):
        self.scroll -= self.scroll_speed
        if abs(self.scroll) > self.img_width: self.scroll = 0
        self.draw()
            
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        self.background_image = Scrolling_Backgeround('Done/Pygame/just_a_srollingBG/1.png', self.screen)

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.background_image.update()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()