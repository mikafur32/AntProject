import random
from LinkedLists import Node, DLL
import World

class Ant:
    '''
    The Ant object

    Parameters
    ----------
    x : int
        The object's current x position in the world.
    y : int
        The object's current y position in the world.

    '''

    # TODO:
    #  1. add nextPosition
    #  2. add Release method (release "chemical" marker)
    #       A. Releases a "tracker" after every iteration ("life") of the simulation
    #

    def __init__(self, row, column, thisWorld: World, pastPositions = None):
        self.row = row
        self.column = column
        self.thisWorld = thisWorld
        self.pastPositions = DLL()
        self.pastPositions.append(Node([thisWorld.worldGrid[int(self.row)][int(self.column)]]))

    def nextPosition(self):
        '''
        Generates a random next position on the grid from 0-7,
        updates the position attribute of the ant,
        and appends the position to the end of pastPositions.

        Returns
        -------
        NONE
        '''
        nextPosition = random.randint(0, 7)



        #(+1, -1)(+1, 0)(+1, +1)
        if nextPosition == 0:
            self.row += 1
            self.column += -1
        if nextPosition == 1:
            self.row += 1
            self.column += 0
        if nextPosition == 2:
            self.row += 1
            self.column += +1

        #(0, -1)  (0, 0)  (0, +1)
        if nextPosition == 3:
            self.row += 0
            self.column += -1
        if nextPosition == 4:
            self.row += 0
            self.column += 1

        #(-1, -1) (-1, 0) (-1, +1)
        if nextPosition == 5:
            self.row += -1
            self.column += -1
        if nextPosition == 6:
            self.row += -1
            self.column += 0
        if nextPosition == 7:
            self.row += -1
            self.column += 1
        self.pastPositions.append(self.thisWorld.worldGrid[int(self.row)][int(self.column)]) #adds the next position in the LinkedList
        self.releaseScent

    def releaseScent(self):
        self.pastPositions.tail.scentConcentration += 10


'''
        lst[rows][columns(location within the row)]
            - list containing rows, so the first dimension is the numbering of the rows

        1. 0 1 2...
        2. 0 1 2...
                      (which row you're in, which column you're in)
          1   0 1 2   (+1, -1) (+1, 0) (+1, +1)
          0   3 o 4   (0, -1)  (0, 0)  (0, +1)
    row  -1   5 6 7   (-1, -1) (-1, 0) (-1, +1)
             -1 0 1
              column
            o = current position
        '''