__mob_data = [ 
    # woods [0][0 - 2]
    ("goblin", 8, 2, 3, 1, None), # name, health, r-attk1, r-attk2, defense, s-effect
    ("slime", 12, 3, 4, 3, None),
    ("wolf", 7, 5, 7, 2, None)
    # plains [1][0 - ?]
]

__mob_drops = {
    "goblin": ("goblin_hide", "goblin_leg", "goblin_sword", "goblin_staff", 
               "goblin_chestplate", "goblin_legging", "goblin_helmet"),
    "slime": ("nothing u got scammed lol"),
    "wolf": ("You also got scammed lol")
# maybe add orc
}

__possible_mobs = [
    "goblin", "slime", "wolf"
]

__drop_data = {
    "goblin": (("goblin_hide", 25), ("goblin_leg", 12), 
        ("goblin_sword", 8), ("goblin_staff", 5), 
        ("goblin_chestplate", 3), ("goblin_legging", 2), 
        ("goblin_helmet", 1))
}

__possible_locations = (
        "woods", "ruins"
) 
# class mob():
#     def __init__(self, name, drops, data):
#         self.name = 
def drops(mob: str) -> list:
    """
    drops(mob)
    mob: mob that is being faced
    """

    import random as r
    from random import randint

    luck = r.randint(0, 6)

    returning = []

    for counter, (key, value) in enumerate(__drop_data[mob]):

        if not counter:
            returning.append(key)
        
        if counter >= luck:
            break
          
        x = r.randint(0, 150) if len(returning) >= 3 else r.randint(0, 100)

        if x <= value:
            returning.append(key)
          
    return returning
              
def printingDrops(preinv: list[str], mob):
    """
    print em drops
    (the counted drop list, self.mob)
    """

    import time as t
    from time import sleep

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

        t.sleep(0.33)

    print("+=======================+")

def printingInv(inv: dict) -> None:
    """
    print inventory
    (the inventory)
    """

    import time as t
    from time import sleep

    print("+========[page 0]=========+")
    count = 0
    for count, i in enumerate(inv): 

        t.sleep(0.075)

        if count % 8 != 0 or count == 0:
            print(f"+ {i[1]} x {i[0]}")
        
        else:
            if len(inv) == count + 1:
                break
            print("+=========================+")

        if count % 8 == 0 and count > 1:
            _check = int(count / 8)
            if len(inv) == count + 1:
                break
            print("\n")
            print(f"+========[page {_check}]=========+")
            
    if count % 8 != 0 or len(inv) == count + 1:
        print("+==========[end]==========+")
        
def returnMob(hp: int, location: str) -> (list | None):
    import random as r
    from random import randint
    
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
        
        print(f"chance: {chance}")
            
        return [__mob_data[_index][0],  
                __mob_data[_index][1] * (1 + _hp_multi),
                __mob_data[_index][2] * (1 + _attk_multi),
                __mob_data[_index][3] * (1 + _attk_multi),
                __mob_data[_index][4] * (1 + _def_multi)]
    
    match location:
        case "woods":
            x = r.randint(0, 20)
            return __wood_mobs(chance=x)
            
        case _:
            raise Exception("ERROR 1: MissType")
        
def insertingMobDrops(preinv: list[str], mob: str, inv: list = []) -> list:

    for thing in __mob_drops[mob]: 
        drop_index = __mob_drops[mob].index(thing)
        _mob_drop = __mob_drops[mob][drop_index]

        if _mob_drop not in inv and _mob_drop in preinv:
            check = [item for item in preinv if item == _mob_drop]
            inv.append([_mob_drop, len(check)])
            continue

        if _mob_drop in inv:
            indices = [index for index, sublist in enumerate(inv)
                       if _mob_drop in sublist]
            inv[indices[0]][1] += 1

        if _mob_drop not in inv:
            continue

        else:
            quit("""Error has occured:
                 hint: I don't have a hint, this seriously shouldn't happen""")
            
    return inv


if __name__ == '__main__':
    pass
