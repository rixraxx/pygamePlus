import pygame

# Game constants
WIDTH, HEIGHT = 640, 480
TITLE = 'Some caption'
FPS = 60
BG_COLOR = 'white'

# Button constants
Demo_Img = 'Button/start_btn.png'

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

# Game class
class Game:
    def __init__(self) -> None:
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        # GameObject initilization
        self.start_button = SingleImageButton(WIDTH/2, HEIGHT/2, Demo_Img, 0.5)

    def run(self):
        # Main game loop
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            # Filling last Frame
            self.screen.fill(BG_COLOR)

            # Game logic
            if self.start_button.draw(self.screen):
                print('Start Game')

            pygame.display.flip()
            self.clock.tick(FPS)

        # Dinit pygame
        pygame.quit()

# initi class and running game
if __name__ == "__main__":
    new_game = Game()
    new_game.run()
