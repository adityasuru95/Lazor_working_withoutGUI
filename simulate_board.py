# LAZOR
# simulate_board.py

import sys

# Initialize block reference information
valid_grid = ['o', 'x', 'a', 'b', 'c']
special_blocks = {
    'a': 'reflect',
    'b': 'opaque',
    'c': 'refract'
}


class Block:

    def __init__(self, ctr_x, ctr_y):
        self.ctr_x = ctr_x
        self.ctr_y = ctr_y

    def __call__(self, typ):
        self.typ = typ

    def interact(self, position, direction):

        typ = self.typ
        if typ == 'N':
            return [((position[0] + direction[0], position[1] + direction[1]), direction)]
        elif typ == 'A':
            if position[0] % 2 == 1:
                return [(position, (direction[0], -direction[1]))]
            else:
                return [(position, (-direction[0], direction[1]))]
        elif typ == 'B':
            return 'END'
        elif typ == 'C':
            if position[0] % 2 == 1:
                return [(position, (direction[0], -direction[1])), ((position[0] + direction[0], position[1] + direction[1]), direction)]
            else:
                return [(position, (-direction[0], direction[1])), ((position[0] + direction[0], position[1] + direction[1]), direction)]
        else:
            pass


class Lazor:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.path = []


def boardCheck(width, height, listOfLazors, dictOfBlocks, targetList):
    blockList = [[0 for i in range(2 * width + 1)] for j in range(2 * height + 1)]

    # Initialize all the blocks to 'N' which are normal / "let is pass" blocks
    listOfHits = []


    for i in range(width):
        for j in range(height):
            blockList[2 * j + 1][2 * i + 1] = Block(2 * j + 1, 2 * i + 1)
            blockList[2 * j + 1][2 * i + 1].typ = 'N'


    for blk in dictOfBlocks:
        ctr_x = 2 * blk[0] + 1
        ctr_y = 2 * blk[1] + 1
        blockList[ctr_y][ctr_x].typ = dictOfBlocks[blk]

    # print(blockList[7][3].typ)


    # Lazor information initialize
    for lazor in listOfLazors:
        lazor.path.append((lazor.position, lazor.direction))

        condition = False
        while condition is False:

            # cx = lazor.path[-1][0][0]
            # cy = lazor.path[-1][0][1]
            # dx = lazor.path[-1][1][0]
            # dy = lazor.path[-1][1][1]


            if lazor.path[-1][0][0] + lazor.path[-1][1][0] < 0 or lazor.path[-1][0][0] + lazor.path[-1][1][0] > 2 * width or lazor.path[-1][0][1] + lazor.path[-1][1][1] < 0 or lazor.path[-1][0][1] + lazor.path[-1][1][1] > 2 * height:
                break

            if lazor.path[-1][0][0] % 2 == 0:
                new = blockList[lazor.path[-1][0][1]][lazor.path[-1][0][0] + lazor.path[-1][1][0]].interact((lazor.path[-1][0][0], lazor.path[-1][0][1]), (lazor.path[-1][1][0], lazor.path[-1][1][1]))
            else:
                new = blockList[lazor.path[-1][0][1] + lazor.path[-1][1][1]][lazor.path[-1][0][0]].interact((lazor.path[-1][0][0], lazor.path[-1][0][1]), (lazor.path[-1][1][0], lazor.path[-1][1][1]))

            if new == 'END':
                break
            else:
                lazor.path.append(new[0])

            if len(new) == 2:
                listOfLazors.append(Lazor((new[1][0][0], new[1][0][1]), (new[1][1][0], new[1][1][1])))

            # Break out of the for loop if the lazor reaches the boundary
            if new[0][0][0] + new[0][1][0] > 2 * width or new[0][0][0] + new[0][1][0] < 0 or new[0][0][1] + new[0][1][1] > 2 * height or new[0][0][1] + new[0][1][1] < 0:
                condition = True


            # Break out of the loop if the lazor goes into an infinite loop (max points = 100)
            # if len(lazor.path) > 3:
               #  if lazor.path[-1][0] == lazor.path[-2][0] and lazor.path[-2][0] == lazor.path[-3][0]:
               #      condition = True

            if len(lazor.path) > 2 and lazor.path[-1][0] == lazor.path[-2][0] and lazor.path[-2][0] == lazor.path[-3][0]:
                condition = True

        for hits in lazor.path:
            listOfHits.append(hits[0])
        # print(len(lazor.path), "\n", lazor.path)


    # for lazor in listOfLazors:
    #   lazor.path = []

    # print("Nos of lazers: ", len(listOfLazors))

    condition = True
    for target in targetList:
        if target not in listOfHits:
            condition = False
    return condition


def get_solution(listOfDicts, w, h, lasers, dictOfBlocks, targetList):
    soln = None
    tries = 0

    listOfLazors = []
    for i in lasers:
        listOfLazors.append(Lazor((i[0], i[1]), (i[2], i[3])))

    for dictOfBlocks in listOfDicts:
        for lazor in listOfLazors:
            lazor.path = []
        tries += 1

        listOfLazors = []
        for i in lasers:
            listOfLazors.append(Lazor((i[0], i[1]), (i[2], i[3])))

        result = boardCheck(w, h, listOfLazors, dictOfBlocks, targetList)
        # print(result)
        if result:
            # print(dictOfBlocks)
            soln = dictOfBlocks
            break

    if soln is None:
        print("No possible solution for the given parameters!")
        sys.exit()

    return(soln, tries)


if __name__ == "__main__":
    pass