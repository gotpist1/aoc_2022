from os import environ


def get_key_marker(n, input_file):
    return [i + n for i in range(0, len(input_file)) if len(set(input_file[i:i + n])) == n][0]


with open('input.txt') as f:
    input_buffer = f.read()

part = environ.get('part')
if part == 'part2':
    # 3120
    print(get_key_marker(14, input_buffer))
else:
    # 1198
    print(get_key_marker(4, input_buffer))
