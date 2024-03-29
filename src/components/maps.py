import pytmx
import pygame
import logging

class Map(pygame.surface.Surface):

    map_prop = {
        "test": {"tp_point_1": (0, 0, 500, 1000, "Foo")}
    }
    def make_points(self, tl, tr, bl, br):
        pass # make the rect to teleport ig 
    # and return it so in game.py it can check if it's hitten

    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha = True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

        self.filename = filename.split('/')[-1].split(".")[0]

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x*self.tmxdata.tilewidth, y*self.tmxdata.tileheight))
                        
    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
    
    def update(player=None):
        if player is None:
            return False # for some reason??
        pass
        # TODO just change the map tmx file name to the map
        # then make a class variable dict that stores the location
        # of where each rect is and check if it gets hit by the player arg