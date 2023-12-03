import pygame
import random
from random import randint
import time
from time import sleep

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