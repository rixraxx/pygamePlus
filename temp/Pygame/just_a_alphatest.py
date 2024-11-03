import pygame
from math import floor

# Game constants
WIDTH, HEIGHT = 640, 480
TITLE = 'Some caption'
FPS = 60
BG_COLOR = 'black'
test_colr = pygame.Color(172, 204, 232)
test_colr2 = pygame.Color(172, 204, 232, 50)
test_colr3 = pygame.Color(172, 204, 232, 100)

class Character:
    def __init__(self, images: list[str], xpos: float|int, ypos: float | int, scale: float | int) -> None:
        self.image: list[pygame.Surface] = [pygame.transform.scale_by((pygame.image.load(_).convert_alpha()), scale) for _ in images]
        self.current_sprite = 0.0
        self.rect = self.image[0].get_rect(center = (xpos, ypos))
    def draw(self, screen: pygame.Surface):
        self.current_sprite += 0.2
        if self.current_sprite > len(self.image): self.current_sprite = 0
        screen.blit(self.image[floor(self.current_sprite)], self.rect)

class TestParticles:
    def __init__(self, screen, xpos, ypos) -> None:
        # self.image = pygame.Surface((100, 150))
        # self.rect = self.image.get_rect(center = (xpos, ypos))
        pygame.draw.rect(screen, test_colr, (100,150,xpos,ypos))

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        self.test_surface = pygame.Surface((150 ,150), pygame.SRCALPHA)
        self.test_surface.fill(test_colr)
        self.alpha = 255

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.screen.fill(BG_COLOR)

            pygame.draw.rect(self.screen, 'lightgreen', (250, 250, 20, 20))
            self.screen.blit(self.test_surface, (200, 200))
            self.test_surface.set_alpha(self.alpha)
            self.alpha-=5
            if self.alpha < 0:
                self.alpha = 255

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()