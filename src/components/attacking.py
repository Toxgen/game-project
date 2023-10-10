import random as r
from all_data import Weapons

class Attacking():
    def __init__(self, current_weapon, defense):
        self.current_weapon = current_weapon
        self.defense = defense

    def attk_RNGESUS(self) -> list:
        dice = r.randint(1, 12)
        dice2 = dice
        counter = 1.0
        returning = None
        print(f"defe: {self.defense}")
        
        if dice2 >= 11:
            returning = [round(all_weapons.get(self.current_weapon)[0] ** 1.75 - self.defense) + 2, 1, dice]
            if returning[0] <= -1:
                returning[0] = 0
                return returning 
            else:
                return returning
            
        while dice2 >= 6:
            counter += 0.1
            if dice2 == 6:
                returning = [round(all_weapons.get(self.current_weapon)[0] ** counter - self.defense) + 1, 0, dice] 
                if returning[0] <= -1:
                    returning[0] = 0
                    return returning 
                else:
                    return returning 
    
            dice2 -= 1

        while dice2 <= 6:
            counter -= 0.1
            if dice2 == 6:
                returning = [round(all_weapons.get(self.current_weapon)[0] ** counter - self.defense) - 1, 0, dice] 
                if returning[0] <= -1:
                    returning[0] = 0
                    return returning 
                else:
                    return returning 
            dice2 += 1

    def defe_RNGESUS(self, attk: int, dice: int) -> list:
        counter = 1.0
        
        if dice >= 11:
            return [round((attk ** 0.6) - (self.defense + 2))]
        
        while dice >= 6:
            counter -= 0.0325
            if dice >= 6:
                return [round((attk ** counter) - (1 + self.defense))]
            dice -= 1

        while dice < 6:
            counter += 0.03
            if dice < 6:
                return [round((attk ** counter) - (self.defense - 1))]
            dice += 1