from Ant import Ant
from World import World
from graphics import *


def main():
    print("")


if __name__ == "__main__":
    main()
    world = World(10, 10, 1)
    win = GraphWin("World", 100, 100) # create 100 x 100 pixel page



    while(True):

        print(str(world))
        world.nextGeneration()

    win.close()  # Close window when done