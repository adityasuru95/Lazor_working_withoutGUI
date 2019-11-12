from sympy.utilities.iterables import multiset_permutations
from copy import deepcopy

# Initialize block reference information
valid_grid = ['o', 'x', 'a', 'b', 'c']
special_blocks = {
    'a': 'reflect',
    'b': 'opaque',
    'c': 'refract'
}


def get_permute_list(gridAsList, blocks, openSpaces):
    '''
    '''
    permute_list = []
    for i in blocks:
        if i is not None:
            for j in range(i[1]):
                permute_list.append(i[0].upper())

    for i in range(openSpaces - len(permute_list)):
        permute_list.append('o')

    return(permute_list)


def generateBoards(plist, gridAsList, w):
    '''
    Comments go here
    '''

    listOfDicts = []
    for i in multiset_permutations(plist):
        dictOfBlocks = {}
        temp = deepcopy(gridAsList)
        index = 0

        for j in range(len(temp)):
            if temp[j] == 'o':
                temp[j] = i[index]
                index += 1
        # print(temp)

        mat = [temp[i:i+w] for i in range(0, len(temp), w)]
        # print(mat)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                cell = mat[i][j].lower()
                if cell in special_blocks.keys():
                    dictOfBlocks[(j, i)] = cell.upper()
        listOfDicts.append(dictOfBlocks)
        # print(dictOfBlocks)
    return(listOfDicts)


if __name__ == "__main__":
    pass