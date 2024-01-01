#!/usr/bin/env python3

import logging
import os

from src.game import Game
    
def main():
    path = r"C:\Users\yao\OneDrive\Documents/vscode-src\game-project"

    handler = logging.FileHandler(os.path.join(path, '_logging/_logs.log'))

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    game = Game()
    game.run()
    
if __name__ == "__main__":
    main() 