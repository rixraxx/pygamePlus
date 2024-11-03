import pygame
from math import floor

# Game constants
WIDTH, HEIGHT = 480, 480
TITLE = 'Some caption'
FPS = 30
BG_COLOR = 'grey15'

class SpriteSheet():
    class Character:
        def __init__(self, images: list[pygame.Surface], xpos: float|int, ypos: float | int) -> None:
            self.image: list[pygame.Surface] = images
            self.current_sprite = 0.0
            self.rect = self.image[0].get_rect(center = (xpos, ypos))
        def draw(self, screen: pygame.Surface):
            self.current_sprite += 0.2
            if self.current_sprite > len(self.image): self.current_sprite = 0
            screen.blit(self.image[floor(self.current_sprite)], self.rect)
    
    def __init__(self, image: pygame.Surface, width: int|float, height: int | float, scale: float | int = 1) -> None:
        self.sheet = image
        self.dimension: tuple[int| float, int|float] = (width, height)
        self.factor = scale
        
        row = self.sheet.get_width() // width
        self.img_list = [] 
        for i in range(int(row)):
            surface = pygame.Surface(self.dimension, pygame.SRCALPHA)
            surface.blit(self.sheet, (0,0), ((i * self.dimension[0], 0), self.dimension))
            self.img_list.append(pygame.transform.scale_by(surface, self.factor))
        
        self.player = self.Character(self.img_list, 240, 240)
    
    def draw(self, screen):
        self.player.draw(screen)

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        self.player_spritesheet = pygame.image.load('Done/Pygame/just_a_spriteSheetAnim/doux.png').convert_alpha()
        self.player = SpriteSheet(self.player_spritesheet, 24, 24, 3)

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.screen.fill(BG_COLOR)

            self.player.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()