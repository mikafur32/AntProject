from World import World
from Ant import Ant

def main():
    print("")


if __name__ == "__main__":
    main()
    world = World( 10,10,1)
    i = 0
    while(i < 9):
        i += 1
        print(str(world))
        world.nextGeneration()

