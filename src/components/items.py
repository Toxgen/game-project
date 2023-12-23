class Item():

    def __init__(self, 
                 name: str, 
                 description: str, 
                 type: str,
                 buy: int, 
                 sell: int,

                 effect: tuple = None,
                 damage: int = None,
                 defense: int = None): 
        
        self.name = name
        self.description = description
        self.type = type

        self.buy = buy
        self.sell = sell

        self.effect = effect
        self.damage = damage
        self.defense = defense
        
    def returnEffect(self):
        if self.type == "potion":
            return self.effect
    
