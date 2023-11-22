#!/usr/bin/env python3

from src.game import Game
from src.tutorial import main_tutorial


def start() -> bool:
    
    config = Game.get_obj(config=True)

    if not config["tutorial_done?"]:
        _tut: tuple[int, str] = main_tutorial()
        entity = Game(100)
        entity.hp = _tut[0]
        entity.inv = _tut[1]
        entity.config["tutorial_done?"] = True
        entity.save_obj(both=True)
        return True
    
    else:
        return Game.get_obj(), Game.get_obj(config=True)
    
def main():
    if isinstance(start(), bool):
        pass
    
    # else:
    #     entity = Game()

if __name__ == "__main__":
    main()

# just make the background of the scence
# then just check where the player is 