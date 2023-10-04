import os
import pickle
import random as r
import signal
import time as t
from os import system

import modules.tools as tool

"""
Add something that allows the player to load or del save files
Add mana for wands and etc
Add like a dictionary for if they have finished like the tutorial or something
"""

potionD = {
    "small_health_potion": (5, 5, "A small health potion, heals 5hp"), # hp+, buy, description
    "medium_health_potion": (20, 10, "A medium health potion, heals 10hp"),
    "large_health_potion": (30, 20, "A large health potion, heals for 30hp")
}

all_weapons = {
    # default
    "fist": (2, None, None, "Your fist"), # [dmg+, buy, sell, description]
    # goblin
    "goblin_sword": (3, 10, 5, "A wooden, green sword carved by goblins")
}

all_armors = {
    # defualt
    "pants": (0, None, None, "A pair of pants"), # defense, sell, buy, description
    # goblin
    "goblin_chestplate": (1, None, None, "Green chestplate")
}

class DelayedKeyboardInterrupt:

    # To stop keyboard interruptions during saving files

    def __enter__(self):
        self.signal_received = False
        self.old_handler = signal.signal(signal.SIGINT, self.handler)
                
    def handler(self, sig, frame):
        self.signal_received = (sig, frame)
    
    def __exit__(self, type, value, traceback):
        signal.signal(signal.SIGINT, self.old_handler)
        if self.signal_received:
            self.old_handler(*self.signal_received)
        
class game:

    @staticmethod
    def save_obj(*obj, remove=False, config=False):
        """
        WARNING!!!
        DO NOT MESS AROUND WITH REMOVE
        """
        
        try:
          if not config:
              with open("data.pickle", "wb") as file:
                  if remove:
                      pickle.dump("", file)

                  else:
                      pickle.dump(obj, file)
          else:
            with open("config.pickle", "wb") as file:
              if remove:
                pickle.dump("", file)

              else:
                pickle.dump(obj, file)

        except Exception as ex:
            print(f"Printing obj for debugging, object: {obj}")
            print("Error during pickling (Possible unsupported) (Saving obj):", ex)
            

    @staticmethod
    def get_obj(config=False):
        try:
          if not config:
            with open("data.pickle", "rb") as file:
                data = pickle.load(file)
                return data
              
          else:
            with open("config.pickle", "rb") as file:
                data = pickle.load(file)
                return data
        
        except Exception as ex:
            print("Error during pickling (Possible unsupported) (Getting obj):", ex)
            
    def __init__(self, hp, name=None, ccWeap="fist", gold: int = 0, xp_sys: list[int] = [1, 4], 
                 inv: list = [], location: str = "woods"):
        self.hp = hp
        self.defe = 0
        self.gold = gold
        self.player_input = ''
        self.ccWeap = ccWeap
        self.xp_sys = xp_sys # [level, xp]
        self.name = name
        self.inv = inv
        self.location = location

    def xp(self) -> list: 
        possible_XPlevels = (0, 7, 8, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 14, 14, 15, 
                             16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 24, 24, 25, 25, 25, 26, 
                             26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 30, 30, 30, 31, 31, 31, 
                             32, 32, 33, 33, 34, 34, 34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 
                             39, 40, 40, 41, 41, 42, 42, 43, 44, 44, 44, 45, 46, 46, 47, 48, 
                             48, 48, 49, 50, 51, 51, 52, 53, 53, 54, 55, 56, 56, 57, 58, 59,
                             60, 61, 62)
        
        exp = self.xp_sys[1]
        level = self.xp_sys[0]
        pre_hp = (self.xp_sys[0] * 5) + 100

        for x in possible_XPlevels[level:]:
            if exp >= x:
                level += 1
                exp -= x
            
            else:
                break
                
        self.xp_sys[1] = exp
        

        if level > self.xp_sys[0]:
            curMaxHp = (level * 5) + 100
            if level - 1 > self.xp_sys[0]:
                print(f"Congrats! You gained {level - self.xp_sys[0]} levels")
                print(f"Yay! {pre_hp}hp -> {curMaxHp}hp")
                self.hp = curMaxHp
                print(f"Next level at {self.xp_sys[1]}/{possible_XPlevels[level]}xp")
            else:
                print(f"Congrats! You gained {level - self.xp_sys[0]} level")
                print(f"Yay! {pre_hp}hp -> {curMaxHp}hp")
                self.hp = curMaxHp
                print(f"Next level at {self.xp_sys[1]}/{possible_XPlevels[level]}xp")

        self.xp_sys[0] = level

        return [self.xp_sys[0], self.xp_sys[1]]
            
    def naming(self) -> (str | None):
        special_chara = """~!@#$%^&*()_+`{|}[]\\:;<,>.?/*-'"="""

        if self.name:
            print("Rename?", "Type in { yes } or { no }", sep='\n')
            while True:
                self.player_input = input('> ')
                if self.player_input.lower() == "yes":
                    break
                elif self.player_input.lower() == "no":
                    self.player_input = True
                    break
                else:
                    print("Please Type in { yes } or { no }", '\n')

            if self.player_input:
                return None

        t.sleep(0.5)
        print("Name?", "p.s. 1 - 12 characters long & no special characters", sep='\n')

        while True:
            self.name = input('> ').strip()
            if 2 >= len(self.name) >= 13:
                print("Retry", '\n')
                continue
                
            else:
                self.name.split()
                for i in self.name:
                    if self.name[i] in special_chara:
                        print("No Special Characters", '\n')
                        continue
                        
                t.sleep(0.22)
                print("Are You Sure? { yes } or { no }")

            while True:
                self.player_input = input('> ').lower()
                if self.player_input.strip() == "yes":
                    t.sleep(0.3333)
                    return str(self.name)
                elif self.player_input == "no":
                    self.name = ''
                    print("Name?", sep='\n')
                    break
                else:
                    print("Type in either { yes } or { no }")
                    continue

    def help_ccmd(self) -> None:
        print("Type In { help } For Commands", "\n")
        t.sleep(0.5)
        while True:
            self.player_input = input('> ').lower()

            match self.player_input:

                case "help":
                    os.system("cls")
                    print("""The Following Commands Are:

                        'Stats': To show your stats
                        'Inventory or inv': To show your inventory
                        'Adventure or adv': To start an adventure 
                        'Switch or swi': To switch current weapon
                            """)
                    t.sleep(1.0)
                    continue

                case "stats":
                    os.system("cls")
                    print("WIP")
                    break

                case "inv":
                    os.system("cls")
                    tool.printingInv(self.inv)

                case "save":
                    os.system("cls")
                    data = [self.inv] # do something about this
                    game.save_obj(data)

                case "adv":
                    os.system("cls")
                    self.main_attack()
                    break

                case _:
                    print("Please type in a allowed command", '\n')

    def attk_RNGESUS(self, current_weapon: str, defe: int) -> (list | float):
        dice = r.randint(1, 12)
        dice2 = dice
        counter = 1.0
        returning = None
        print(f"defe: {defe}")
        
        if dice2 >= 11:
            returning = [round(all_weapons.get(current_weapon)[0] ** 1.75 - defe) + 2, 1, dice]
            if returning[0] <= -1:
                returning[0] = 0
                return returning 
            else:
                return returning
            
        while dice2 >= 6:
            counter += 0.1
            if dice2 == 6:
                returning = [round(all_weapons.get(current_weapon)[0] ** counter - defe) + 1, 0, dice] 
                if returning[0] <= -1:
                    returning[0] = 0
                    return returning 
                else:
                    return returning 
    
            dice2 -= 1

        while dice2 <= 6:
            counter -= 0.1
            if dice2 == 6:
                returning = [round(all_weapons.get(current_weapon)[0] ** counter - defe) - 1, 0, dice] 
                if returning[0] <= -1:
                    returning[0] = 0
                    return returning 
                else:
                    return returning 
            dice2 += 1

    def defe_RNGESUS(self, attk: int, dice: int) -> list:
        counter = 1.0
        
        if dice >= 11:
            return [round((attk ** 0.6) - (self.defe + 2))]
        
        while dice >= 6:
            counter -= 0.0325
            if dice >= 6:
                return [round((attk ** counter) - (1 + self.defe))]
            dice -= 1

        while dice < 6:
            counter += 0.03
            if dice < 6:
                return [round((attk ** counter) - (self.defe - 1))]
            dice += 1
                    
    def main_attack(self) -> None:
        crit = None
        mob_list = tool.returnMob(self.hp, self.location) # Woods for now, but implement a system later
        if not mob_list:
            print("It is not possible to attack here")
            return None
            
        mob, mobHp = mob_list[0], mob_list[1]
        mobAttk, mobDefe = [mob_list[2], mob_list[3]], mob_list[4]
        mob = "goblin"
            
        print(f"Encountered '{mob}'! || Hp: {mobHp}, Attk: {mobAttk[0]} - {mobAttk[1]}, Def: {mobDefe}")
        print("Type attack to attack your opponent!")
        
        maxHp = (self.xp_sys[0] * 5) + 100
        maxMobHp = mobHp

        while True:
            self.player_input = input('> ').lower()
            if self.player_input in ["attack", "atk", "attk", "q"]:
                # os.system("cls")

                attk = self.attk_RNGESUS(self.ccWeap, mobDefe)
                print(f"attk: {attk}")
                mobAttkacking = self.defe_RNGESUS(r.randint(mobAttk[0], mobAttk[1]), attk[2])

                mobHp -= attk[0]
                crit = attk[1]

                self.hp -= mobAttkacking[0]

                if self.hp <= 0:
                    quit("WIP")

                if mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {attk[2]}",
                          f"- Lost: {mobAttkacking[0]}hp", sep='\n')

                if crit:
                    print(f"CRIT! Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
                else:
                    print(f"+ Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
            else:
                print("Please type in attack", '\n')
                continue

        print(f"You have defeated the {mob}!")


        preinv = tool.drops(mob)

        self.inv = tool.insertingMobDrops(preinv, mob, self.inv)
        tool.printingDrops(preinv, mob)

class starting_phase(game):
    def __init__(self):
        self.hp = 100
        self.defe = 0
        self.mob = "goblin"
        self.inv = {}
        self.location = "woods"
    
    def __enter__(self) -> tuple:
        print("tutorial!!", "=========", sep='\n')
        crit = None

        mobHp = 20
        mobAttk = "2 - 3"
        mobDefe = 0

        print(
            f"Encountered 'Goblin'! || Hp: {mobHp}, Attk: {mobAttk}, Def: {mobDefe}, Level: 1")
        print("Type attack to attack your opponent!")

        maxHp = self.hp
        maxMobHp = mobHp

        while True:
            try:
                self.player_input = input('> ').lower()
            except EOFError:
                self.player_input = "attack"

            if self.player_input in ["attack", "atk", "attk", "q"]:
                os.system("cls")

                attk = super().attk_RNGESUS("fist", mobDefe)
                defe = super().defe_RNGESUS(r.randint(2, 5), attk[2])

                mobHp -= attk[0]
                crit = attk[1]
                
                self.hp -= defe[0]

                if self.hp <= 0:
                    quit("ERROR 1: Died unexpected")

                if mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {attk[2]}",
                          f"- Lost: {defe[0]}hp", sep='\n')

                if crit:
                    print(f"CRIT! Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
                    
                else:
                    print(f"+ Dealt: {attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
            else:
                print("Please type in attack", '\n')
                continue

        print("You have defeated the Goblin!")

        preinv = tool.drops(self.mob)

        tool.insertingMobDrops(preinv, "goblin")
        print("+=====================+",
              "You gained 4 xp!",
              "+=====================+", sep="\n")
        tool.printingDrops(preinv, "goblin")

        return (self.hp, self.inv)
              
    def __exit__(self, *exc) -> None:
        return None
        
def start() -> tuple: 
    data = game.get_obj()
    print(type(data))
    print(data)
    game.save_obj(remove=True)
  
    with DelayedKeyboardInterrupt():
      try:
          if not data["is_done_tutorial"]:
              print("1")
              with starting_phase() as tut:
                  game.save_obj((tut[0]), (tut[1]), {"is_done_tutorial": True})
                  game.save_obj({"is_done_tutorial": True}, config=True)
                  main = game(hp=tut[0])
                  data = game.get_obj()
            
          else:
            return () # reutne somehring like true if this came from tutorial
            # then writ wohter if state,ent comparing if they have done this

      except TypeError:
          if data == "":
              print("2")
              with starting_phase() as tut:
                  game.save_obj((tut[0]), (tut[1]))
                  game.save_obj({"is_done_tutorial": True}, config=True)
                  main = game(hp=tut[0])

def main():
    pass
if __name__ == "__main__":
    main = game(hp=100, xp_sys=[2, 1001])
    main.xp()
    main.main_attack()