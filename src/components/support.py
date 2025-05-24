from os import walk

import pygame
import logging

from math import pow

def import_folder(path,
                  map=False):
    
    surface_list = []

    if map:
        
        from src.components.surfaces import Map

        for _, __, map_files in walk(path):
            for _map in map_files:
                full_path = str(path) + '/' + _map
                mapmap = Map(full_path)
                surface_list.append(mapmap)
                
    else:
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)

    return surface_list

def easeOutQuad(perc_done: int, affect_val: int):
    """
    tweening function

    perc_done: how much of the function is done 0-1
    affect_val: affected value
    """
    return affect_val * ( 1 - (1 - perc_done) * (1 - perc_done) + 1 );

def easeInOutExpo(perc_done: int, affect_val: int):
    """
    tweening function

    perc_done: how much of the function is done 0-1
    affect_val: affected value
    """
    if not perc_done:
        return affect_val
    
    elif perc_done == 1:
        return affect_val * 2
    
    elif perc_done < 0.5:
        return affect_val * ( (1 - pow(2, 20 * perc_done - 10)) / 2  + 1)
    
    else:
        return affect_val * ( (2 - pow(2, -20 * perc_done + 10)) / 2 + 1) 
