from functools import reduce
from operator import add
from os import environ


def get_range_arrays(sections):
    for d in sections:
        fnum = [x for x in range(int(d[0].split("-")[0]), int(d[0].split("-")[1]) + 1)]
        snum = [x for x in range(int(d[1].split("-")[0]), int(d[1].split("-")[1]) + 1)]
        yield fnum, snum

def getSolutionPart1(input_list):
    # 475
    sections = [section_pairs.split(",") for section_pairs in input_list]
    ranged_arrays = list(get_range_arrays(sections))
    fully_contains_count = [True for fnum, snum in ranged_arrays if all(elem in fnum for elem in snum) or all(elem in snum for elem in fnum)]
    return reduce(add, fully_contains_count)


def getSolutionPart2(input_list):
    # 825
    sections = [section_pairs.split(",") for section_pairs in input_list]
    ranged_arrays = list(get_range_arrays(sections))
    overlaps = [True for fnum, snum in ranged_arrays if any(elem in fnum for elem in snum)]
    return reduce(add, overlaps)


with open('input.txt') as f:
    file_input = [x.replace("\n", '') for x in f.readlines()]

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
