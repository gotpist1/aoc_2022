import string
from functools import reduce
from operator import add
from os import environ

priority_map = {}

all_chars_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
prio_list = [i for i in range(1, 53)]

for i in range(len(prio_list)):
    priority_map[all_chars_list[i]] = prio_list[i]


def get_compartments(data):
    x = len(data)
    return [data[slice(0, x // 2)], data[slice(x // 2, x)]]


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def getSolutionPart1(input_list):
    # 7674
    compartments_list = [get_compartments(data) for data in input_list]
    prio_value_list = []
    for comp_list in compartments_list:
        a = list(set(comp_list[0]) & set(comp_list[1]))
        for s in a:
            prio_value_list.append(priority_map.get(s))

    return reduce(add, prio_value_list)


def getSolutionPart2(input_list):
    # 2805
    prio_value_list = []
    elf_groups = list(chunks(input_list, 3))
    for group in elf_groups:
        a = list(set(group[0]) & set(group[1]) & set(group[2]))
        for x in a:
            prio_value_list.append(priority_map.get(x))
    return reduce(add, prio_value_list)


with open('input.txt') as f:
    file_input = [x.replace("\n", '') for x in f.readlines()]

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
