import pygame
from random import choice

# Game constants
WIDTH, HEIGHT = 480, 480
TITLE = 'Some caption'
FPS = 30
BG_COLOR = 'grey15'
Tile = 30
col, row = WIDTH//Tile, HEIGHT//Tile

class Cell:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y
        self.walls = {'top': True,
                      'left': True,
                      'bottom': True,
                      'right': True}
        self.visited = False
    def draw(self, screen):
        if self.visited:
            pygame.draw.rect(screen, 'grey75', (self.x * Tile, self.y * Tile, Tile, Tile))
        if self.walls['top']:
            pass

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

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
    print('pygame Maze Generation using Recursive Backtrack Algorithim')
    new_game = Game()
    new_game.run()