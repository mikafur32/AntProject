import random
class Ant:
    '''
    The Ant object

    :parameter position: The object's current position in the world.
    :type position: 2d array/list


    '''


    #TODO:
        #1. add nextPosition
            #A. add randomPosition
                #a.
        #2. add Release method
            #A. Releases a "tracker" after every iteration ("life") of the simulation

    def __init__(self, position):
        self.position = position

    def nextPosition(self):
        '''

        :rtype: 2d List
        :return: the next position
        '''
