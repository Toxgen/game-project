import pygame
import random
from random import randint
import time
from time import sleep

__mob_data = (
    # woods [0][0 - 2]
    ("goblin", 8, 2, 3, 1, None), # name, health, r-attk1, r-attk2, defense, s-effect
    ("slime", 12, 3, 4, 3, None),
    ("wolf", 7, 5, 7, 2, None)
    # plains [1][0 - ?]
)

__mob_drops = {
    "goblin": ("goblin_hide", "goblin_leg", "goblin_sword", "goblin_staff", 
               "goblin_chestplate", "goblin_legging", "goblin_helmet"),
    "slime": ("nothing u got scammed lol"),
    "wolf": ("You also got scammed lol")
# maybe add orc
}


__drop_data = {
    "goblin": (("goblin_hide", 25), ("goblin_leg", 12), 
        ("goblin_sword", 8), ("goblin_staff", 5), 
        ("goblin_chestplate", 3), ("goblin_legging", 2), 
        ("goblin_helmet", 1))
}

__possible_locations = (
        "woods", "ruins"
) 
class Mob():

    armorDefBonus = (
        "",
    )

    def __init__(self, 
                 name: str, 
                 drops: tuple, 
                 stats: tuple) -> None:
        
        self.name = name
        self.drops = drops # dros (self explantory)
        self.stats = stats # name, health, r-attk1, r-attk2, defense, s-effect
        
    def returnArmorBonus(self) -> tuple[int]:
       return 

    def foo(self, 
            heatlh: int = 0) -> tuple[int]:
        pass
"""
USE THESE CLASSES TO BLIT OBJECTS WHEN I LEARN PYGAME
"""
class Goblin(Mob):
    def __init__(self, 
                 name: str, 
                 drops: tuple, 
                 stats: tuple) -> None:
        super().__init__(name, drops, stats)

class Slime(Mob):
    def __init__(self, 
                name: str, 
                drops: tuple, 
                stats: tuple) -> None:
        super().__init__(name, drops, stats)

def drops(mob: str) -> list[str]:
    """
    drops(mob)
    mob: mob that is being faced
    """

    luck = random.randint(0, 6)

    returning = []

    for counter, (key, value) in enumerate(__drop_data[mob]):

        if not counter:
            returning.append(key)
        
        if counter >= luck:
            break
          
        x = random.randint(0, 150) if len(returning) >= 3 else random.randint(0, 100)

        if x <= value:
            returning.append(key)
          
    return returning
              
def printingDrops(preinv: list[str], mob) -> None: # change this into blitting
    """
    print em drops
    (the counted drop list, self.mob)
    """

    for q, x in enumerate(__mob_drops[mob]):

        if not q:
            print("+=======================+")

        _amount = [m for m in preinv if m == x]

        if len(_amount) > 1:
            print(f"Earned {len(_amount)} {x}s")

        elif len(_amount) == 0:
            continue
        
        else:
            print(f"Earned {len(_amount)} {x}")

        time.sleep(0.33)

    print("+=======================+")
    return None

def printingInv(inv: dict) -> None: # change this into blitting
    """
    print inventory
    (the inventory)
    """

    print("+========[page 0]=========+")
    count = 0
    for count, (key, value) in enumerate(inv.items()): 

        time.sleep(0.075)

        if count % 8 != 0 or count == 0:
            print(f"+ {key} x {value}", end='\n')
        
        else:
            if len(inv) == count + 1:
                break
            print("+=========================+")

        if count % 8 == 0 and count > 1:
            _check = int(count / 8)
            if len(inv) == count + 1:
                break
            print("\n", f"+========[page {_check}]=========+")
            
    if count % 8 != 0 or len(inv) == count + 1:
        print("+==========[end]==========+")
        return None
        
def returnMob(hp: int, location: str) -> list:
    
    if location not in __possible_locations:
        return None

    if hp > 50:
        _hp_multi = round(hp/50* 0.5) 
        _def_multi = round(hp/50 * 0.5)
        _attk_multi = round(hp/40 * 0.25)
    
    else:
        _hp_multi, _def_multi, _attk_multi = 1, 1, 1

    def __wood_mobs(chance: int) -> list:
        
        _index = 0 if chance < 4 else 1    
        _index = 2 if chance < 12 else 0
         
        return [__mob_data[_index][0],  
                __mob_data[_index][1] * (1 + _hp_multi),
                __mob_data[_index][2] * (1 + _attk_multi),
                __mob_data[_index][3] * (1 + _attk_multi),
                __mob_data[_index][4] * (1 + _def_multi)]
    
    match location:
        case "woods":
            x = random.randint(0, 20)
            return __wood_mobs(chance=x)
            
        case _:
            raise Exception("something went wrong")
        
def insertingMobDrops(preinv: list[str], mob: str, inv: dict = {}) -> dict:

    for thing in __mob_drops[mob]: 
        drop_index = __mob_drops[mob].index(thing)
        _mob_drop = __mob_drops[mob][drop_index]
        check = [item for item in preinv if item == _mob_drop]

        if _mob_drop not in inv and _mob_drop in preinv:
            inv[_mob_drop] = len(check)
            continue

        if _mob_drop in inv:
            inv[_mob_drop] += len(check) 
            continue

        if _mob_drop not in inv:
            continue

        else:
            raise Exception("This really shouldn't happen")
            
    return inv


if __name__ == '__main__':
    pass