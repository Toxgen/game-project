global __mob_data, __mob_drops, __possible_mobs

__mob_data = [ 
    # woods [0][0 - 2]
    ["goblin", 8, 2, 3, 1, None],
    ["slime", 12, 3, 4, 3, None],
    ["wolf", 7, 5, 7, 2, None]
    # plains [1][0 - ?]
]


__mob_drops = {
    "goblin": ["goblin_hide", "goblin_sword", "goblin_staff", 
               "goblin_chestplate", "goblin_legging", "goblin_helmet"],
# maybe add orc
}

__possible_mobs = [
    "goblin", "slime", "wolf"
]

def drops(mob: str) -> list:
    """
    drops(mob)
    mob: mob that is being faced
    """

    # make this better cause its possible to 

    import random as r
    from random import randint

    luck = r.randint(1, 6)

    match mob:

        case "goblin":

            returning = []

            for _i in range(luck):

                if not _i: # guaranteed 1
                    returning.append("goblin_hide")

                _x = r.randint(0, 100)

                if len(returning) >= 3:
                    _x = r.randint(0, 150)

                if _x <= 3:
                    _x = r.randint(1, 3)
                    if _x == 1:
                        returning.append("goblin_chestplate")

                    elif _x == 2:
                        returning.append("leather_legging")

                    else:
                        returning.append("goblin_helmet")

                if _x <= 5:  
                    returning.append("goblin_staff")
                    continue

                if _x <= 8:  
                    returning.append("goblin_sword")
                    continue

                if _x <= 12:  
                    returning.append("goblin_leg")
                    continue

                if _x <= 25: 
                    returning.append("goblin_hide")
                    continue

            return returning

        case _:
            raise Exception("1st: Oh NAHHHHHHHHHHHHHHHHH")

def counting_drop(check: list[str], mob: str):
    """
    counting_drop(list, mob)
    list: cct inventory
    mob: the mob that is being faced
    """

    match mob:

        case "goblin":
            g_hide = check.count("goblin_hide")

            g_leg = check.count("goblin_leg")
            
            g_sword = check.count("goblin_sword")

            g_staff = check.count("goblin_staff")

            g_chest = check.count("goblin_chestplate")

            g_legging = check.count("goblin_legging")

            g_helmet = check.count("goblin_helmet")

            return [g_hide, g_leg, g_sword, g_staff, g_chest, g_legging, g_helmet] # dont forget to index this into the game.py thing
    
        case _:
            raise Exception("Error: This shouldn't happen, p.s. check mob arg")
              
def printingDrops(preinv: list[str]):
    """
    print em drops
    (the counted drop list, self.mob)
    """

    import time as t
    from time import sleep

    for _q, x in enumerate(preinv):

        if not _q:
                print("+=======================+")

        if preinv[_q] > 1:
            print(f"Earned {preinv[_q]} {x}s")
        else:
            print(f"Earned {preinv[_q]} {x}")

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
    print(f"len: {len(inv)}")
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
        
def returnMob(hp: int, location: str) -> list:
    import random as r
    from random import randint

    if hp > 50:
        _hp_multi = round(hp/20 * 0.5) 
        _def_multi = round(hp/20 * 0.5)
        _attk_mul = round(hp/30 * 0.25)
    
    else:
        _hp_multi = 1
        _def_multi = 1
        _attk_mul = 1

    def __wood_mobs(__mob_data: list, mob: str, hp: int, defe: int, attk: int) -> list: 
        # there should be a easier way to do this way less boilerplate code
        match mob:
            case "goblin":
                    return [__mob_data[0][0], 
                            __mob_data[0][1] + hp + hp * 0.5, 
                            __mob_data[0][2] + attk + attk * 0.5,
                            __mob_data[0][3] + attk + attk * 0.5,
                            __mob_data[0][4] + defe + defe * 0.5]
        
            case "slime":
                    return [__mob_data[1][0], 
                            __mob_data[1][1] + hp + hp * 0.5, 
                            __mob_data[1][2] + attk + attk * 0.5,
                            __mob_data[1][3] + attk + attk * 0.5,
                            __mob_data[1][4] + defe + defe * 0.5]
            case "wolf":
                pass # work on this later

            case _:
                raise Exception("wood mobs error")  
    
    match location:
        case "woods":
            x = r.randint(0, 20)
            if x > 12:
                return __wood_mobs(__mob_data, __mob_data[0][0], _hp_multi, _def_multi, _attk_mul)
            
            if x > 8:
                return __wood_mobs(__mob_data, __mob_data[1][0], _hp_multi, _def_multi, _attk_mul)
            
            if x > 4:
                return __wood_mobs(__mob_data, __mob_data[2][0], _hp_multi, _def_multi, _attk_mul)
        case _:
            raise Exception("ERROR 1: MissType")
        
def insertingMobDrops(preinv: list[str], mob: str, inv: list = []) -> list:

    for thing in __mob_drops[mob]: 
        drop_index = __mob_drops[mob].index(thing)
        _mob_drop = __mob_drops[mob][drop_index]

        if not _mob_drop in inv and _mob_drop in preinv:
            check = [item for item in preinv if item == _mob_drop]
            inv.append([_mob_drop, len(check)])
            continue

        if _mob_drop in inv:
            indices = [index for index, sublist in enumerate(inv) if _mob_drop in sublist]
            print(indices)
            inv[indices[0]][1] += 1

        if not _mob_drop in inv:
            continue

        else:
            quit("""Error has occured:
                 hint: I don't have a hint, this seriously shouldn't happen""")
            
    return inv


if __name__ == '__main__':
    pass