import random as r
import time as t

import modules.tools as tool

import modules.sql_data as sql

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
    # goblin
    "goblin_sword": [3, 10, 5, "A wooden, green sword carved by goblins"] # [dmg+, buy, sell, description]
}

all_armors = {
    # goblin
    "goblin_chestplate": [1, ]
}
class main:

    @staticmethod
    def sqlQuery(connection,
                      add=False,
                      grab=False,
                      tut=False):
        if tut:
            for i in range: 
                x = sql.execute_query(connection=connection, 
                                      query=f"""select exists(select * from stats where id = {i+1});""")
                if not x:
                    query=f"""insert into stats (id, name, gold, cc_weap, tut_booean, hp)
                    values ({i+1}, "", 0, "", null, 100)"""
                    return sql.execute_query(connection=connection, query=query)

        if grab:
            query="""select * from stats;"""

        if add:
            query=""""""

        return sql.execute_query(connection=connection, query=query, fetch=True)
        

    def __init__(self, hp, name, ccWeap, gold):
        __check = sql.execute_query(connection=connection, query="select tut_check from stats;", noText=True)
        if not __check:
            pass # work on this tmw
        self.hp = hp
        self.gold = gold
        self.input = ''
        self.ccWeap = ccWeap
        self.xp_sys = [0, 4, 0]
        self.name = name
        self.inv = {}
        self.location = "woods"

    def xp(self) -> None:
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

                case "adv":
                    print("WIP")
                    break

                case _:
                    print("Please type in a allowed command", '\n')
                    continue

    def attk_RNGESUS(self, input: str, defe: int) -> int:
        dice = r.randint(1, 12)
        dice2 = dice
        counter = 1.0
        
        if dice2 >= 11:
            return [round(self.weapDict.get(input) ** 1.75 - defe) + 2, 1, dice]
        
        while dice2 >= 6:
            counter += 0.1
            if dice2 == 6:
                return [round(self.weapDict.get(input) ** counter - defe) + 1, 0, dice]
            dice2 -= 1

        while dice2 <= 6:
            counter -= 0.1
            if dice2 == 6: # maybe add something if only it was lower than >2 or >3
                return [round(self.weapDict.get(input) ** counter - defe) - 1, 0, dice]
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

    def selectWeapon(self) -> None:
        possibleWeapList = ["fist", "goblin_sword"] # maybe just throw this into a database or something to that 
        # extent with other varibles similar to this, for organization
        sel_wep = list(self.weapDict.keys())
        for xy in self.weapDict:
            for y in possibleWeapList:
                if sel_wep[xy] == possibleWeapList[y]:
                    if xy == 0:
                        print("____________________________", '\n')
                    print(f"{sel_wep[xy]}")
                    if xy+1 == len(self.weapDict):
                        print("____________________________")
                        break
                    
    def main_attack(self) -> None:
        crit = None
        mob_list = tool.returnMob(self.hp, "woods") # Woods for now, but implement a system later

        mob = mob_list[0]
        mobHp = mob_list[1]
        mobAttk = [x for x in mob_list if 2 in x if 3 in x] # no need for list comprehension here !
        mobDefe = mob_list[4]
            
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

                if len(attk) == 2:
                    mobHp -= attk[0]
                    crit = attk[1]
                else:
                    mobHp -= attk[0]

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

        print("You have defeated the Goblin!") # akso gotta change this cause u dont always be defeating goblins


        preinv = tool.counting_drop(tool.drops(mob), mob)

        self.inv = tool.insertingMobDrops(preinv, self.inv, mob)
        tool.printingDrops(preinv, mob)

class starting_phase(main):
    def __init__(self):
        self.hp = 100
        self.defe = 0
        self.mob = "goblin"
        self.inv = {}
        self.location = "woods"


    def __repr__(self):
        return "Tutorial!"


    def start(self) -> list:
        crit = 0

        __mobHp = 20
        mobAttk = "2 - 3"
        __mobDefe = 0

        print(
            f"Encountered 'Goblin'! || Hp: {__mobHp}, Attk: {mobAttk}, Def: {__mobDefe}, Level: 1")
        print("Type attack to attack your opponent!")

        maxHp = self.hp
        maxMobHp = __mobHp

        while True:
            """
            when it crits, it doesn't show CRIT!!!
            """
            self.input = input('> ').lower()
            if self.input in ["attack", "atk", "attk", "q"]:

                __attk = super().attk_RNGESUS("fist", __mobDefe)
                __defe = super().defe_RNGESUS(r.randint(2, 3), __attk[2])


                if len(__attk) == 2:
                    __mobHp -= __attk[0]
                    crit = __attk[1]
                else:
                    __mobHp -= __attk[0]
                    
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

        preinv = tool.counting_drop(tool.drops(self.mob), self.mob)

        super().insertingMobDrops(preinv, "goblin")
        print("+=====================+",
              "You gained 4 xp!",
              "+=====================+", sep="\n")
        tool.printingDrops(preinv, self.mob)

        return [self.hp, preinv]

if __name__ == "__main__":
    t = t.time()

    try:

        connection = sql.create_server_connection("localhost", "root", sql.pw)
        connection = sql.create_db_connection("localhost", "root", sql.pw, "rpg_stats")
        player_stats = main.sqlQuery(connection, grab=True) # print out something the database and its users and use it
        main.sqlQuery(connection=connection, )

        if not player_stats[4]:

             tutorial = starting_phase()

             print(tutorial, "=========", sep='\n')
             _main_return = tutorial.start()
             main = main(_main_return[0], )
             main.sqlQuery(connection, autoSend=True) # add something here that updates the data into sql

    except KeyboardInterrupt:
        connection.close()
        quit(KeyboardInterrupt)

    connection.close()
