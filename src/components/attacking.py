import random as r


class Attacking():
    def __init__(self, current_weapon, defense):
        self.current_weapon = current_weapon
        self.defense = defense

    def attack_RNGESUS(self) -> list[int]:
        dice = r.randint(1, 12)
        dice2 = dice
        counter = 1.0
        returning = [0]
        
        if dice2 >= 11:
            returning = [round(pow(self.current_weapon.damage, 1.75) 
                               - self.defense) + 2, 1, dice]
            if returning[0] <= -1:
                returning[0] = 0
                return returning 
            else:
                return returning
            
        while dice2 >= 6:
            counter += 0.1
            if dice2 == 6:
                returning = [round(pow(self.current_weapon.damage, counter)
                                   - self.defense) + 1, 0, dice] 
                if returning[0] <= -1:
                    returning[0] = 0
                    return returning 
                else:
                    return returning 
    
            dice2 -= 1

        while dice2 <= 6:
            counter -= 0.1
            if dice2 == 6:
                returning = [round(pow(self.current_weapon.damage, counter) 
                                   - self.defense) - 1, 0, dice] 
                if returning[0] <= -1:
                    returning[0] = 0
                    return returning 
                else:
                    return returning
            dice2 += 1

    def defense_RNGESUS(self, attk: int, dice: int) -> list[int]:
        counter = 1.0
        
        if dice >= 11:
            return [round(pow(attk, 0.6) - (self.defense + 2))]
        
        while dice >= 6:
            counter -= 0.0325
            if dice >= 6:
                return [round(pow(attk, counter) - (self.defense + 1))]
            dice -= 1

        while dice < 6:
            counter += 0.03
            if dice < 6:
                return [round(pow(attk, counter) - (self.defense - 1))]
            dice += 1