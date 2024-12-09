import itertools

import common

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
test_input_part_2 = None
test_answer_1 = 3749
test_answer_2 = 11387


def parse_input(input: str):
    lines = input.splitlines()
    equations = [(int(line.split(":")[0]), [int(num) for num in line.split(":")[1].strip().split(" ")]) for line in lines]
    return equations


def compute_equation(nums, ops):
    tot = nums[0]
    for i in range(len(ops)):
        tot = ops[i](tot, nums[i + 1])
    return tot


def all_combinations(nums, true_tot, allowed_ops):
    possibles = list(itertools.product(allowed_ops, repeat=len(nums) - 1))
    for p in possibles:
        tot = compute_equation(nums, p)
        if tot == true_tot:
            return tot
        elif tot > true_tot:
            break
    return 0


def part1(input: str):
    parsed = parse_input(input)
    return sum([all_combinations(eq[1], eq[0], [lambda a, b: a * b, lambda a, b: a + b]) for eq in parsed])


def part2(input: str):
    parsed = parse_input(input)
    return sum([all_combinations(eq[1], eq[0], [lambda a, b: a * b, lambda a, b: a + b, lambda a, b: int(f"{a}{b}")]) for eq in parsed])


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
