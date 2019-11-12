# Software Carpentry
# Group Project - Lazor Game
# Group 5: Aditiya Suru, Casey Zhu, Lincoln Kartchner
# initialize_board.py

import sys
import operator
from collections import Counter
from functools import reduce
from math import factorial

# Initialize block reference information
valid_grid = ['o', 'x', 'a', 'b', 'c']
special_blocks = {
    'a': 'reflect',
    'b': 'opaque',
    'c': 'refract'
}


def nperms(plist):
    '''
    '''
    num = factorial(len(plist))
    count_vals = Counter(plist).values()
    den = reduce(operator.mul, (factorial(i) for i in count_vals), 1)
    perms = num / den
    return(perms)


def readBoard():
    '''
    Reads in .bff file (filename)
    Parses for given board, including fixed blocks
    Parses for given available blocks
    Parses for lazers
    Parses for targets
    Initializes appropriate amount of each based on input numbers
    '''

    print("Welcome to the Lazor board solver!")
    bfile = input("Enter the name of the board (.bff file) you want to solve: ")
    filename = bfile.split('\\')[-1]

    # Check if file exists, open if it does
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print('Error: no such file exists')
        sys.exit()

    # Generate grid (list of lists) by checking for 'GRID START'
    initGrid = []
    start = False
    for i in f.readlines():
        if start:
            if "GRID STOP" in i:
                break
            initGrid.append(i)
        else:
            if "GRID START" in i:
                start = True

    if not start:
        print("Grid not initialized!")
        sys.exit()

    # print('Error: GRID STOP not found!')

    # Read through grid, grabbing special characters
    blocks = [None, None, None]
    lasers = []
    targets = []
    f.seek(0)
    start = False

    for i in f.readlines():
        if start:
            try:
                firstChar = i[0].upper()
            except SyntaxError:
                print("Error: non-char in grid!")

            if firstChar == '#' or firstChar == '\n' or firstChar == '\t':
                continue

            elif firstChar == 'A':
                line = ''.join(i.split())
                count = int(line[1:])
                blocks[0] = ('A', count)

            elif firstChar == 'B':
                line = ''.join(i.split())
                count = int(line[1:])
                blocks[1] = ('B', count)

            elif firstChar == 'C':
                line = ''.join(i.split())
                count = int(line[1:])
                blocks[2] = ('C', count)

            elif firstChar == 'L':
                line = i.split()
                # Initialize lazor
                x = int(line[1])
                y = int(line[2])
                dx = int(line[3])
                dy = int(line[4])
                lasers.append((x, y, dx, dy))

            elif firstChar.upper() == 'P':
                line = i.split()
                # Initialize target
                x = int(line[1])
                y = int(line[2])
                targets.append((x, y))

            else:
                print('Warning: line begins with an invalid character')
                continue
        else:
            if "GRID STOP" in i:
                start = True
    f.close()

    # Check if necessary board components are provided
    if not start:
        print("Grid not stopped!")
        sys.exit()

    if not targets:
        print("No targets were provided!")
        sys.exit()

    if not lasers:
        print("No lasers were provided!")
        sys.exit()

    if all(i is None for i in blocks):
        print("No blocks were provided!")
        sys.exit()

    # Prep grid for conversion to list
    for i, v in enumerate(initGrid):
        initGrid[i] = v.split()

    # Convert grid to single list, get num of available spaces
    openSpaces = 0
    gridAsList = []
    empty = []
    for i in range(len(initGrid)):
        for j in range(len(initGrid[0])):
            initGrid[i][j] = initGrid[i][j].strip()
            initGrid[i][j] = initGrid[i][j].lower()

            gridAsList.append(initGrid[i][j])

            if initGrid[i][j] in valid_grid:
                pass
            else:
                print(initGrid[i][j])
                print('Error: Invalid block in grid!')
                sys.exit()

            if initGrid[i][j] == 'o':
                openSpaces += 1
            if initGrid[i][j] == 'x':
                empty.append((j, i))

    # init_NS, init_EW = get_nsew_coords(initGrid)
    # Get grid width
    w = len(initGrid[0])
    h = len(initGrid)

    return (filename, initGrid, gridAsList, blocks,
            openSpaces, lasers, targets, w, h, empty)


if __name__ == "__main__":
    pass
    # # TEMPORARY SOLUTION FOR YARN_5, REPLACE WITH ACTUAL SOLUTION LATER
    # # KEEP FILE AS YARN_5 FOR NOW
    # bfile = '.\\bff_files\\yarn_5.bff'
    # filename = bfile.split('\\')[-1]
    # print('-=-' * 17)
    # print('Solving board: ' + filename)
    # t0 = time.time()

    # filename, initGrid, gridAsList, blocks, openSpaces, \
    #     lasers, targets, w, h = readBoard()
    # solnGrid = initGrid
    # plist = get_permute_list(gridAsList, blocks, openSpaces)
    # tries = generateBoards(plist, gridAsList, w)
    # tf = time.time()
    # runtime = tf - t0

    # print('Run finished. Time: %0.5f sec' % (runtime))
    # print('-=-' * 17)
    # print(initGrid)

    # text_soln(filename, initGrid, soln, tries, runtime)