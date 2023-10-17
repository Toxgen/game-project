class Item():
    def __init__(self, 
                 name: str = "", 
                 description: str = "", 
                 buy: int = 0, 
                 sell: int = 0,
                 effect: int = 0): # effect is what it does
        # just change it to the bare minimum of each item rather than just forcing
        # all of the child classes to have it
        # also just run the method from the main class into the use so like
        # its better
        self.name = name
        self.description = description
        self.buy = buy
        self.sell = sell
        self.effect = effect

    def sell(self):
        pass # has to check if there is a possible shop location

    def buy(self):
        pass # has to check if there is a possible shop location
    """
    for these bottom methods just put them into their respective child classes
    """
    def equip(self):
        pass

    def unequip(self):
        pass
           
class Armor(Item):
    def __init__(self, name, description, buy, sell, effect):
        super().__init__(name, description, buy, sell, effect)

    def returnBonus(self):
        pass # just put this as a whole in an different class that has 
        # a method to find the bonus of all the armors

class Consumable(Item):
    def __init__(self, name, description, buy, sell, effect):
        super().__init__(name, description, buy, sell, effect)
        
class Weapons(Item):
    def __init__(self, name, description, buy, sell, damage):
        super().__init__(name, description, buy, sell)
        self.damage = damage