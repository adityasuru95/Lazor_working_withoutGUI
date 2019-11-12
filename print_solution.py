# Software Carpentry
# Lazor Project
# Group 5

'''
This file is responsible for printing the solution board
The result is a .txt file containing the answer
'''

from copy import deepcopy
import datetime


def text_soln(filename, initGrid, soln, tries, possible, runtime):
    '''
    Write the solution board to a file with some other information
    **Parameters**
        filename: string
            The name of the board we are solving
        initGrid: list
            A list of lists; the given empty problem board
        soln: dictionary
            A dictionary containing the positions of the pieces
            for the solution board. Keys are the coordinates,
            values are the block type at the coordinates
        tries: int
            The number of tries it took to find the answer
        possible: int
            The number of possible boards that could have been
            made from the inputs
        runtime: float
            The amount of time it took to get the answer
    **Returns**
        NOTHING
    '''

    fname = filename.split('.')[0]

    solnGrid = deepcopy(initGrid)
    for i in soln.keys():
        solnGrid[i[1]][i[0]] = soln[i]

    f = open(fname + '_solution.txt', 'w')

    f.write('Software Carpentry Lazor Project - Group 5\n')
    f.write(str(datetime.datetime.now()))
    f.write('\nPuzzle: ' + fname + '\n \n')

    f.write('Given board: \n')
    for i in initGrid:
        line = ' '.join(i)
        line = line + '\n'
        f.write(line)

    f.write('\nSolution board: \n')
    for i in solnGrid:
        line = ' '.join(i)
        line = line + '\n'
        f.write(line)

    f.write('\n%d guesses were made out of a possible %d boards.\n' % (tries, possible))
    f.write('Finding this solution took %f seconds.\n' % (runtime))
    f.write('Thanks for playing!\n')


if __name__ == "__main__":
    pass