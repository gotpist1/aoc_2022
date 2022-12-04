from functools import reduce
from operator import add
from os import environ


def getSolutionPart1(input_list):
    # 475
    fully_contains_count = []
    s = [section_pairs.split(",") for section_pairs in input_list]
    for d in s:
        fnum = [x for x in range(int(d[0].split("-")[0]), int(d[0].split("-")[1]) + 1)]
        snum = [x for x in range(int(d[1].split("-")[0]), int(d[1].split("-")[1]) + 1)]
        result_all = all(elem in fnum for elem in snum)
        result_all_2 = all(elem in snum for elem in fnum)
        if result_all or result_all_2:
            fully_contains_count.append(True)

    return reduce(add, fully_contains_count)


def getSolutionPart2(input_list):
    # 825
    overlaps = []
    s = [section_pairs.split(",") for section_pairs in input_list]
    for d in s:
        first = d[0].split("-")
        second = d[1].split("-")
        fnum = [x for x in range(int(first[0]), int(first[1]) + 1)]
        snum = [x for x in range(int(second[0]), int(second[1]) + 1)]
        result_all = any(elem in fnum for elem in snum)
        if result_all:
            overlaps.append(True)

    return reduce(add, overlaps)


with open('input.txt') as f:
    file_input = [x.replace("\n", '') for x in f.readlines()]

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
