import os
from typing import List


REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse_passports(raw_inputs: List[str]):
    start = 0
    passports: List[List[str]] = []
    for index, raw in enumerate(raw_inputs):
        if raw == '\n':
            passports.append(raw_inputs[start:index])
            start = index + 1

    parsed_passports: List[dict] = []
    for i in range(len(passports)):
        parsed_passport = {}
        for j in range(len(passports[i])):
            passports[i][j] = passports[i][j].strip('\n')
            sep = passports[i][j].split(' ')

            if len(sep) > 1:
                for s in sep:
                    key, value = s.split(':')
                    parsed_passport[key] = value
            else:
                key, value = passports[i][j].split(':')
                parsed_passport[key] = value

        parsed_passports.append(parsed_passport)

    return parsed_passports


def part_one(passports: List[dict]):
    valid = 0
    for passport in passports:
        if all(key in passport.keys() for key in REQUIRED_KEYS):
            valid += 1
    return valid


with open(f'{os.getcwd()}\\day4\\inputs.txt') as f:
    raw_inputs = f.readlines()


# I'm not sure why but this returns a result with 1
# less than the correct answer.  I cannot figure out
# the issue. I tried adding 1 to the answer for the heck
# of it and it was correct. Python geniuses, help me out.
print(part_one(parse_passports(raw_inputs)))
