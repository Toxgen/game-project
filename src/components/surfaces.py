import pytmx
import pygame
import logging
from src.constants import layers

class Map(pygame.surface.Surface):

    def __init__(self, filename, group=None):

        tm = pytmx.load_pygame(filename, pixelalpha = True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.group = group

        self.filename = filename.split('/')[-1].split(".")[0]

    def __str__(self):
        return self.filename
    
    def __setattr__(self, name: str, value) -> None:
        if name == "group" and value is not None:
            super().__init__(value)
        else:
            return super().__setattr__(name, value)
        
    def render(self, surface, offset):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, ((x - offset.x / self.tmxdata.tilewidth) * self.tmxdata.tilewidth , 
                                            (y - offset.y / self.tmxdata.tileheight) *self.tmxdata.tileheight))
                        
                        
    def make_map(self, offset=pygame.Vector2(0, 0)):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface, offset)
        return temp_surface
    
    def update(self):
        return self.make_map()
    
class Default(pygame.sprite.Sprite):
    def __init__(self, pos, surf, group, z_index = layers):
        super().__init__(group)
        self.pos = pos
        self.surf = surf
        self.z_index = z_index

class Water(Default):
    def __init__(self, pos, frames, group):
        self.frames = frames
        self.frame_index = 0

        super().__init__(pos, 
                         self.frames[self.frame_index], 
                         group)
        
    def animate(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)

class Other(Default):
    def __init__(self, pos, frames, group):
        self.frames = frames
        self.frame_index = 0

        super().__init__(pos, 
                         self.frames[self.frame_index], 
                         group)
        
    def animate(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)
        