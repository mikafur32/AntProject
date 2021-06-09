from Ant import Ant
from graphics import *

class World:


    def __init__(self, y_columns, x_rows, numAnts):
        '''

        Parameters
        ----------
        x_rows : int
            The width of the grid (world) the ants will be contained in.
        y_columns : int
            The height of the grid.
        worldGrid : 2d List(Boolean)
            Boolean array of the locations of the ants.
            Parameters : x_rows, y_columns
        numAnts : int
            The number of ants in the simulation.
        antList : List(Ant)
            A list containing all of the ants in the simulation.
            Parameters : numAnts

            dim_row = 2
dim_columns = 2

output = [[0 for x in range(dim_columns)] for i in range(dim_row)]
        '''
        self.y_columns = y_columns
        self.x_rows = x_rows
        self.worldGrid = [[False for x in range(x_rows)] for i in range(y_columns)]
        self.numAnts = numAnts
        self.antList = [Ant(x_rows / 2,y_columns / 2 )] * numAnts# middle of the grid

    def nextGeneration(self):
        '''Updates each ant in antList, calling nextPosition on each ant in the list.'''
        #TODO
        # What happens if more than one ant is in the cell?
        for ants in self.antList:
            self.worldGrid[int(ants.row)][int(ants.column)] = False
            ants.nextPosition()
            self.worldGrid[int(ants.row)][int(ants.column)] = True

    def containsAnt(self,row,column):
        '''Verifies the presence of an ant given a row and column.'''
        return self.worldGrid[row][column]

    def __str__(self):
        '''A Conway's Game of Life inspired row x column grid containing "live" cells/ants and "non-living" cells.        '''
        string = ""
        for row in range(self.x_rows):
            for column in range(self.y_columns):
                if self.containsAnt(row,column):
                    string += "\u2588" + "\u2588"
                else:
                    string += "  "
            string += "\n"
        return string


''' GRAPHICS
    def toString(self):
        win = GraphWin("My Circle", 100, 100)
        c = Circle(Point(50,50), 10)
        c.draw(win)
        win.getMouse() # Pause to view result
        win.close()    # Close window when done
                                                                                    
'''