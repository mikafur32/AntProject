import Ant
from graphics import *
import Cell
class World:

    # TODO
    #   Separate display and logic
    #   MVC Model view controller

    def __init__(self, x_rows, y_columns, numAnts):
        '''

        Parameters
        ----------
        x_rows : int
            The width of the grid (world) the ants will be contained in.
        y_columns : int
            The height of the grid.
        worldGrid : 2d List(Cell)
            Cell array of the locations of the ants.
            Parameters : x_rows, y_columns
        numAnts : int
            The number of ants in the simulation.
        antList : List(Ant)
            A list containing all of the ants in the simulation.
            Parameters : numAnts


        '''
        self.x_rows = x_rows
        self.y_columns = y_columns
        self.worldGrid = [[Cell.Cell() for x in range(x_rows)] for i in range(y_columns)]



        self.numAnts = numAnts
        self.antList = [Ant.Ant(x_rows / 2,y_columns / 2, self)] * numAnts # middle of the grid

    def nextGeneration(self, antObject, graphWin):
        '''Updates each ant in antList, calling nextPosition on each ant in the list.'''

        for ants in self.antList:
            self.worldGrid[int(ants.row)][int(ants.column)].hasAnt = False

            positionBefore_X = ants.row
            positionBefore_Y = ants.column # gathers positional data for the generation of the antObject

            ants.nextPosition()

            positionAfter_X = ants.row
            positionAfter_Y = ants.column

            while not self.isValidPosition(ants): #verifies the position of the ant
                ants.nextPosition()
                positionAfter_X = ants.row
                positionAfter_Y = ants.column

            ants.pastPositions.append(ants.thisWorld.worldGrid[int(ants.row)][int(ants.column)])  # adds the next position in the LinkedList

            self.worldGrid[int(ants.row)][int(ants.column)].hasAnt = True

            ############ MOVEMENT MECHANICS ############
            point = antObject.getCenter()
            point.draw(graphWin)
            ## Draw scent marker

            antObject.move(( positionBefore_X - positionAfter_X) * 5, (positionBefore_Y - positionAfter_Y) * 5)
            #Moves the ant n pixels

    def isValidPosition(self, ant):
        '''
        Verifies the position is in bounds.

        Returns
        -------
        Boolean
        '''
        x_pos = ant.row
        y_pos = ant.column

        if( x_pos < 0 or x_pos >= self.x_rows):
            return False
        if(y_pos < 0 or y_pos >= self.y_columns):
            return False
        return True


    def containsAnt(self,row,column):
        '''Verifies the presence of an ant given a row and column and returns a boolean.'''
        return self.worldGrid[row][column].hasAnt

    def toString(self,graphWin, antObject):

        antObject.draw(graphWin)










##################### NOTES #######################
"""
        incrementing 0...x to indicate the strength of the trail

        build rating of most direct path back

        set of ants map the area - know the paths they took back, thus together they have a more robust thought of the area

        w/ no info, take direct path back, 
                if intersect another ant path, know the 

            dijkstra's shortest path
        """