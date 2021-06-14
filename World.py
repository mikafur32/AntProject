import Ant
from graphics import *
import Cell
class World:


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
        self.worldGrid = [[Cell() for x in range(x_rows)] for i in range(y_columns)]
        """
        incrementing 0...x to indicate the strength of the trail
        
        build rating of most direct path back
        
        set of ants map the area - know the paths they took back, thus together they have a more robust thought of the area
        
        w/ no info, take direct path back, 
                if intersect another ant path, know the 
            
            dijkstra's shortest path
        """
        #TODO
        #   scent value +100 est , decrement
        #   RULES FOR ANTS

        self.numAnts = numAnts
        self.antList = [Ant(x_rows / 2,y_columns / 2 )] * numAnts # middle of the grid

    def nextGeneration(self):
        '''Updates each ant in antList, calling nextPosition on each ant in the list.'''

        for ants in self.antList:
            self.worldGrid[int(ants.row)][int(ants.column)].hasAnt = False
            currentAntPostion = ants.getCurrentPosition

            ants.nextPosition()
            while not self.isValidPosition(ants):
                ants.pastPositions.remove(ants.pastPositions.size - 1) #remove last entry
                ants.nextPosition()

            self.worldGrid[int(ants.row)][int(ants.column)].hasAnt = True

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

    def __str__(self):
        '''A Conway's Game of Life inspired row x column grid containing "live" cells/ants and "non-living" cells.'''
        string = ""
        for row in range(self.x_rows):
            for column in range(self.y_columns):
                if self.containsAnt(row,column):
                    string += "\u2588" + "\u2588"
                else:
                    string += "--"
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