from functools import reduce
from operator import add
from os import environ


def get_crates_map(input_list):
    num_crates = [list(filter(None, x)) for x in input_list if "" in x and "1" in x][0]
    num_crates_filtered = [list(filter(lambda x: x != " ", num_crates))][0]
    crates_rows = [x for x in input_list if "1" not in x and "move" not in x]
    fs = [list(filter(None, s)) for s in crates_rows]
    xl = list(filter(None, fs))
    indexes = {}
    for x in num_crates_filtered:
        indexes[int(x)] = num_crates.index(x)
    cs_map = {}
    for col, idx in indexes.items():
        cs_map[col] = [s[idx] for s in xl if len(s) >= idx]
    return cs_map


def getSolutionPart1(input_list):
    cs_map = get_crates_map(input_list)
    moves = [x.split(" ") for x in input_list if "move" in x]
    for idx, m in enumerate(moves):
        qty = int(m[1])
        fr = int(m[3])
        to = int(m[5])
        for _ in range(0, qty):
            from_crate = list(filter(lambda x: x != " ", cs_map.get(fr)))
            to_crate = list(filter(lambda x: x != " ", cs_map.get(to)))
            to_crate.insert(0, from_crate.pop(0))
            cs_map[fr] = from_crate
            cs_map[to] = to_crate
    return reduce(add, [val[0] for val in cs_map.values()])


def getSolutionPart2(input_list):
    cs_map = get_crates_map(input_list)
    moves = [x.split(" ") for x in input_list if "move" in x]
    for idx, m in enumerate(moves):
        qty = int(m[1])
        fr = int(m[3])
        to = int(m[5])
        for i, e in reversed(list(enumerate(range(0, qty)))):
            from_crate = list(filter(lambda x: x != " ", cs_map.get(fr)))
            to_crate = list(filter(lambda x: x != " ", cs_map.get(to)))
            to_crate.insert(0, from_crate.pop(i))
            cs_map[fr] = from_crate
            cs_map[to] = to_crate
    return reduce(add, [val[0] for val in cs_map.values()])


with open('input.txt') as f:
    crates_array = f.read().split("\n")

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(crates_array))
else:
    print(getSolutionPart1(crates_array))
