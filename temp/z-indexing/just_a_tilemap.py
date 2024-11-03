import pygame

# Game constants
WIDTH, HEIGHT = 640, 480
TITLE = 'Some caption'
FPS = 20
BG_COLOR = 'grey15'

class SingleImageButton:
        def __init__(self, xpos: float | int, ypos: float | int, image: str, scale: float | int = 1):
            self.image = pygame.image.load(image).convert_alpha()
            if scale != 1:
                self.image = pygame.transform.scale_by(self.image, scale)
            self.rect = self.image.get_rect(topleft = (xpos, ypos))
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

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        self.main_surface = pygame.Surface((512,480))
        self.main_surface.fill('mediumseagreen')
        self.tile_map = [[None for i in range(16)] for j in range(16)]
        for i in range(1,16):
            pygame.draw.line(self.main_surface, 'grey35',(32*i, 0), (32*i, HEIGHT))
            pygame.draw.line(self.main_surface, 'grey35',(0, 32*i), (WIDTH, 32*i))
        
        self.tiles_surface = pygame.Surface((128,480))
        self.tiles_surface.fill('grey25')
        self.origanl_tile = [pygame.image.load(f'Tiles/{i}.png').convert_alpha() for i in range(1,5)]
        self.origanl_tile = [pygame.transform.scale2x(_) for _ in self.origanl_tile]
        self.tile = [SingleImageButton(28, 28+(i*120), f'Tiles/{i+1}.png', 4) for i in range(4)]

        self.tile_selected = None

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.screen.fill(BG_COLOR)

            self.screen.blit(self.main_surface, (128,0))
            self.screen.blit(self.tiles_surface, (0,0))
            
            if self.tile[0].draw(self.tiles_surface):
                self.tile_selected = 0
            if self.tile[1].draw(self.tiles_surface):
                self.tile_selected = 1
            if self.tile[2].draw(self.tiles_surface):
                self.tile_selected = 2
            if self.tile[3].draw(self.tiles_surface):
                self.tile_selected = 3

            pos = pygame.mouse.get_pos() 
            if self.tile_selected != None and pos[0] > 128:    
                xpos = pos[0]//32
                ypos = pos[1]//32
                self.screen.blit(self.origanl_tile[self.tile_selected], pos)
                if pygame.mouse.get_pressed()[0] == 1:
                    self.main_surface.blit(self.origanl_tile[self.tile_selected], ((xpos * 32)-128, (ypos*32)))

            
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()