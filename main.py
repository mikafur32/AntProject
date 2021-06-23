import World
from graphics import *
import time

def main():
    print("")


if __name__ == "__main__":
    main()
    size_x = 1000
    size_y = 900

    world = World.World(size_x, size_y, 5)
    win = GraphWin("World", size_x, size_y) # create 1000 x 900 pixel page
    ant = Circle(Point(500, 450), 5)





    world.toString(win,ant)
    while True:
        world.nextGeneration(ant, win)
        time.sleep(0.25)

    win.close()  # Close window when done