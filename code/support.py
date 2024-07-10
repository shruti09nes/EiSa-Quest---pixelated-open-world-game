from csv import reader  #to read csv file
from os import walk  #generate file name in directory either top down or bottom up
import pygame

def import_csv_layout(path):  
	terrain_map = []  
	with open(path) as level_map: 
		layout = reader(level_map,delimiter = ',') #read opened csv file
		for row in layout: #loop for each row
			terrain_map.append(list(row)) #convert each csv row to 2d list
		return terrain_map  #imported csv file

def import_folder(path):  #image
	surface_list = []  #to store surface

	for _,__,img_files in walk(path):  #generate tuple
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list
