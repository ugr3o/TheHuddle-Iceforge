import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from game.game import Game

if __name__ == "__main__":
    Game().iniciar()
