import pygame

# Game constants
WIDTH, HEIGHT = 640, 480
TITLE = 'Some caption'
FPS = 60
BG_COLOR = 'white'

# Button constants
btn_w, btn_h = 160, 60
btn_color = 'grey'
btn_border_clr = 'black'
btn_border_w = 2
pos_x , pos_y = 320, 240
btn_font_color = 'black'

class Button:
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

# Game class
class Game:
    def __init__(self) -> None:
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        self.play_button = Button(x=250, y=20, button_font= pygame.font.SysFont('Arial', 30), border=True)

    def run(self):
        # Main game loop
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            # Filling last Frame
            self.screen.fill(BG_COLOR)

            # Game logic
            if self.play_button.draw(self.screen):
                print('Is clicked')

            pygame.display.flip()
            self.clock.tick(FPS)

        # Dinit pygame
        pygame.quit()

# initi class and running game
if __name__ == "__main__":
    new_game = Game()
    new_game.run()
