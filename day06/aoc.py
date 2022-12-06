from os import environ


def get_key_marker(marker_length, input_file):
    for i in range(0, len(input_file)):
        key = input_file[i:i + marker_length]
        if len(set(key)) == len(key):
            return i + len(key)


def getSolutionPart1(input_list):
    # 1198
    return get_key_marker(4, input_list)


def getSolutionPart2(input_list):
    # 3120
    return get_key_marker(14, input_list)


with open('input.txt') as f:
    input_buffer = f.read()

part = environ.get('part')

if part == 'part2':
    print(getSolutionPart2(input_buffer))
else:
    print(getSolutionPart1(input_buffer))
