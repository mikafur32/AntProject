from Ant import Ant


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
        '''
        self.y_columns = y_columns
        self.x_rows = x_rows
        self.worldGrid = [x_rows][y_columns]
        self.numAnts = numAnts
        self.antList = Ant([x_rows / 2,y_columns / 2 ])[numAnts] # middle of the grid

    def nextGeneration(self):
        '''Updates each ant in antList, calling nextPosition on each ant in the list.'''
        #TODO
        # What happens if more than one ant is in the cell?
        for ants in self.antList:
            self.worldGrid[ants.row][ants.column] = False
            ants.nextPosition()
            self.worldGrid[ants.row][ants.column] = True

    def containsAnt(self,row,column):
        '''Verifies the presence of an ant given a row and column.'''
        return self.worldGrid[row][column]

    def __str__(self):
        '''A Conway's Game of Life inspired row x column grid containing "live" cells/ants and "non-living" cells.        '''
        for row in self.x_rows:
            for column in self.y_columns:
                if self.containsAnt(row,column):
                    print("\u2588" + "\u2588", end="")
                else:
                    print("  ", end="")
            print("\n")

        '''
        private static void printGrid(World world)
        {
            for (int row = 0; row < world.getHeight(); row++)
            {
                for (int column = 0; column < world.getWidth(); column++)
                {
                    System.out.print((world.getCell(row, column))
                        ? ("\u2588" + "\u2588")
                        : "  ");
                }
                System.out.println();
            }
        }
        '''