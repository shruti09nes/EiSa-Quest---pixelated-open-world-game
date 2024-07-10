import pygame 
from settings import *  #access to all variable defined in settings

class Tile(pygame.sprite.Sprite):  #represent tile object
	def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
		super().__init__(groups)  #calls constructor of superclass
		self.sprite_type = sprite_type
		y_offset = HITBOX_OFFSET[sprite_type]  #retrieve from setting
		self.image = surface
		if sprite_type == 'object':
			self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))  #for object or ibstacle
		else:
			self.rect = self.image.get_rect(topleft = pos)  #for non-object items like ground
		self.hitbox = self.rect.inflate(0,y_offset)
		#hitbox---collison detection	