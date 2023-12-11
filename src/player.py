import pygame, sys, json
from src.constants import *

from src.components.support import *

pygame.init()

class Player(pygame.sprite.Sprite):

    def save(self) -> None:

        obj = (self.player, self.inv, self.location)

        with open("save/data.json", "w") as file:        
            json.dump(obj, file, indent=4)

        return None
    
    @staticmethod
    def load() -> None:
        
            try:
                with open("save/data.json") as file:
                    data = json.load(file)
                    return data

            except json.decoder.JSONDecodeError as j:
                print("first time saving: inputting standard form. error -> %s" % j)
                obj = [{"tutorial_done?": False, "is_attacking?": False}, 
                       [{"hp": 0, "gold": 0,"current_tool": "", "level": 0, "experience": 0}]]
                        
                return obj
                
    def return_next_level(self) -> int:
        return round((1.31 * self.player["level"] + 5))
                
    def __init__(self, group,
                 player: dict = {"hp": 0,
                                 "defense+": 0,
                                 "gold": 0,
                                 "currentTool": None,
                                 "level": 0,
                                 "experience": 0},

                inv: dict = {},
                location: dict = {"x": 250, "y": 250,
                                  "where": "woods"}): 

        super().__init__(group)

        self.import_assets()
        self.status = "down"
        self.frame_index = 0

        self.player = player
        self.inv = inv
        self.location = location
        self.defense = 0 # maybe make method to find the total defense here
        
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (location["x"], location["y"]))

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
    
    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}
        for animation in self.animations.keys():
            fullpath = "Assets/Resources/Character/" + animation
            self.animations[animation] = import_folder(fullpath)
        
        print(self.animations)

    def animation(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status += self.status.split("_")[0] + "_idle"

    def update(self, dt):
         self.input()
         self.get_status
         self.move(dt)
         self.animation(dt)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

    def move(self, dt):
        
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt

        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

    def xp(self) -> int: 
        
        exp = self.player["experience"]
        pre_hp = (self.player["level"] * 5) + 100

        while True:
            amt_exp = self.return_next_level(self.player["level"])
            if exp >= amt_exp:
                level += 1
                exp -= amt_exp
            
            else:
                break
                
        self.player["experience"] = exp
        
        if level > self.level:
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
        