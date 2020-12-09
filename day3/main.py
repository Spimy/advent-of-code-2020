import os
from typing import List
from functools import reduce


def part_one(field: List[str], right=3, down=1):
    tree_count = 0
    current_pos = right

    for index in range(0, len(field), down):
        if (index + down) >= len(field):
            continue

        row = field[index + down]
        if row[current_pos % len(row)] == '#':
            tree_count += 1

        current_pos += right

    return tree_count


def part_two(field: List[str]):
    options = [
        {'right': 1, 'down': 1},
        {'right': 3, 'down': 1},
        {'right': 5, 'down': 1},
        {'right': 7, 'down': 1},
        {'right': 1, 'down': 2}
    ]
    results = [part_one(field, **option) for option in options]
    final = reduce(lambda acc, result: acc * result, results)
    return final


with open(f'{os.getcwd()}\\day3\\inputs.txt', 'r') as f:
    field = [line.strip() for line in f]


print(part_one(field))
print(part_two(field))
