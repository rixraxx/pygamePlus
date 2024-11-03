import pygame
from math import ceil

# Game constants
WIDTH, HEIGHT = 656, 284
TITLE = 'Parallax Background'
FPS = 60
BG_COLOR = 'white'

# Background Sprites loading
Day_sprites = [
    'Done/Pygame/just_a_parallexBg/sprites/day/day sky.png',
    'Done/Pygame/just_a_parallexBg/sprites/day/day buildings back.png',
    'Done/Pygame/just_a_parallexBg/sprites/day/day buildings front.png'
]
Day_sprite_Ground = 'Done/Pygame/just_a_parallexBg/sprites/day/day fence.png'

Evening_sprites = [
    'Done/Pygame/just_a_parallexBg/sprites/evening/evening buildings back.png',
    'Done/Pygame/just_a_parallexBg/sprites/evening/evening buildings front.png',
    'Done/Pygame/just_a_parallexBg/sprites/evening/evening fence.png',
    'Done/Pygame/just_a_parallexBg/sprites/evening/evening sky.png'
]

Night_sprites = [
    'Done/Pygame/just_a_parallexBg/sprites/night/night buildings back.png',
    'Done/Pygame/just_a_parallexBg/sprites/night/night buildings front.png',
    'Done/Pygame/just_a_parallexBg/sprites/night/night fence.png',
    'Done/Pygame/just_a_parallexBg/sprites/night/night sky.png'
]

class ScrollingBackground:
    def __init__(self, image: pygame.Surface, screen: pygame.Surface, scroll_speed: float = 7.5, y: int | float = 0) -> None:
        self.image = image
        self.img_width = self.image.get_width()
        self.screen = screen
        self.scroll_speed = scroll_speed
        self.scroll = 0
        self.tiles = ceil(self.screen.get_width() / self.img_width) + 1
        self.ypos = y

    def draw(self):
        for i in range(self.tiles):
            self.screen.blit(self.image, (i * self.img_width + self.scroll, self.ypos))

    def update(self):
        self.scroll -= self.scroll_speed
        if abs(self.scroll) > self.img_width:
            self.scroll = 0
        self.draw()

class ParallaxBackground:
    def __init__(self, images: list[pygame.Surface], screen: pygame.Surface, speeds: list[float]) -> None:
        self.layers = [ScrollingBackground(image, screen, speed) for image, speed in zip(images, speeds)]

    def update(self):
        for layer in self.layers:
            layer.update()

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.is_running = True

        self.day_images = self.load_images(Day_sprites)
        self.day_ground = pygame.image.load(Day_sprite_Ground).convert_alpha()
        self.parallax_background = ParallaxBackground(self.day_images, self.screen, [1, 3, 5])
        self.ground  = ScrollingBackground(self.day_ground, self.screen,5.7,216)
        self.parallax_background.layers.append(self.ground)

    def load_images(self, image_paths: list[str]) -> list[pygame.Surface]:
        images = [pygame.image.load(path).convert_alpha() for path in image_paths]
        return [pygame.transform.scale2x(image) for image in images]

    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            self.screen.fill(BG_COLOR)
            self.parallax_background.update()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()
