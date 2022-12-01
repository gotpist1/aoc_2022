from functools import reduce
from operator import add
from os import environ


def getCaloriesByElf(input_list):
    int_list = list(map(lambda x: int(x.replace('\n', '')) if x != "\n" else 'x', input_list))
    size = len(int_list)
    idx_list = [idx + 1 for idx, val in enumerate(int_list) if val == "x"]
    result = [int_list[i: j] for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]
    calories_by_elf = [reduce(add, [int(x) for x in val if x != 'x']) for val in result]
    return calories_by_elf

def getSolutionPart1(input_list):
    # Answer 65912
    return max(getCaloriesByElf(input_list))


def getSolutionPart2(input_list):
    # right answer 195625
    calories_by_elf = getCaloriesByElf(input_list)
    calories_by_elf.sort(reverse=True)
    return reduce(add, calories_by_elf[0:3])


with open('input.txt') as f:
    file_input = [x for x in f.readlines()]

print('Python')
part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(file_input))
else:
    print(getSolutionPart1(file_input))
