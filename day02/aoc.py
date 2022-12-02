from functools import reduce
from operator import add
from os import environ

scores_map = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

actual_scores_map = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}


def getSolutionPart1(input_list):
    #13682
    my_scores = []
    s = [x.split(" ") for x in [y.replace("\n", '') for y in input_list]]
    for moves in s:
        my_scores.append(scores_map.get(f"{moves[0]} {moves[1]}"))
    return reduce(add, my_scores)


def getSolutionPart2(input_list):
    #12881
    my_scores = []
    s = [x.split(" ") for x in [y.replace("\n", '') for y in input_list]]
    for moves in s:
        my_scores.append(actual_scores_map.get(f"{moves[0]} {moves[1]}"))
    return reduce(add, my_scores)


with open('input.txt') as f:
    file_input = [x for x in f.readlines()]

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
