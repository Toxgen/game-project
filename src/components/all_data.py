class Weapons():
    def __init__(self, damage, buy_price, sell_price, description):
        self.damage = damage
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.description = description

    def show_weapons(self):
        
Fist = Weapons(2, None, None, "Your fist")
Goblin_sword = Weapons(3, 10, 5, "A wooden, green sword")
