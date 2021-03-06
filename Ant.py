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
        concentrations = self.getScentConcentration()
        total = concentrations[0] + concentrations[1] + concentrations[2] + concentrations[3] + concentrations[4] + concentrations[5] + concentrations[6] + concentrations[7]

        nextPosition = random.choices([0,1,2,3,4,5,6,7], [concentrations[0] / total, concentrations[1] / total, concentrations[2] / total,
                                                          concentrations[3] / total, concentrations[4] / total, concentrations[5] / total,
                                                          concentrations[6] / total, concentrations[7]/ total], 1)
        # Weighted probability



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
        self.releaseScent

    def releaseScent(self):
        self.pastPositions.tail.scentConcentration += 10

    def getScentConcentration(self):
        '''
        Querys the world for the surrounding cells' scentConcentration value.
        Returns
        -------
        The eight surrounding cells scent value.
        '''

        return {0: self.thisWorld.worldGrid(self.row + 1, self.column -1).scentConcentration, 1:self.thisWorld.worldGrid(self.row + 1, self.column).scentConcentration,
                            2:self.thisWorld.worldGrid(self.row + 1, self.column + 1).scentConcentration, 3:self.thisWorld.worldGrid(self.row + 0, self.column - 1).scentConcentration,
                            4:self.thisWorld.worldGrid(self.row + 0, self.column + 1).scentConcentration, 5:self.thisWorld.worldGrid(self.row - 1, self.column - 1).scentConcentration,
                            6:self.thisWorld.worldGrid(self.row - 1, self.column - 0).scentConcentration, 7:self.thisWorld.worldGrid(self.row - 1, self.column + 1).scentConcentration}





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