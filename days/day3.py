import re

import common

test_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
test_input_part_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
test_answer_1 = 161
test_answer_2 = 48


def parse_input(input: str):
    return input


def part1(input: str):
    parsed = parse_input(input)
    muls = [m[4:-1].split(",") for m in re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", parsed)]
    ans = sum([int(m[0]) * int(m[1]) for m in muls])
    return ans


def part2(input: str):
    parsed = parse_input(input)
    muls = [m.span() for m in re.finditer("mul\([0-9]{1,3},[0-9]{1,3}\)", parsed)]
    dos = [m.start() for m in re.finditer("do\(\)", parsed)]
    donts = [m.start() for m in re.finditer("don't\(\)", parsed)]
    active = True
    current_i = 0
    ans = 0
    for start, end in muls:
        current_i = start
        if dos and dos[0] < current_i:
            active = True
            dos.pop(0)
        if donts and donts[0] < current_i:
            active = False
            donts.pop(0)
        if active:
            nums = parsed[start + 4 : end - 1].split(",")
            ans += int(nums[0]) * int(nums[1])
    return ans


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
