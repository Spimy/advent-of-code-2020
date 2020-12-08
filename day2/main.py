from typing import List
from day2.inputs import policy_pass


def part_one(policy_pass: List[str]):
    valid_count = 0

    for pass_set in policy_pass:
        policy, password = pass_set.split(': ')
        ranges = policy.split('-')

        min_range = ranges[0]
        max_range, required_letter = ranges[1].split(' ')

        letter_count = 0
        for letter in password:
            if letter == required_letter:
                letter_count += 1

        if letter_count >= int(min_range) and letter_count <= int(max_range):
            valid_count += 1

    return valid_count


def part_two(policy_pass: List[str]):
    valid_count = 0

    for pass_set in policy_pass:
        policy, password = pass_set.split(': ')
        positions = policy.split('-')

        pos_1 = positions[0]
        pos_2, required_letter = positions[1].split(' ')

        ltr_pos_1 = password[int(pos_1) - 1]
        ltr_pos_2 = password[int(pos_2) - 1]
        if ltr_pos_1 != ltr_pos_2 and (ltr_pos_1 == required_letter or ltr_pos_2 == required_letter):
            valid_count += 1

    return valid_count


print(part_one(policy_pass))
print(part_two(policy_pass))
