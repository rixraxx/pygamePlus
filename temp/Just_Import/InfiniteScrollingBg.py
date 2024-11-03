import pygame
from math import ceil

class Background:
    class TileBackground:
        class Tile(pygame.sprite.Sprite):
            def __init__(self, image: pygame.Surface, rect: tuple[int|float, int|float], parent: 'Background.TileBackground') -> None:
                super().__init__()
                self.image = image
                self.parent = parent
                self.rect: pygame.FRect = self.image.get_frect(topleft = (rect[0]*self.parent.image_width, rect[1]*self.parent.image_height))
            
            def update(self) -> None:
                if self.rect.top > self.parent.screen_height: self.rect.top = -self.parent.image_height
                self.rect.move_ip(0,self.parent.speed)
        
        def __init__(self, image: pygame.Surface, screen: pygame.Surface, speed: float = 2.0) -> None:
            self.image = image
            self.screen = screen
            self.speed = speed
            self.screen_width = self.screen.get_width()
            self.screen_height = self.screen.get_height()
            self.image_width = self.image.get_width()
            self.image_height = self.image.get_height()
            rows = ceil(self.screen_width/self.image_width)
            col = ceil(self.screen_height/self.image_height)
            self.group = pygame.sprite.Group() #type: ignore
            for i in range(rows):
                for j in range(-1,col):
                    self.group.add(self.Tile(self.image, (i,j), self))
    
        def update(self):
            self.group.draw(self.screen)
            self.group.update()
    
    class Infinite_Scrolling_Background:
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