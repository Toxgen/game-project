from os import walk
import pygame
import logging

from src.components.surfaces import Map


def import_folder(path,
                  map=False):
    
    surface_list = []

    if map:
        for _, __, map_files in walk(path):
            for map in map_files:
                full_path = path + '/' + map
                mapmap = Map(full_path)
                surface_list.append(mapmap)
                
    else:
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)

    return surface_list