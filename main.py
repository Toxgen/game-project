#!/usr/bin/env python3

import logging

from src.game import Game
    
def main():
    logging.basicConfig(filename='_logging/_logs.log')
    game = Game()
    game.run()
    
if __name__ == "__main__":
    main()