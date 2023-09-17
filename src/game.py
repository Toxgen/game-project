import random as r
import time as t
import pickle
import signal
import logging

import modules.tools as tool

"""
Add something that allows the player to load or del save files
Add mana for wands and etc
"""
potionD = {
    "small_health_potion": [5, 5, "A small health potion, heals 5hp"], 
    "medium_health_potion": [20, 10, "A medium health potion, heals 10hp"],
    "large_health_potion": [30, 20, "A large health potion, heals for 30hp"]
}

all_weapons = {
    # default
    "fist": [2, None, None, "Your fist"],
    # goblin
    "goblin_sword": [3, 10, 5, "A wooden, green sword carved by goblins"] # [dmg+, buy, sell, description]
}

all_armors = {
    # goblin
    "goblin_chestplate": [1, ]
}

class DelayedKeyboardInterrupt:

    def __enter__(self):
        self.signal_received = False
        self.old_handler = signal.signal(signal.SIGINT, self.handler)
                
    def handler(self, sig, frame):
        self.signal_received = (sig, frame)
        print("TEST")
    
    def __exit__(self, type, value, traceback):
        signal.signal(signal.SIGINT, self.old_handler)
        if self.signal_received:
            self.old_handler(*self.signal_received)

class main:

    @staticmethod
    def save_obj(*obj, remove=False):
        """
        WARNING!!!
        DO NOT MESS AROUND WITH REMOVE
        """

        try:

            with open("data.pickle", "wb") as file:
                if remove:
                    pickle.dump("", file)

                else:
                    pickle.dump(obj, file)

        except Exception as ex:
            print("Error during pickling (Possible unsupported) (Saving obj):", ex)
            print(f"Printing obj for debugging, object: {obj}")

    @staticmethod
    def get_obj():
        try:
            with open("data.pickle", "rb") as file:
                data = pickle.load(file)
                return data
        
        except Exception as ex:
            print("Error during pickling (Possible unsupported) (Getting obj):", ex)

    @staticmethod
    def insertData() -> tuple: # this is going to take forever
        try:
            pass


        except KeyboardInterrupt as ky:
            print("Uh Oh, idk what happens here now")
            

    def __init__(self, hp, name, ccWeap, gold):
        self.hp = hp
        self.defe = 0
        self.gold = gold
        self.input = ''
        self.ccWeap = ccWeap
        self.xp_sys = [0, 4, 0]
        self.name = name
        self.inv = {}
        self.location = "woods"

    def xp(self) -> None: # maybe just change the xp into a list and enumerate it
        cc_level = self.xp_sys[0]

        self.xp_sys[0] = 0
        print(round(1.5 * (cc_level ** 1.15)))

        if round(1.5 * (cc_level ** 1.15)) <= self.xp_sys[1]:
            self.xp_sys[0] += 1
        
        while self.xp_sys[2] > round(1.5 * (self.xp_sys[0] ** 1.15) + 10):
            self.xp_sys[0] += 1
                    
        if cc_level > self.xp_sys[0]:
            print(f"Congrats! You gained {self.xp_sys[0] - cc_level}")
            
    def naming(self) -> (str | None):
        special_chara = "~!@#$%^&*()_+`{|}[]\:;<,>.?/*-'="
        c = None

        if self.name:
            print("Rename?", "Type in { yes } or { no }", sep='\n')
            while True:
                self.input = input('> ').lower().strip()
                if self.input == "yes":
                    break
                elif self.input == "no":
                    self.input = True
                    break
                else:
                    print("Please Type in { yes } or { no }", '\n')

        if self.input:
            return None

        t.sleep(0.5)
        print("Name?", "p.s. 1 - 12 characters long & no special characters", sep='\n')

        while True:
            self.name = input('> ').strip()
            if len(self.name) <= 0:
                print("Retry", '\n')
                continue
            elif len(self.name) >= 13:
                print("Retry", '\n')
                continue
            else:
                self.name.split()
                for i in self.name:
                    if self.name[i] in special_chara:
                        print("No Special Characters", '\n')
                        c = True
                if c:
                    c = False
                    continue
                else:
                    t.sleep(0.22)
                    print("Are You Sure? { yes } or { no }")

            while True:
                self.input = input('> ').lower()
                if self.input.strip() == "yes":
                    t.sleep(0.3333)
                    return str(self.name)
                elif self.input == "no":
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
            self.input = input('> ').lower()

            match self.input:

                case "help":
                    print("""The Following Commands Are:

                            'Stats': To show your stats
                            'Inventory or inv': To show your inventory
                            'Adventure or adv': To start an adventure 
                            'Switch or swi': To switch current weapon
                            """)
                    t.sleep(1.0)
                    continue

                case "stats":
                    print("WIP")
                    break

                case "inv":

                    tool.printingInv(self.inv)

                case "save":
                    data = [self.inv]
                    main.save_obj(data)

                case "adv":
                    print("WIP")
                    break

                case _:
                    print("Please type in a allowed command", '\n')
                    continue

    def attk_RNGESUS(self, current_weapon: str, defe: int) -> int:
        dice = r.randint(1, 12)
        dice2 = dice
        counter = 1.0
        
        if dice2 >= 11:
            return [round(all_weapons.get(current_weapon)[0] ** 1.75 - defe) + 2, 1, dice] # find what weapon they are currently using
        
        while dice2 >= 6:
            counter += 0.1
            if dice2 == 6:
                return [round(all_weapons.get(current_weapon)[0] ** counter - defe) + 1, 0, dice]
            dice2 -= 1

        while dice2 <= 6:
            counter -= 0.1
            if dice2 == 6: # maybe add something if only it was lower than >2 or >3
                return [round(all_weapons.get(current_weapon)[0] ** counter - defe) - 1, 0, dice]
            dice2 += 1

    def defe_RNGESUS(self, attk: int, dice: int) -> int:
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
        mob_list = tool.returnMob(self.hp, "woods") # Woods for now, but implement a system later

        mob, mobHp = mob_list[0], mob_list[1]
        mobAttk, mobDefe = [mob_list[2], mob_list[3]], mob_list[4]
            
        print(
            f"Encountered '{mob}'! || Hp: {mobHp}, Attk: {mobAttk[0]} - {mobAttk[1]}, Def: {mobDefe}")
        print("Type attack to attack your opponent!")

        maxHp = self.hp
        maxMobHp = mobHp

        while True:
            self.input = input('> ').lower()
            if self.input in ["attack", "atk", "attk", "q"]:

                attk = self.attk_RNGESUS(self.ccWeap, mobDefe)
                mobDefe = self.defe_RNGESUS(r.randint(mobAttk[0], mobAttk[1]), attk[2])

                mobHp -= attk[0]
                crit = attk[1]

                self.hp -= mobDefe[0]

                if self.hp <= 0:
                    quit("WIP")

                if mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {attk[2]}",
                          f"- Lost: {mobDefe[0]}hp", sep='\n')

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

        self.inv = tool.insertingMobDrops(preinv, self.inv, mob)
        tool.printingDrops(preinv, mob)

class starting_phase(main):
    def __init__(self):
        self.hp = 100
        self.defe = 0
        self.mob = "goblin"
        self.inv = {}
        self.location = "woods"
    
    def __enter__(self) -> list:
        print("tutorial!!", "=========", sep='\n')
        crit = None

        __mobHp = 20
        mobAttk = "2 - 3"
        __mobDefe = 0

        print(
            f"Encountered 'Goblin'! || Hp: {__mobHp}, Attk: {mobAttk}, Def: {__mobDefe}, Level: 1")
        print("Type attack to attack your opponent!")

        maxHp = self.hp
        maxMobHp = __mobHp

        while True:

            self.input = input('> ').lower()
            if self.input in ["attack", "atk", "attk", "q"]:

                __attk = super().attk_RNGESUS("fist", __mobDefe)
                __defe = super().defe_RNGESUS(r.randint(3, 7), __attk[2])

                __mobHp -= __attk[0]
                crit = __attk[1]
                
                self.hp -= __defe[0]

                if self.hp <= 0:
                    quit("ERROR 1: Died unexpected")

                if __mobHp <= 0:
                    break

                else:
                    print("+===========================+",
                          f"% Rolled: {__attk[2]}",
                          f"- Lost: {__defe[0]}hp", sep='\n')

                if crit:
                    print(f"CRIT! Dealt: {__attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {__mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
                    
                else:
                    print(f"+ Dealt: {__attk[0]}hp",
                            f"Your Hp: {self.hp}/{maxHp}",
                            f"Enemy Hp: {__mobHp}/{maxMobHp}", 
                            "+===========================+", 
                            sep='\n')
                    t.sleep(0.133)
            else:
                print("Please type in attack", '\n')
                continue

        print("You have defeated the Goblin!")

        preinv = tool.drops(self.mob)

        inv = tool.insertingMobDrops(preinv, "goblin")
        print("+=====================+",
              "You gained 4 xp!",
              "+=====================+", sep="\n")
        tool.printingDrops(preinv, "goblin")

        return [self.hp, self.inv]
              
    def __exit__(self, *exc):
        print(f'__exit__ called with: {exc!r}')

if __name__ == "__main__":
    with DelayedKeyboardInterrupt():
        for i in range(20):
            i += 1
            print(i)
            t.sleep(0.2)

    for i in range(20):
        print(i)
        t.sleep(0.11115)
    
            # data = main.get_obj()

            # if data or not data:

            #     with starting_phase() as tut:

            #         main.save_obj(tut, [0])