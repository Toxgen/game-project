#!/usr/bin/env python3

import logging

logging.basicConfig(filename='_logging/_logs.log')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

from src.game import Game
    
def main():

    game = Game()
    game.run()
    
if __name__ == "__main__":
    main()  