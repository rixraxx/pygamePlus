import pygame
from math import floor, ceil

# Game constants
WIDTH, HEIGHT = 480, 480
TITLE = 'Some caption'
FPS = 30
BG_COLOR = 'lightgreen'

# Player Constant
Ideal_Sprites = [f'Done/Pygame/Just_A_PlayerAnim/sprites/Idle/Idle_0{i}.png' for i in range(1,13)]
Run_Sprites = [f'Done/Pygame/Just_A_PlayerAnim/sprites/Run/Run_0{i}.png' for i in range(1,9)]
Attack_Sprites = [f'Done/Pygame/Just_A_PlayerAnim/sprites/Attack/Attack_02_0{i}.png' for i in range(1,12)]

class AnimatedButton:
    def __init__(self, xpos: float | int, ypos: float | int, image: list[str], font: pygame.Font, text: str, scale: float | int = 1):
        self.image = [pygame.image.load(_).convert()for _ in image]
        self.font = font.render(text, True, 'black')
        if scale != 1:
            self.image = [pygame.transform.scale_by(_, scale)for _ in self.image]
        self.rect = self.image[0].get_rect(midbottom = (xpos, ypos))
        self.clicked = False
        self.font_rect = self.font.get_rect(center = (44,28))
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

class Character:
    def __init__(self, images: list[str], xpos: float|int, ypos: float | int, scale: float | int) -> None:
        self.image: list[pygame.Surface] = [pygame.transform.scale_by((pygame.image.load(_).convert_alpha()), scale) for _ in images]
        self.current_sprite = 0.0
        self.rect = self.image[0].get_rect(center = (xpos, ypos))
    def draw(self, screen: pygame.Surface):
        self.current_sprite += 0.2
        if self.current_sprite > len(self.image): self.current_sprite = 0
        screen.blit(self.image[floor(self.current_sprite)], self.rect)

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.isrunning = True

        self.general_font = pygame.font.SysFont('Arial', 20, True)
        
        self.button_list = ['Done/Pygame/Just_A_PlayerAnim/sprites/Button/buttons_ideal.png', 'Done/Pygame/Just_A_PlayerAnim/sprites/Button/buttons_pressed.png']
        self.ideal_button = AnimatedButton(80, HEIGHT-20, self.button_list, self.general_font, 'IDEAL')
        self.attack_button = AnimatedButton(240, HEIGHT-20, self.button_list, self.general_font, 'ATTACK')
        self.run_button = AnimatedButton(400, HEIGHT-20, self.button_list, self.general_font, 'RUN')

        self.ideal_char = Character(Ideal_Sprites, 240, 240, 2.5)
        self.attack_char = Character(Attack_Sprites, 240, 240, 2.5)
        self.run_char = Character(Run_Sprites, 240, 240, 2.5)
        self.player_anim = [self.ideal_char, self.run_char, self.attack_char]
        self.current_anim = 0

    def run(self):
        while self.isrunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isrunning = False

            self.screen.fill(BG_COLOR)

            self.player_anim[self.current_anim].draw(self.screen)
            
            if self.ideal_button.draw(self.screen):
                self.current_anim = 0
            if self.run_button.draw(self.screen):
                self.current_anim = 1
            if self.attack_button.draw(self.screen):
                self.current_anim = 2
            
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == '__main__':
    new_game = Game()
    new_game.run()