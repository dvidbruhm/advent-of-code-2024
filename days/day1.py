import common
import numpy as np

test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""
test_input_part_2 = None
test_answer_1 = 11
test_answer_2 = 31


def parse_input(input: str):
    locs = np.array([line.split("   ") for line in input.splitlines()], dtype=int)
    left, right = locs[:, 0], locs[:, 1]
    return left, right


def part1(input: str):
    left, right = parse_input(input)
    left.sort(), right.sort()
    return np.abs(left - right).sum()


def part2(input: str):
    left, right = parse_input(input)
    return sum([(right == le).sum() * le for le in left])


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
