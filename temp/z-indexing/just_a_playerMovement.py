import pygame

# Game constants
WIDTH, HEIGHT = 480, 480
TITLE = 'Some caption'
FPS = 60
BG_COLOR = 'grey15'

class PlayerMovement(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, 'mediumseagreen', (25, 25), 25)
        self.rect = self.image.get_rect(center = (240, 0))
        self.direction = pygame.Vector2(0,0)
        self.speed = 5
        self.velocity = 0
    def update(self):
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     self.direction.y = -self.speed
        # elif keys[pygame.K_s]:2
        #     self.direction.y = self.speed
        # else:
        #     self.direction.y = 0
        # if keys[pygame.K_a]:
        #     self.direction.x = -self.speed
        # elif keys[pygame.K_d]:
        #     self.direction.x = self.speed
        # else:
        #     self.direction.x = 0
        # self.rect.move_ip(self.direction)
        
        # Gravity
        if self.rect.bottom < 480:
            self.rect.move_ip((0, int(self.velocity)))
        else: self.rect.center = (240,455)
        self.velocity += 0.2
        if self.velocity > 8: self.velocity = 8



class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        self.player = PlayerMovement()
        self.visible_sprites = pygame.sprite.Group() #type: ignore
        self.visible_sprites.add(self.player)

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.screen.fill(BG_COLOR)

            self.visible_sprites.update()
            self.visible_sprites.draw(self.screen)


            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()