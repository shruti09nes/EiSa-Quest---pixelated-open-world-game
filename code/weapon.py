import pygame
import os

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]

        full_path = os.path.join('../graphics/weapons/',
                                 player.weapon, f"{direction}.png")

        try:
            self.image = pygame.image.load(full_path).convert_alpha()
        except pygame.error as e:
            print("Error loading weapon image:", e)
            self.image = pygame.Surface((32, 32))  
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.center).move(10, 10)
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.center).move(-10, 10)
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.center).move(12, 19)
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.center).move(-12, -19)
