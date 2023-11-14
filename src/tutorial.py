import os
import random
import time

import pygame
import tools as tool  # make them into src.-> whatever after testing
from components.attacking import Attacking
from constants import X_pos, Y_pos, weapon_list

pygame.init()
screen = pygame.display.set_mode((X_pos, Y_pos))
font = pygame.font.Font(None, 50)

pygame.display.set_caption('Game?')
clock = pygame.time.Clock()

test = pygame.Surface((X_pos, 100))
test.fill("blue")
text = font.render('Test', False, "Green")


def main_tutorial() -> tuple:

    hp = 100
    defense = 0
    mob = "goblin"
    inv = {}
    crit = None
    mobHp = 20
    mobAttk = "2 - 3"
    mobDefense = 0
    attack = Attacking(weapon_list[0], defense)

    print("tutorial!!", "=========", sep='\n')

    print(
        f"Encountered 'Goblin'! || Hp: {mobHp}, Attk: {mobAttk}, Def: {mobDefense}, Level: 1"
    )
    print("Type attack to attack your opponent!")

    maxHp = hp
    maxMobHp = mobHp
    dang = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #
                    print("jump")

            if event.type == pygame.KEYUP:
                print("woah")

        screen.blit(test, (0, dang))
        screen.blit(text, (dang, 300))
        print(dang)

        pygame.display.update()
        clock.tick(60)

    #     try:
    #         player_input = input('> ').lower()
    #     except EOFError:
    #         player_input = "attack"

    #     if player_input in ["attack", "attk", "q"]:
    #         os.system("cls")

    #         attk = attack.attack_RNGESUS()
    #         defense = attack.defense_RNGESUS(random.randint(2, 5), attk[2])

    #         mobHp -= attk[0]
    #         crit = attk[1]

    #         hp -= defense[0]

    #         if hp <= 0:
    #             quit("ERROR 1: Died unexpected")

    #         if mobHp <= 0:
    #             break

    #         else:
    #             print("+===========================+",
    #                   f"% Rolled: {attk[2]}",
    #                   f"- Lost: {defense[0]}hp",
    #                   sep='\n')

    #         if crit:
    #             print(f"CRIT! Dealt: {attk[0]}hp",
    #                   f"Your Hp: {hp}/{maxHp}",
    #                   f"Enemy Hp: {mobHp}/{maxMobHp}",
    #                   "+===========================+",
    #                   sep='\n')
    #             time.sleep(0.133)

    #         else:
    #             print(f"+ Dealt: {attk[0]}hp",
    #                   f"Your Hp: {hp}/{maxHp}",
    #                   f"Enemy Hp: {mobHp}/{maxMobHp}",
    #                   "+===========================+",
    #                   sep='\n')
    #             time.sleep(0.133)
    #     else:
    #         print("Please type in attack", '\n')
    #         continue

    # print("You have defeated the %s!" % mob)

    # preinv = tool.drops(mob)

    # tool.insertingMobDrops(preinv, "goblin")
    # print("+=====================+",
    #       "You gained 4 xp!",
    #       "+=====================+",
    #       sep="\n")
    # tool.printingDrops(preinv, "goblin")

    # return (hp, inv)

if __name__ == "__main__":
    main_tutorial() 