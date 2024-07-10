import pygame, sys, asyncio 
from settings import *
from level import Level
from gameover import GameOverScreen
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Eisa')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.game_over_screen = GameOverScreen()
        self.player_lives = 3 
        
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    def run(self):
        print("Game started!")
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    elif event.key == pygame.K_q:  # Quit the game
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_r:  # Restart the game
                        self.restart_game()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            
            # Check game over condition
            if self.level.player.game_over:
                self.game_over(self.level.player.score)  # Pass the player's score to game_over method
            
            pygame.display.update()
            self.clock.tick(FPS)

    def game_over(self, earned_score):
        self.game_over_screen.display(self.screen, earned_score)
        # Display prompt
        font = pygame.font.Font(None, 36)
        text_quit = font.render("Press Q to quit", True, (255, 255, 255))
        text_quit_rect = text_quit.get_rect(center=(WIDTH // 2, HEIGTH // 2 + 50))
        self.screen.blit(text_quit, text_quit_rect)
        
        text_restart = font.render("Press R to restart", True, (255, 255, 255))
        text_restart_rect = text_restart.get_rect(center=(WIDTH // 2, HEIGTH // 2 + 100))
        self.screen.blit(text_restart, text_restart_rect)
        
        pygame.display.update()

    def restart_game(self):
        # Reset game state
        self.level = Level()
        self.level.player.score = 0
        self.level.player.game_over = False

if __name__ == '__main__':
    game = Game()
    game.run()
