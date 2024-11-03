import pygame

# Game constants
WIDTH, HEIGHT = 512, 384
TITLE = 'Some caption'
FPS = 30

# Backgroun tile
Bg_Tile = ['Done/Pygame/just_a_scrollingBg/Blue.png',
           'Done/Pygame/just_a_scrollingBg/Brown.png',
           'Done/Pygame/just_a_scrollingBg/Gray.png',
           'Done/Pygame/just_a_scrollingBg/Green.png',
           'Done/Pygame/just_a_scrollingBg/Pink.png',
           'Done/Pygame/just_a_scrollingBg/Purple.png',
           'Done/Pygame/just_a_scrollingBg/Yellow.png']
current_bg = 4

class TileBackground(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, rect: tuple[int|float, int|float]) -> None:
        super().__init__()
        self.image = image
        self.rect = self.image.get_frect(topleft = (rect[0]*64, rect[1]*64))
    def update(self) -> None:
        if self.rect.top > 384: self.rect.top = -64
        self.rect.move_ip(0,2)

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        self.background_image = pygame.image.load(Bg_Tile[current_bg]).convert()

        self.visible_sprite = pygame.sprite.Group() #type: ignore
        for i in range(8):
            for j in range(-1, 6):
                self.visible_sprite.add(TileBackground(self.background_image, (i,j)))
                

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.visible_sprite.draw(self.screen)
            self.visible_sprite.update()

            self.clock.tick(FPS)
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()