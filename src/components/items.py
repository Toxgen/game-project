
potionD = {
    "small_health_potion": (5, 5, "A small health potion, heals 5hp"), # hp+, buy, description
    "medium_health_potion": (20, 10, "A medium health potion, heals 10hp"),
    "large_health_potion": (30, 20, "A large health potion, heals for 30hp")
}
class Item():
    def __init__(self, name, description, buy, sell, effect):
        self.name = name
        self.description = description
        self.buy = buy
        self.sell = sell
        self.effect = effect

class Potion(Item):
    def use(self):
        pass