import pygame

# Game constants
WIDTH, HEIGHT = 480, 480
BLOCK_SIZE = 160
TITLE = 'Tic-Tac-Toe'
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
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        # IN game state
        self.gameState = 'menu'
        self.clicked = False

        # General font
        self.gen_font = pygame.font.SysFont('Arial', 26)
        self.markers_font = pygame.font.SysFont('Arial', 80)
        self.title_font = pygame.font.SysFont('Algerian', 45)
        self.title = self.title_font.render('Tic-Tac-toe', True, 'antiquewhite')

        # MainMenu Buttons
        self.start_btn = AnimatedButton(240, 270, Button, self.gen_font, 'START', 2)
        self.exit_btn = AnimatedButton(240, 350, Button, self.gen_font, 'EXIT',2)

    def Draw_grid(self):
        for i in range(1,3):
            pygame.draw.line(self.screen, 'antiquewhite',(BLOCK_SIZE*i, 0), (BLOCK_SIZE*i, HEIGHT), 2)
            pygame.draw.line(self.screen, 'antiquewhite',(0, BLOCK_SIZE*i), (WIDTH, BLOCK_SIZE*i), 2)
    
    def reset(self):
        self.winner = None
        self.board = [[0 for _ in range(3)]for _ in range(3)]
        self.gameState = 'game'
        self.turn = 'x'

    def draw_markers(self, mousepo):
        pass


    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False
                if self.gameState == 'game':
                    if event.type == pygame.MOUSEBUTTONDOWN and not self.clicked:
                        self.draw_markers(pygame.mouse.get_pos())
                        self.clicked = True
                    if event.type == pygame.MOUSEBUTTONUP and self.clicked:
                        self.clicked = False
                    
                        

            self.screen.fill(BG_COLOR)

            if self.gameState == 'menu':
                self.screen.blit(self.title, self.title.get_rect(center = (240, 140)))
                if self.start_btn.draw(self.screen):
                    self.reset()
                if self.exit_btn.draw(self.screen):
                    self.isrunning = False
            elif self.gameState == 'game':
                self.Draw_grid()


            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()