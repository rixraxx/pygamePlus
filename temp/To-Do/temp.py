import pygame
from random import randint

# Game constants
WIDTH, HEIGHT = 360, 360
TITLE = 'Some caption'
FPS = 60
isrunning = True
BG_COLOR = 'grey15'

class ParticleSystem:
    def __init__(self) -> None:
        self.particles = []
    
    def emmit(self, screen):
        if self.particles:
            self.del_particle()
            for particles in self.particles:
                particles[0][1] += particles[2][1]
                particles[0][0] += particles[2][0]
                particles[1] -= 0.2
                pygame.draw.circle(screen, 'antiquewhite', particles[0], int(particles[1]))


    def app_particles(self):
        xpos = pygame.mouse.get_pos()[0]
        ypos = pygame.mouse.get_pos()[1]
        radius = 10
        direction_x = randint(-3, 3)
        direction_y = randint(-3, 3)
        particle_circle = [[xpos, ypos], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)
    
    def del_particle(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

# General setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(TITLE)

# Pygame ParticleSystem
particles = ParticleSystem()
PARTICLE_CALL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_CALL_EVENT, 70)

# Main game loop
while isrunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isrunning = False
        if event.type == PARTICLE_CALL_EVENT:
            particles.app_particles()

    # Filling last Frame
    screen.fill(BG_COLOR)

    # Game logic
    particles.emmit(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()