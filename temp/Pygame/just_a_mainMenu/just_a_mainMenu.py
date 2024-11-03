import pygame

# Game constants
WIDTH, HEIGHT = 640, 480
TITLE = 'Some caption'
FPS = 60
BG_COLOR = 'grey15'

Button = ['./Button/buttons_ideal.png', 'Button/buttons_pressed.png']

class AnimatedButton:
    def __init__(self, xpos: float | int, ypos: float | int, image: list[str], font: pygame.Font, text: str, scalex: float | int = 1, scaley: float | int = 1):
        self.image = [pygame.image.load(_).convert()for _ in image]
        self.font = font.render(text, True, 'black')
        if scalex != 1 or scaley !=0:
            self.image = [pygame.transform.scale_by(_, (scalex, scaley))for _ in self.image]
        self.rect = self.image[0].get_rect(midbottom = (xpos, ypos))
        self.clicked = False
        self.font_rect = self.font.get_rect(center = (self.image[0].get_width()/2,self.image[0].get_height()/2))
        self.image[0].blit(self.font, self.font_rect)
        self.image[1].blit(self.font, self.font_rect)
                    
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

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        # IN game state
        self.gameState = 'menu'

        # General font
        self.gen_font = pygame.font.SysFont('Arial', 26)

        # MainMenu Buttons
        self.start_btn = AnimatedButton(320, 200, Button, self.gen_font, 'START', 2)
        self.option_btn = AnimatedButton(320, 296, Button, self.gen_font,'OPTION', 2)
        self.exit_btn = AnimatedButton(320, 392, Button, self.gen_font, 'EXIT',2)

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.screen.fill(BG_COLOR)

            if self.gameState == 'menu':
                if self.start_btn.draw(self.screen):
                    print('srt')
                    self.gameState = 'game'
                if self.option_btn.draw(self.screen):
                    print('opt')
                if self.exit_btn.draw(self.screen):
                    self.isrunning = False
            elif self.gameState == 'game':
                pass


            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()