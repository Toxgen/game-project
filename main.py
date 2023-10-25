from src.game import Game
from src.tutorial import main_tutorial


def start() -> bool:
    
    config = Game.get_obj(config=True)
    
    return config["tutorial_done?"]
    
def main():
    tut_bool = start()
    print(f"what did we get: {tut_bool}")
    if not tut_bool:
        _tutorial_return: tuple[int, str] = main_tutorial()
        entity = Game(100)
        entity.hp = _tutorial_return[0]
        entity.inv = _tutorial_return[1]
        #entity.tutorial_done = True
        entity.save_obj(config=True)
    # else:
        
if __name__ == "__main__":
    main()