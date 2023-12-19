class Item():

    def __init__(self, 
                 name: str = "", 
                 description: str = "", 
                 buy: int = 0, 
                 sell: int = 0,

                 effect: tuple = None,
                 damage: int = None,
                 defense: int = None): 
        
        self.name = name
        self.description = description
        self.buy = buy
        self.sell = sell

        self.effect = effect
        self.damage = damage
        self.defense = defense
        
    def returnEffect(self):
        return self.effect # maybe do a if statement to check if it is potion
    
