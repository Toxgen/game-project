def drops(mob: str) -> list:
    """
    drops(mob)
    mob: mob that is being faced
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

                if _x <= 3:
                    _x = r.randint(1, 3)
                    if _x == 1:
                        returning.append("goblin_chestplate")

                    elif _x == 2:
                        returning.append("leather_leggings")

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

def counting_drop(list: list, mob: str):
    """
    counting_drop(list, mob)
    list: cct inventory
    mob: the mob that is being faced
    """

    match mob:

        case "goblin":
            g_hide = list.count("goblin_hide")

            g_leg = list.count("goblin_leg")
            
            g_sword = list.count("goblin_sword")

            g_staff = list.count("goblin_staff")

            g_chest = list.count("goblin_chestplate")

            g_legging = list.count("goblin_legging")

            g_helmet = list.count("goblin_helmet")

            return [g_hide, g_leg, g_sword, g_staff, g_chest, g_legging, g_helmet]
    
        case _:
            raise Exception("Error: This shouldn't happen, p.s. check mob arg")
              

if __name__ == "__main__":
    import time
    t = time.time()
    c = drops("goblin")
    print(c)
    print("1/2")
    print(counting_drop(c, "goblin"))
    tt = time.time()
    tt -= t
    round(tt)
    print(f"2/2! Build Finished in (time: {tt}s)")