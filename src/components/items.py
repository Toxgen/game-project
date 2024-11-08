import pygame

from src.components.support import import_folder
class Item:

    def __init__(self, 
                 name: str, 
                 description: str, 
                 type: str,
                 buy: int, 
                 sell: int,

                 effect: tuple = None,
                 damage: int = None,
                 defense: int = None):
        
        self.name = name
        self.description = description
        self.type = type

        self.buy = buy
        self.sell = sell

        self.effect = effect
        self.damage = damage
        self.defense = defense
        
        self.import_image()

    def import_image(self):
        full_path = "Assets/Resources/Items/" + self.name
        self.image = import_folder(full_path)

    def returnEffect(self):
        if self.type == "potion":
            return self.effect
        