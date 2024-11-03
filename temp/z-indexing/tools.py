import pygame
from math import ceil, floor

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

class Button:
    class SingleImageButton:
        def __init__(self, xpos: float | int, ypos: float | int, image: str, scale: float | int = 1):
            self.image = pygame.image.load(image).convert()
            if scale != 1:
                self.image = pygame.transform.scale_by(self.image, scale)
            self.rect = self.image.get_rect(center = (xpos, ypos))
            self.clicked = False

        def draw(self, screen: pygame.Surface) -> bool:
            action = False
            #get mouse position
            pos = pygame.mouse.get_pos()
            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_just_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True   
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            #draw button on screen
            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action
        
    class RetroButton:
        # Button constants
        btn_w, btn_h = 160, 60
        btn_color = 'grey'
        btn_border_clr = 'black'
        btn_border_w = 2
        pos_x , pos_y = 320, 240
        btn_font_color = 'black'
        def __init__(self, x:int = pos_x, y:int = pos_y, button_width:int = btn_w, button_height:int  = btn_h, button_color: str | pygame.Color = btn_color, border: bool = False, border_color: str | pygame.Color = btn_border_clr, border_width:int = btn_border_w, button_font = None, button_text: str = 'None', font_color: str | pygame.Color = btn_font_color):
            self.button_clicked = False
            self.image = pygame.Surface((button_width, button_height))
            self.image.fill(button_color)
            self.rect = self.image.get_rect(center = (x, y))
            if border: 
                pygame.draw.rect(self.image, border_color, self.image.get_rect(), border_width )
            self.button_text_image = button_font.render(button_text, True, font_color)
            self.image.blit(self.button_text_image, self.button_text_image.get_rect(center = (button_width/2, button_height/2)))
            self.clicked = False

        def draw(self, screen: pygame.Surface) -> bool:
            action = False
            #get mouse position
            pos = pygame.mouse.get_pos()
            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_just_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True   
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            #draw button on screen
            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action
    
    class AnimatedButton:
        '''Contain two sprites one for normal and another for action'''
        def __init__(self, xpos: float | int, ypos: float | int, image: list[str], scale: float | int = 1):
            self.image = [pygame.image.load(_).convert()for _ in image]
            if scale != 1:
                self.image = [pygame.transform.scale_by(_, scale)for _ in self.image]
            self.rect = self.image[0].get_rect(center = (xpos, ypos))
            self.clicked = False

        def draw(self, screen: pygame.Surface) -> bool:
            action = False
            #get mouse position
            pos = pygame.mouse.get_pos()
            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_just_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True   
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            #draw button on screen
            if not self.clicked:
                screen.blit(self.image[0], (self.rect.x, self.rect.y))
            else:
                screen.blit(self.image[1], (self.rect.x, self.rect.y))
            return action
    
class PlayerAnimation:
    def __init__(self, images: list[str], xpos: float|int, ypos: float | int, scale: float | int) -> None:
        self.image: list[pygame.Surface] = [pygame.transform.scale_by((pygame.image.load(_).convert_alpha()), scale) for _ in images]
        self.current_sprite = 0.0
        self.rect = self.image[0].get_rect(center = (xpos, ypos))
    def draw(self, screen: pygame.Surface):
        self.current_sprite += 0.2
        if self.current_sprite > len(self.image): self.current_sprite = 0
        screen.blit(self.image[floor(self.current_sprite)], self.rect)
