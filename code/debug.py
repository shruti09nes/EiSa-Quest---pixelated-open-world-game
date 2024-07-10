import pygame  #import python library
pygame.init()  #initialize imported module ... called before beigning pygame program
font = pygame.font.Font(None,30) #specifies font file

def debug(info,y = 10, x = 10):   #display debugging information
	display_surface = pygame.display.get_surface() #gets display screen -- whee graphics rendered
	debug_surf = font.render(str(info),True,'White') 
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)  #draw rectangle
	display_surface.blit(debug_surf,debug_rect)  #blit/draw text file on display screen
