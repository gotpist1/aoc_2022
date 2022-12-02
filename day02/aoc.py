from functools import reduce
from operator import add
from os import environ

LOST=0
DRAW=3
WON=6
ROCK_P=1
PAPER_P=2
SCISSORS_P=3

OP_R_M="A"
OP_P_M="B"
OP_S_M="C"

ME_R_M="X"
ME_P_M="Y"
ME_S_M="Z"



def getSolutionPart1(input_list):
    #
    my_scores = []
    s = [x.split(" ") for x in [y.replace("\n", '') for y in input_list]]
    for moves in s:
        op_move = moves[0]
        me_move = moves[1]
        if op_move == OP_R_M and me_move != ME_P_M and me_move != ME_R_M:
            my_scores.append(SCISSORS_P + LOST)
        elif op_move == OP_R_M and me_move == ME_P_M:
            my_scores.append(PAPER_P + WON)
        elif op_move == OP_R_M and me_move == ME_R_M:
            my_scores.append(ROCK_P + DRAW)
        elif op_move == OP_P_M and me_move != ME_P_M and me_move != ME_S_M:
            my_scores.append(ROCK_P + LOST)
        elif op_move == OP_P_M and me_move == ME_S_M:
            my_scores.append(SCISSORS_P + WON)
        elif op_move == OP_P_M and me_move == ME_P_M:
            my_scores.append(PAPER_P + DRAW)
        elif op_move == OP_S_M and me_move != ME_R_M and me_move != ME_S_M:
            my_scores.append(PAPER_P + LOST)
        elif op_move == OP_S_M and me_move == ME_R_M:
            my_scores.append(ROCK_P + WON)
        elif op_move == OP_S_M and me_move == ME_S_M:
            my_scores.append(SCISSORS_P + DRAW)

    return reduce(add, my_scores)


def getSolutionPart2(input_list):
    #

    return None


with open('input.txt') as f:
    file_input = [x for x in f.readlines()]

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
