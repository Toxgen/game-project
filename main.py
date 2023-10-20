from src.game import Game
from src.tutorial import main_tutorial


def start() -> bool:
    # Game.get_obj(remove=True)
    data = Game.get_obj()
    config = Game.get_obj(config=True)
    print(f"data: {data}")
    print(f"config: {config}")
    
    return False if data == "" else True#config["is_done_tutorial"]
    
def main():
    tut_bool = start()
    print(f"what did we get: {tut_bool}")
    if not tut_bool:
        tut = main_tutorial()
        Game.save_obj((tut[0]), (tut[1]))
        Game.save_config(is_done_tutorial=True)
        main = Game(hp=tut[0])
    # else:
        
if __name__ == "__main__":
    main()