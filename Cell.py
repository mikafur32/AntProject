from Ant import Ant
import World
from graphics import *

class Cell:
    def __init__(self, currentAnts = None, scentConcentration = 0, ):
        self.currentAnts = currentAnts
        self.hasAnt = currentAnts != None
        self.scentConcentration = scentConcentration

        '''
        Parameters
        ----------
        hasAnt : boolean
            Determines if the cell contains an ant in this generation.
        scentConcentration : int
            The concentration of scent in the current cell. A scale 0-100.
            Higher the concentration, the greater the probability the ant will follow.
        '''

