from os import walk
import pygame
import logging

from src.components.maps import Map


def import_folder(path,
                  map=False):
    
    logging.debug("running??")
    
    surface_list = []

    if map:
        logging.debug("running?")
        for _, __, map_files in walk(path):
            full_path = path + '/' + map_files[0]
            mapmap = Map(full_path)
            surface_list.append(mapmap)

    else:
        logging.debug("running???")

        for _, __, img_files in walk(path):
            logging.debug(f"running????, img_file {img_files}")
            for image in img_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)

    return surface_list