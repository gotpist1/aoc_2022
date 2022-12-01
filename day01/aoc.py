from functools import reduce
from operator import add
from os import environ


def getCaloriesByElf(input_list):
    return [reduce(add, elf_calories) for elf_calories in
            list(map(lambda calorie_array: [int(calorie) for calorie in calorie_array if calorie != ''],
                     [line.split("\n") for line in input_list.split("\n\n")]))]


def getSolutionPart1(input_list):
    # Answer 65912
    return max(getCaloriesByElf(input_list))


def getSolutionPart2(input_list):
    # right answer 195625
    calories_by_elf = getCaloriesByElf(input_list)
    calories_by_elf.sort(reverse=True)
    return reduce(add, calories_by_elf[0:3])


with open('input.txt', mode="r") as f:
    all_text = f.read()

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(all_text))
else:
    print(getSolutionPart1(all_text))
