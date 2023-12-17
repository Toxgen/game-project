class Item():

    def __init__(self, 
                 name: str = "", 
                 description: str = "", 
                 buy: int = 0, 
                 sell: int = 0): 
        
        self.name = name
        self.description = description
        self.buy = buy
        self.sell = sell
           
class Armor(Item):
    def __init__(self, name, description, buy, sell):
        super().__init__(name, description, buy, sell)

class Consumable(Item):
    def __init__(self, name, description, buy, sell, effect):
        super().__init__(name, description, buy, sell)
        self.effect = effect # increased hp or mana
        
class Weapons(Item):
    def __init__(self, name, description, buy, sell, damage):
        super().__init__(name, description, buy, sell)
        self.damage = damage