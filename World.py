from Ant import Ant


class World:
    '''

    '''
    # TODO:
    #  DONE 1. Create list of ants
    #  2. Use list of ants to create a nextGeneration function


    def __init__(self, y_columns, x_rows, numAnts):
        '''

        Parameters
        ----------
        x_rows : int
            The width of the grid (world) the ants will be contained in.
        y_columns : int
            The height of the grid.
        numAnts : int
            The number of ants in the simulation.

        '''
        self.y_columns = y_columns
        self.x_rows = x_rows
        self.numAnts = numAnts
        antList = Ant([0, 0])[numAnts]

    def nextGeneration(self):
        '''
        Updates each ant in antList, calling nextPosition on each

        Returns
        -------
        NONE
        '''