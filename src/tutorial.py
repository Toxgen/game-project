#!/usr/bin/env python3

import random
import time
from sys import exit
import os

import pygame
try:
    import src.tools as tool  
    from src.components.attacking import Attacking
    from src.constants import Screen_dim, Weapon_tuple

except ModuleNotFoundError:
    import tools as tool
    from components.attacking import Attacking
    from constants import Screen_dim, Weapon_tuple

pygame.init()
screen = pygame.display.set_mode(Screen_dim)
font = pygame.font.Font(None, 30)

pygame.display.set_caption('Game')
clock = pygame.time.Clock()

bottomRect = pygame.image.load(os.path.join('Assets/AttackBar.png')).convert_alpha()
bottomRect = pygame.transform.scale(bottomRect, (600, 500))
screen.blit(bottomRect, (0, 0))

def overrideBlit(text, changeXY: bool = True) -> None:

    if changeXY:
        screen.blit(text, (20, 420))

    else:
        screen.blit(text, (25, 435))
        
    pygame.display.update()


def resetBottomRect() -> None:
    screen.blit(bottomRect, (0, 0))
    pygame.display.update()


def main_tutorial() -> tuple:

    hp = 100
    defense = 0
    mob = "goblin"
    inv = {}
    crit = None
    mobHp = 20
    mobAttk = "2 - 3"
    mobDefense = 0
    entityAttack = False
    attack = Attacking(Weapon_tuple[0], defense)

    print("tutorial!!", "=========", sep='\n')

    print(f"Encountered 'Goblin'! || Hp: {mobHp}, Attk: {mobAttk}, Def: {mobDefense}, Level: 1")
    print("Type attack to attack your opponent!")

    maxHp = hp
    maxMobHp = mobHp

    # startup
    resetBottomRect()
    # mobile compability
    pygame.draw.rect(screen, "pink", pygame.Rect((Screen_dim[0] - 75, 0), (75, 75)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    entityAttack = True

            if event.type == pygame.KEYUP:
                print('')

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)
                if 520 <= mouse_pos[0] <= 601 and 0 <= mouse_pos[1] <= 75:
                    entityAttack = True

        if entityAttack:
            attk = attack.attack_RNGESUS()
            defense = attack.defense_RNGESUS(random.randint(2, 5), attk[2])

            mobHp -= attk[0]
            crit = attk[1]

            hp -= defense[0]

            print(f'attk: {attk}')
            print(f'defense: {defense}')

            if mobHp <= 0:
                resetBottomRect()

                text = font.render('You have defeated the %s!' % mob, False,
                                   "Green")
                overrideBlit(text)

                preinv = tool.drops(mob)

                tool.insertingMobDrops(preinv, "goblin")
                time.sleep(2)

                resetBottomRect()
                text = font.render("You gained 4 xp!", False, "yellow")
                overrideBlit(text)

                time.sleep(2)

                text = font.render(f"You got {preinv}", False, "yellow")

                time.sleep(3)
                return (hp, inv)

            else:
                # print("+===========================+",
                #     f"% Rolled: {attk[2]}",
                #     f"- Lost: {defense[0]}hp",
                #     sep='\n')

                firstIter = font.render(
                    f"% Rolled: {attk[2]} Lost: {defense[0]}hp", False,
                    "yellow")

            if crit:
                # print(f"CRIT! Dealt: {attk[0]}hp",
                #         f"Your Hp: {hp}/{maxHp}",
                #         f"Enemy Hp: {mobHp}/{maxMobHp}",
                #         "+===========================+",
                #         sep='\n')

                secondIter = font.render(
                    f"CRIT! Dealt: {attk[0]}hp Your Hp: {hp}/{maxHp} Enemy Hp: {mobHp}/{maxMobHp}",
                    False, "yellow")
                entityAttack = False

            else:
                # print(f"+ Dealt: {attk[0]}hp",
                #         f"Your Hp: {hp}/{maxHp}",
                #         f"Enemy Hp: {mobHp}/{maxMobHp}",
                #         "+===========================+",
                #         sep='\n')

                secondIter = font.render(
                    f"Dealt: {attk[0]}hp Your Hp: {hp}/{maxHp} Enemy Hp: {mobHp}/{maxMobHp}",
                    False, "pink")
                entityAttack = False

            resetBottomRect()

            screen.blit(firstIter, (15, 415)) # blits the text for stuff
            screen.blit(secondIter, (15, 450))

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main_tutorial()
