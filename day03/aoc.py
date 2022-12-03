import string
from functools import reduce
from operator import add
from os import environ

all_chars_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
prio_list = [i for i in range(1, 53)]
priority_map = {all_chars_list[i]: prio_list[i] for i in range(len(prio_list))}


def get_compartments(data):
    return [data[slice(0, len(data) // 2)], data[slice(len(data) // 2, len(data))]]


def getSolutionPart1(input_list):
    # 7674
    return reduce(add, [priority_map.get(s[0]) for s in [list(set(comp_list[0]) & set(comp_list[1])) for comp_list in
                                                         [get_compartments(data) for data in input_list]]])


def getSolutionPart2(input_list):
    # 2805
    return reduce(add, [priority_map.get(s[0]) for s in
                        [list(set(group[0]) & set(group[1]) & set(group[2])) for group in
                         [input_list[i:i + 3] for i in range(0, len(input_list), 3)]]])


with open('input.txt') as f:
    file_input = [x.replace("\n", '') for x in f.readlines()]

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
