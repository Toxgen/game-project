import json
import os
import pygame
import random as r
import time as t
from os import system
from sys import exit

try:
    import tools as tool

except ModuleNotFoundError:
    from . import tools as tool

"""
Add something that allows the player to load or del save files
Add mana for wands and etc
Add like a dictionary for if they have finished like the tutorial or something
"""
all_armors = {
    # defualt
    "pants": (0, None, None, "A pair of pants"), # defense, sell, buy, description
    # goblin
    "goblin_chestplate": (1, None, None, "Green chestplate")
}

class Game(pygame.sprite.Sprite):
    
    @staticmethod
    def get_obj(config=False):
        
        if config:
            try:
                with open("save/config.json") as file:
                    data = json.load(file)

            except json.decoder.JSONDecodeError as j:
                print("first time saving: inputting standard form. error -> %s" % j)
                obj = {
                    "tutorial_done?": False,
                    "is_attacking?": False
                }
                    
                with open("save/config.json", "w") as file:        
                    json.dump(obj, file, indent=4)
                        
                return obj
              
        else:
            try:
                with open("save/data.json") as file:
                    data = json.load(file)

            except json.decoder.JSONDecodeError as j:
                print("first time saving: inputting standard form. error -> %s" % j)
                obj = {
                    "hp": 0, "gold": 0,
                    "current_weapon": "", "level": 0,
                    "experience": 0,
                    "inventory": [
                        "", ""
                    ]
                }

                with open("save/data.json", "w") as file:        
                    json.dump(obj, file, indent=4)

                return obj
                
        return data

    def save_obj(self,
                 config: bool = False,
                 both: bool = False) -> None:
        
        if both and config:
            raise Exception("code better")
        
        #------------------------------#
        if both:
            obj = {
                "hp": self.hp, "gold": self.gold,
                "current_weapon": self.currentWeapon, "level": self.level,
                "experience": self.experience,
                "inventory": self.inv
            }

            with open("save/data.json", "w") as file:        
                json.dump(obj, file, indent=4)
            
            obj = self.config

            with open("save/config.json", "w") as file:        
                    json.dump(obj, file, indent=4)

            return None
        #------------------------------#   

        if config:
            obj = self.config
            with open("save/config.json", "w") as file:        
                json.dump(obj, file, indent=4)
            
        else:
            obj = {
                "hp": self.hp, "gold": self.gold,
                "current_weapon": self.currentWeapon, "level": self.level,
                "experience": self.experience,
                "inventory": self.inv
            }
            with open("save/data.json", "w") as file:        
                json.dump(obj, file, indent=4) 

    """
    def return_next_level(self):
        return
    """
    
    def __init__(self, 
                 hp: int,
                 config: dict,
                 currentWeapon: str = "fist", 
                 gold: int = 0,
                 level: int = 0,
                 experience: int = 4,
                 inv: list = [], # plan to change this into a dictionary
                 location: str = "woods"): 
        
        super.__init__()
        self.hp = hp
        self.defense = 0
        self.gold = gold
        self.player_input = ''
        self.currentWeapon = currentWeapon
        self.level = level
        self.experience = experience
        self.inv = inv
        self.location = location
        self.config = Game.get_obj(config=True)

    def xp(self) -> None: 
        possible_XPlevels = (0, 7, 8, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 14, 14, 15, 
                             16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 24, 24, 25, 25, 25, 26, 
                             26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 30, 30, 30, 31, 31, 31, 
                             32, 32, 33, 33, 34, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 
                             39, 40, 40, 41, 41, 42, 42, 43, 44, 44, 44, 45, 46, 46, 47, 48, 
                             48, 48, 49, 50, 51, 51, 52, 53, 53, 54, 55, 56, 56, 57, 58, 59,
                             60, 61, 62) # maybe do some math to figure this out rather than
                            # a big list
        
        exp = self.experience
        level = self.level
        pre_hp = (self.level * 5) + 100

        for x in possible_XPlevels[level:]:
            if exp >= x:
                level += 1
                exp -= x
            
            else:
                break
                
        self.experience = exp
        
        if level > self.level:
            curMaxHp = (level * 5) + 100
            if level - 1 > level:
                print(f"Congrats! You gained {level - self.level} levels")
                print(f"Yay! {pre_hp}hp -> {curMaxHp}hp")
                self.hp = curMaxHp
                print(f"Next level at {self.experience}/{possible_XPlevels[level]}xp")
            else:
                print(f"Congrats! You gained {level - self.level} level")
                print(f"Yay! {pre_hp}hp -> {curMaxHp}hp")
                self.hp = curMaxHp
                print(f"Next level at {self.experience}/{possible_XPlevels[level]}xp")

        self.level = level
        return None
    
    def help_ccmd(self) -> None:
        print("Type In { help } For Commands", "\n")
        t.sleep(0.5)
        while True:
            self.player_input = input('> ').lower()

            match self.player_input:

                case "help":
                    os.system("clear")
                    print("""The Following Commands Are:

                        'Stats': To show your stats
                        'Inventory or inv': To show your inventory
                        'Adventure or adv': To start an adventure 
                        'Switch or swi': To switch current weapon
                            """)
                    t.sleep(1.0)
                    continue

                case "stats":
                    os.system("clear")
                    print("WIP")
                    break

                case "inv":
                    os.system("clear")
                    tool.printingInv(self.inv)

                case "adv":
                    os.system("clear")
                    self.main_attack()
                    break

                case _:
                    print("Please type in a allowed command", '\n')
                    
        return None
                    
    def main_attack(self) -> None:
        crit = None
        mob_list = tool.returnMob(self.hp, self.location) # Woods for now, but implement a system later

        if not mob_list:
            print("It is not possible to attack here")
            return None
            
        mob, mobHp = mob_list[0], mob_list[1]
        mobAttk, mobDefe = [mob_list[2], mob_list[3]], mob_list[4]
            
        print(f"Encountered '{mob}'! || Hp: {mobHp}, Attk: {mobAttk[0]} - {mobAttk[1]}, Def: {mobDefe}")
        print("Type attack to attack your opponent!")
        
        maxHp = (self.xp_sys[0] * 5) + 100
        maxMobHp = mobHp

        while True:
            self.player_input = input('> ').lower()
            if self.player_input in ["attack", "atk", "attk", "q"]:
                os.system("clear")

                attk = self.attk_RNGESUS(self.ccWeap, mobDefe)
                print(f"attk: {attk}")
                mobAttkacking = self.defe_RNGESUS(r.randint(mobAttk[0], mobAttk[1]), attk[2])

                mobHp -= attk[0]
                crit = attk[1]

                self.hp -= mobAttkacking[0]

                if self.hp <= 0:
                    quit("WIP")

                if mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {attk[2]}",
                          f"- Lost: {mobAttkacking[0]}hp", sep='\n')

                if crit:
                    print(f"CRIT! Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
                else:
                    print(f"+ Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
            else:
                print("Please type in attack", '\n')
                continue

        print(f"You have defeated the {mob}!")


        preinv = tool.drops(mob)

        self.inv = tool.insertingMobDrops(preinv, mob, self.inv)
        tool.printingDrops(preinv, mob)
        
if __name__ == "__main__":
    main = Game(0)
    print(main)