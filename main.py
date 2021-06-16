import World
from graphics import *
import time

def main():
    print("")


if __name__ == "__main__":
    main()
    world = World.World(50, 50, 5)
    win = GraphWin("World", 1000, 900) # create 100 x 100 pixel page
    ant = Circle(Point(500, 450), 5)




    world.toString(win,ant)
    while True:
        world.nextGeneration(ant, win)
        time.sleep(0.25)

    win.close()  # Close window when done