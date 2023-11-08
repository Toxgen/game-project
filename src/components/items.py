class Item():
    
    _possible_locations = (
        "blacksmith",
    )

    def __init__(self, 
                 name: str = "", 
                 description: str = "", 
                 buyCost: int = 0, 
                 sellCost: int = 0): 
        
        self.name = name
        self.description = description
        self.buyCost = buyCost
        self.sellCost = sellCost

    def sell(self, location) -> (True | False):
        if location not in Item._possible_locations:
            return False

    def buy(self, location) -> (True | False):
       if location not in Item._possible_locations:
           return False
       
           
class Armor(Item):
    def __init__(self, name, description, buy, sell):
        super().__init__(name, description, buy, sell)

    def equip(self):
        pass

    def unequip(self):
        pass

    def returnBonus(self):
        pass # just put this as a whole in an different class that has 
        # a method to find the bonus of all the armors

class Consumable(Item):
    def __init__(self, name, description, buy, sell, effect):
        super().__init__(name, description, buy, sell)
        self.effect = effect # increased hp or mana
        
class Weapons(Item):
    def __init__(self, name, description, buy, sell, damage):
        super().__init__(name, description, buy, sell)
        self.damage = damage
    
    def equip(self):
        pass