import pygame
from sprites import *
from config import *
import sys



class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('8bitoperator_jve.ttf', 32)
        self.running = True

        self.character_spritesheet = Spritesheet('img/character.png',True)
        self.terrain_spritesheet = Spritesheet('img/terrain.png',True)
        self.enemy_spritesheet = Spritesheet('img/enemy.png',True)
        self.intro_background = pygame.image.load('img/introbackground.png')
        self.go_background = pygame.image.load('img/gameover.png')
        self.button_spritesheet = Spritesheet('img/ingamebutton2.png',False)

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 'W':
                    Block(self, j, i)
                if column == 'P':
                    self.player = Player(self, j, i)
                if column == 'T':
                    Trophey(self, j, i)
                if column == 'E':
                    Enemy(self, j, i)
                if column == 'B':
                    InGameButton(self,j,i)

    def new(self):


        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # gameloop
        while self.playing:
            self.events()
            self.update()
            self.draw()



    def game_over(self):
        pygame.mixer.music.load('sound/8-bit-video-game-lose-sound-version-1-145828.mp3')
        pygame.mixer.music.play(0)  # Plays six times, not five!

        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2,WIN_HEIGHT/2))

        restart_button = TextButton(10,WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 32)
        quit_button = TextButton(500, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Quit', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.mixer.music.load('sound/Worldmap Theme 2.mp3')
                pygame.mixer.music.play(500)  # Plays six times, not five!

                self.new()
                self.main()
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.quit()
                sys.exit()


            self.screen.blit(self.go_background, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
    def intro_screen(self):
        pygame.mixer.music.load('sound/Intro Theme.mp3')
        pygame.mixer.music.play(500)  # Plays six times, not five!

        intro = True

        title = self.font.render('RPG PUZZLE GAME', True, BLACK)
        title_rect = title.get_rect(x=220, y=10)

        play_button = TextButton(220, 100, 200, 100, WHITE, BLACK, 'Play', 64)
        instruction_button = TextButton(140, 240, 380, 100, WHITE, BLACK, 'Instructions', 64)
        quit_button = TextButton(220, 360, 200, 100, RED, BLACK, 'Quit', 64)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.mixer.music.load('sound/Worldmap Theme 2.mp3')
                pygame.mixer.music.play(100)
 # Plays six times, not five!
                intro = False
            if instruction_button.is_pressed(mouse_pos, mouse_pressed):

                self.instruction_screen()
                intro = False
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.quit()
                sys.exit()

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(instruction_button.image, instruction_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def pause_screen(self):
        pygame.mixer.music.load('sound/Worldmap Theme LOW PASS.wav')
        pygame.mixer.music.play(100)
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        play_button = TextButton(220, 400, 200, 100, WHITE, BLACK, 'Resume', 64)


        if play_button.is_pressed(mouse_pos, mouse_pressed):
            pygame.mixer.music.load('sound/Worldmap Theme 2.mp3')
            pygame.mixer.music.play(100)
            instruction = False


    def instruction_screen(self):
        instruction = True

        title = self.font.render('Instructions', True, BLACK)
        title_rect = title.get_rect(x=220, y=10)

        message1 = self.font.render('This is a game about puzzles.', True, BLACK)
        message_rect1 = title.get_rect(x=10, y=50)
        message2 = self.font.render('You have to solve puzzles in the dungeons', True, BLACK)
        message_rect2 = title.get_rect(x=120, y=80)

        play_button = TextButton(220, 400, 200, 100, WHITE, BLACK, 'Play', 64)
        while instruction:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    instruction = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                pygame.mixer.music.load('sound/Worldmap Theme 2.mp3')
                pygame.mixer.music.play(100)
                instruction = False

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(message1, message_rect1)
            self.screen.blit(message2, message_rect2)
            self.screen.blit(play_button.image, play_button.rect)

            pygame.display.update()


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
