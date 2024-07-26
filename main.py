#!/usr/bin/env python3

import logging
import os
import pathlib
from sys import argv

from src.game import Game
     
def main():
    try:  
        path = pathlib.Path(__file__).parent.resolve()
        handler = logging.FileHandler(os.path.join(path, '_logging/_logs.log'))

    except Exception as e:
        logging.log(level=40, msg="Logging defining went wrong")
        raise e

    finally:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)

    if (len(argv) > 1 and argv[1].lower() == "true"):
        debug = True
    
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
    # alt + x to run a file