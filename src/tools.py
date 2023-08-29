class gameInfo:
    pass # might want to just make a place to store all the info in herer

def drops(mob: str) -> list:
    """
    very complicated drops
    (the mob level, self.luck, self.mob)
    """

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
        
def counting_drop(list: list, mob: str):
    """
    count em
    (the drops, self.mob)
    """

    match mob:

        case "goblin":
            g_hide = list.count("goblin_hide")

            g_leg = list.count("goblin_leg")
            
            g_sword = list.count("goblin_sword")

            g_staff = list.count("goblin_staff")

            return [g_hide, g_leg, g_sword, g_staff]
    
        case _:
            raise Exception("Error: This shouldn't happen, p.s. check mob arg")      
def printingDrops(preinv: list, mob: str):
    """
    print em drops
    (the counted drop list, self.mob)
    """

    import time as t
    from time import sleep

    match mob:

        case "goblin":

            for _q in range(len(preinv)):

                match _q:

                        case 0:
                            if preinv[_q] > 1:
                                print("+=======================+",
                                    f"Earned {preinv[_q]} goblin_hides", sep='\n')
                            else:
                                print("+=======================+",
                                    f"Earned {preinv[_q]} goblin_hide", sep='\n')

                            t.sleep(0.33)
                            continue

                        case 1:
                            if preinv[_q]:
                                if preinv[_q] > 1:
                                    print(f"Earned {preinv[_q]} goblin_legs")
                                else:
                                    print(f"Earned {preinv[_q]} goblin_leg")

                                t.sleep(0.33)
                            continue

                        case 2:
                            if preinv[_q]:
                                if preinv[_q] > 1:
                                    print(f"Earned {preinv[_q]} goblin_swords")
                                else:
                                    print(f"Earned {preinv[_q]} goblin_sword")

                                t.sleep(0.33)
                            continue

                        case 3:
                            if preinv[_q]:
                                if preinv[_q] > 1:
                                    print(f"Earned {preinv[_q]} goblin_staffs",
                                        "+=======================+", sep='\n')
                                else:
                                    print(f"Earned {preinv[_q]} goblin_staff",
                                        "+=======================+", sep='\n')
                            else:
                                print("+=======================+")

                                t.sleep(0.33)
            
        case _:
            raise Exception("Error: This shouldn't happen, p.s. check mob arg")        
def printingInv(inv: dict) -> None:
    """
    print inventory
    (the inventory)
    """

    import time as t
    from time import sleep

    __quit = False

    print("+======|inv|======+")
    for _i, (key, value) in enumerate(inv.items()): 
        print(f'+ {value} x {key}')

        t.sleep(0.05)

        if _i % 8 == 0 and _i > 1:
            print("+=================+")

            while True: # probably gotta fix this because if they have a lot of items, then this would just bug out
                # probably do something like i % 8 = 0: blah blah blah
                check = input("Continue? ").lower()
                if check in ["yes", "ye", "y", "continue", "cont"]:
                    print("+=================+")
                    break
                elif check in ["no", "n"]:
                    __quit = True
                    break
                else:
                    continue

            if __quit:
                break

            while _i % 8 != 0:
                print(f"+ {value[_i]} x {key[_i]}")
                
    print("+=================+")

def returnMob(hp: int, location: str) -> list:
    import random as r
    from random import randint
    md = [ 
        # woods [0][0 - 2]
        ["goblin", 8, 2, 3, 1, None],
        ["slime", 12, 3, 4, 3, None],
        ["wolf", 7, 5, 7, 2, None]
        # plains [1][0 - ?]
    ]
    if hp > 50:
        _hp_multi = round(hp/20 * 0.5) 
        _def_multi = round(hp/20 * 0.5)
        _attk_mul = round(hp/30 * 0.25)
    
    else:
        _hp_multi = 1
        _def_multi = 1
        _attk_mul = 1

    def __wood_mobs(md: list, mob: str, hp: int, defe: int, attk: int) -> list: 
        match mob:
            case "goblin":
                for i in range(5):
                    return [md[0][0], 
                            md[0][1] + hp + hp * 0.5, 
                            md[0][2] + attk + attk * 0.5,
                            md[0][3] + attk + attk * 0.5,
                            md[0][4] + defe + defe * 0.5]
        
            case "slime":
                    return [md[1][0], 
                            md[1][1] + hp + hp * 0.5, 
                            md[1][2] + attk + attk * 0.5,
                            md[1][3] + attk + attk * 0.5,
                            md[1][4] + defe + defe * 0.5]
            case "wolf":
                pass # work on this later

            case _:
                raise Exception("wood mobs error")  
    
    match location:
        case "woods":
            x = r.randint(0, 20)
            if x > 12:
                return __wood_mobs(md, md[0][0], _hp_multi, _def_multi, _attk_mul)
            
            if x > 8:
                return __wood_mobs(md, md[1][0], _hp_multi, _def_multi, _attk_mul)
            
            if x > 4:
                return __wood_mobs(md, md[2][0], _hp_multi, _def_multi, _attk_mul)
        case _:
            raise Exception("ERROR 1: MissType")

if __name__ == '__main__':
    pass