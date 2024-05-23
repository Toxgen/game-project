#!/usr/bin/env python3

import logging
import os
import pathlib

from src.game import Game
    
def main():
    try:  
        path = pathlib.Path(__file__).parent.resolve()
        handler = logging.FileHandler(os.path.join(path, '_logging/_logs.log'))

    except Exception:
        logging.log(level=40, msg="Logging defining went wrong")

    finally:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
    
    game = Game()
    game.run()
    
if __name__ == "__main__":
    main()