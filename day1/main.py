from typing import List
from day1.inputs import entries

SUM_EXPENSES = 2020


def part_one(entries: List[int]):
    for entry_1 in entries:
        for entry_2 in entries:
            if (entry_1 + entry_2) == SUM_EXPENSES:
                return entry_1 * entry_2

    return 0


def part_two(entries: List[int]):
    for entry_1 in entries:
        for entry_2 in entries:
            for entry_3 in entries:
                if (entry_1 + entry_2 + entry_3) == SUM_EXPENSES:
                    return entry_1 * entry_2 * entry_3

    return 0


print(part_one(entries))
print(part_two(entries))
