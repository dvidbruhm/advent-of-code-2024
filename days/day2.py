import common
import numpy as np

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
test_input_part_2 = None
test_answer_1 = 2
test_answer_2 = 4


def parse_input(input: str):
    reports = [np.array(r.split(" "), dtype=int) for r in input.splitlines()]
    return reports


def same_sign(diff):
    return np.all(diff > 0) if diff[0] > 0 else np.all(diff < 0)


def is_safe(arr):
    return same_sign(arr) and np.abs(arr).max() <= 3


def part1(input: str):
    parsed = parse_input(input)
    return sum([same_sign(np.diff(r)) and np.abs(np.diff(r)).max() <= 3 for r in parsed])


def part2(input: str):
    parsed = parse_input(input)
    safes = 0
    for r in parsed:
        if is_safe(np.diff(r)):
            safes += 1
            continue
        for i in range(len(r)):
            if is_safe(np.diff(np.delete(r, i))):
                safes += 1
                break
    return safes


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
