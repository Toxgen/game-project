import os
import random
import time
from sys import exit
import pygame
from components.attacking import Attacking
from constants import weapon_list, X_pos, Y_pos
import tools as tool # make them into src.-> whatever after testing

    
pygame.init()
screen = pygame.display.set_mode((1000, 750))
font = pygame.font.Font(None, 30)

pygame.display.set_caption('Game?')
clock = pygame.time.Clock()

bottomRect = pygame.Surface((X_pos, 100))
bottomRect.fill("blue")

def overrideBlit(rectangle, text, changeXY: bool = True) -> None: # maybe make a class that can just do this
    screen.blit(rectangle, (0, Y_pos - 100))
    if isinstance(text, tuple):
        for (num, x) in enumerate(text):
            print(f"debug time || text = {text}")
            if not num:
                print(f"what is x: {x}")
                screen.blit(x, (25, 400))
                print("not num if", f"num: int = {num}")
            
            else:
                screen.blit(x, (25, 435))
                print("if num", f"num: int = {num}")

        return None

    if changeXY:
        screen.blit(text, (20, 420))
    
    else:
        screen.blit(text, (25, 435))

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
    attack = Attacking(weapon_list[0], defense)

    screen.blit

    print("tutorial!!", "=========", sep='\n')

    print(
        f"Encountered 'Goblin'! || Hp: {mobHp}, Attk: {mobAttk}, Def: {mobDefense}, Level: 1"
    )
    print("Type attack to attack your opponent!")

    maxHp = hp
    maxMobHp = mobHp
    
    # startup
    screen.blit(bottomRect, (0, Y_pos - 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    entityAttack = True

            if event.type == pygame.KEYUP:
                print('\n')

        if entityAttack:
            attk = attack.attack_RNGESUS()
            defense = attack.defense_RNGESUS(random.randint(2, 5), attk[2])

            mobHp -= attk[0]
            crit = attk[1]

            hp -= defense[0]

            if mobHp <= 0:
                text = font.render('You have defeated the %s!' % mob, False, "Green")
                overrideBlit(bottomRect, text)

                preinv = tool.drops(mob)

                tool.insertingMobDrops(preinv, "goblin")
                time.sleep(2)
                text = font.render("You gained 4 xp!", False, "yellow")
                overrideBlit(bottomRect, text)

                tool.printingDrops(preinv, "goblin")
                time.sleep(3)
                return (hp, inv)

            else:
                print("+===========================+",
                    f"% Rolled: {attk[2]}",
                    f"- Lost: {defense[0]}hp",
                    sep='\n')
                
                roll_lost = font.render(f"% Rolled: {attk[2]} Lost: {defense[0]}hp", False, "yellow")
                
                overrideBlit(bottomRect, roll_lost)

            if crit:
                print(f"CRIT! Dealt: {attk[0]}hp",
                        f"Your Hp: {hp}/{maxHp}",
                        f"Enemy Hp: {mobHp}/{maxMobHp}",
                        "+===========================+",
                        sep='\n')
                
                urhp_enhp = font.render(f"CRIT! Dealt: {attk[0]}hp Your Hp: {hp}/{maxHp} Enemy Hp: {mobHp}/{maxMobHp}", False, "yellow")

            else:
                print(f"+ Dealt: {attk[0]}hp",
                        f"Your Hp: {hp}/{maxHp}",
                        f"Enemy Hp: {mobHp}/{maxMobHp}",
                        "+===========================+",
                        sep='\n')
                
                urhp_enhp = font.render(f"Dealt: {attk[0]}hp Your Hp: {hp}/{maxHp} Enemy Hp: {mobHp}/{maxMobHp}", False, "pink")
                entityAttack = False

            # attackTuple = (roll_lost, urhp_enhp)
            # overrideBlit(bottomRect, attackTuple)
            
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main_tutorial() 