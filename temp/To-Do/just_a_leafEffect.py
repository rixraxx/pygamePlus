import pygame
from random import randint, choice

# Game constants
WIDTH, HEIGHT = 360, 360
TITLE = 'Some caption'
FPS = 30
BG_COLOR = 'grey15'

class LeafEffect:
    def __init__(self, image: pygame.Surface) -> None:
        self.image = image
        self.particles = []
        # self.endpos = ((60,360), (360, 60))
    def add_particles(self):
        startpos = [10, 10]
        direction = [randint(1, 15), randint(1, 15)]
        self.particles.append([startpos,direction])
    def del_particles(self):
        particle_copy = [_ for  _ in self.particles if _[0][0] < 360 or _[0][1] < 360]
        self.particles = particle_copy
    def emmit(self, screen: pygame.Surface):
        if self.particles:
            self.del_particles()
            for leaf in self.particles:
                leaf[0][0] += leaf[1][0]
                leaf[0][1] += leaf[1][1]
                screen.blit(self.image, leaf[0])

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        # Particle System
        self.leaf_img = pygame.image.load('leaf.png').convert_alpha()
        self.particleSystem = LeafEffect(self.leaf_img)
        self.particles_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.particles_event, 275)

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False
                if event.type == self.particles_event:
                    self.particleSystem.add_particles()

            self.screen.fill(BG_COLOR)

            self.particleSystem.emmit(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()