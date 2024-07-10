import pygame
import sys
from settings import *
from enemy import Enemy

class GameOverScreen:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)
    #    self.restart_text = self.font.render('Press R to Restart', True, 'white')
    #    self.quit_text = self.font.render('Press Q to Quit', True, 'white')
        self.score_text = None


    def display(self, screen, earned_score):

        screen.fill('pink')
        self.score_text = self.font.render(f'Final Score: {earned_score}', True, 'white')
        screen.blit(self.score_text, (WIDTH // 2 - self.score_text.get_width() // 2, HEIGTH // 2 - 50))
    #    screen.blit(self.restart_text, (WIDTH // 2 - self.restart_text.get_width() // 2, HEIGTH // 2))
    #    screen.blit(self.quit_text, (WIDTH // 2 - self.quit_text.get_width() // 2, HEIGTH // 2 + 50))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    return 'restart'
                elif event.key == pygame.K_w:  # Quit the game
                    pygame.quit()
                    sys.exit()
