import os
import random
import time

from src.components.attacking import Attacking

from src.components import attacking

from . import tools as tool


def main_tutorial() -> (tuple | None):

    hp = 100
    defense = 0
    mob = "goblin"
    inv = {}
    crit = None
    mobHp = 20
    mobAttk = "2 - 3"
    mobdefense = 0
    attack = Attacking("fist", defense)

    print("tutorial!!", "=========", sep='\n')

    print(
        f"Encountered 'Goblin'! || Hp: {mobHp}, Attk: {mobAttk}, Def: {mobdefense}, Level: 1")
    print("Type attack to attack your opponent!")

    maxHp = hp
    maxMobHp = mobHp

    while True:
        try:
            player_input = input('> ').lower()
        except EOFError:
            player_input = "attack"

        if player_input in ["attack", "atk", "attk", "q"]:
            os.system("cls")

            attk = attack.attk_RNGESUS("fist", mobdefense)
            defense = attack.defense_RNGESUS(random.randint(2, 5), attk[2])

            mobHp -= attk[0]
            crit = attk[1]
            
            hp -= defense[0]

            if hp <= 0:
                quit("ERROR 1: Died unexpected")

            if mobHp <= 0:
                break

            else:
                print("+===========================+",
                        f"% Rolled: {attk[2]}",
                        f"- Lost: {defense[0]}hp", sep='\n')

            if crit:
                print(f"CRIT! Dealt: {attk[0]}hp",
                        f"Your Hp: {hp}/{maxHp}",
                        f"Enemy Hp: {mobHp}/{maxMobHp}", 
                        "+===========================+", 
                        sep='\n')
                time.sleep(0.133)
                
            else:
                print(f"+ Dealt: {attk[0]}hp",
                        f"Your Hp: {hp}/{maxHp}",
                        f"Enemy Hp: {mobHp}/{maxMobHp}", 
                        "+===========================+", 
                        sep='\n')
                time.sleep(0.133)
        else:
            print("Please type in attack", '\n')
            continue

    print("You have defeated the %s!" % mob)

    preinv = tool.drops(mob)

    tool.insertingMobDrops(preinv, "goblin")
    print("+=====================+",
            "You gained 4 xp!",
            "+=====================+", sep="\n")
    tool.printingDrops(preinv, "goblin")

    return (hp, inv)

if __name__ == "__main__":
    main_tutorial()