import pygame, json
from src.constants import *

pygame.init()

class Player(pygame.sprite.Sprite):

    def save(self) -> None:

        obj = (self.player, self.inv, self.location)

        with open("save/data.json", "w") as file:        
            json.dump(obj, file, indent=4)
        
        obj = self.config
    
    @staticmethod
    def load() -> None:
        
            try:
                with open("save/data.json") as file:
                    json.load(file)

            except json.decoder.JSONDecodeError as j:
                print("first time saving: inputting standard form. error -> %s" % j)
                obj = {
                    "tutorial_done?": False,
                    "is_attacking?": False,
                    "hp": 0, "gold": 0,
                    "current_weapon": "", "level": 0,
                    "experience": 0,
                    "inventory": []
                    }
                    
                with open("save/config.json", "w") as file:        
                    json.dump(obj, file, indent=4)
                        
                return obj
                
    def return_next_level(self) -> int:
        return round((1.31 * player["level"] + 5))
                
    def __init__(self,
                 player: dict = {"hp": 0,
                                 "defense+": 0,
                                 "gold": 0,
                                 "currentTool": None,
                                 "level": 0,
                                 "experience": 0},

                inv: dict = {},
                location: dict = {"x": 0, "y": 0,
                                  "where": "woods"}): 

        super().__init__()
        self.player = player
        self.inv = inv
        self.location = location    

        self.image = pygame.Surface((64, 32))
        self.rect = self.image.get_rect(center = (location["x"], location["y"]))
        self.group = pygame.sprite.Group()

    def update(self):
         pass
    
    def xp(self) -> int: 
        
        exp = self.player["experience"]
        level = self.player["level"]
        pre_hp = (self.player[level] * 5) + 100

        while True:
            amt_exp = self.return_next_level(level)
            if exp >= amt_exp:
                level += 1
                exp -= amt_exp
            
            else:
                break
                
        self.player["experience"] = exp
        
        if level > self.level: # i mean just blit all of this out
            curMaxHp = (level * 5) + 100
            if level - 1 > level:
                print(f"Congrats! You gained {level - self.level} levels")
                print(f"Yay! {pre_hp}hp -> {curMaxHp}hp")
                self.hp = curMaxHp
                print(f"Next level at {self.experience}/{self.return_next_level(level)}xp")
            else:
                print(f"Congrats! You gained {level - self.level} level")
                print(f"Yay! {pre_hp}hp -> {curMaxHp}hp")
                self.hp = curMaxHp
                print(f"Next level at {self.experience}/{self.return_next_level(level)}xp")

        self.player["level"] = level
        return 1

class PlayerMove(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.animation_frame = 0
        self.rect = pygame.Rect(center = (x, y))

    def update(self):
        for keys in pygame.event.