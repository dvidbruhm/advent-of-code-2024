from itertools import islice

import common
import numpy

test_input = """0 1 10 99 999"""
test_input = """125 17"""
test_input_part_2 = None
test_answer_1 = 55312
test_answer_2 = 55312


def parse_input(input: str):
    stones = input.split(" ")
    return stones


def rules(stone):
    l = len(stone)
    if stone == "0":
        return "1", None
    if l % 2 == 0:
        return stone[: l // 2], str(int(stone[l // 2 :]))
    return str(int(stone) * 2024), None


def rules_map(number_map: dict):
    map_copy = number_map.copy()
    number_map.clear()
    for key in map_copy.keys():
        amount = map_copy[key]

        l = len(str(key))
        if key == 0:
            number_map[1] = number_map.get(1, 0) + amount
        elif l % 2 == 0:
            part1, part2 = int(str(key)[: l // 2]), int(str(key)[l // 2 :])
            number_map[part1] = number_map.get(part1, 0) + amount
            number_map[part2] = number_map.get(part2, 0) + amount
        else:
            number_map[key * 2024] = number_map.get(key * 2024, 0) + amount


def first_try_slow():
    stones = parse_input(input)
    for j in range(25):
        print(j)
        stones_iter = iter(enumerate(stones))
        for i, s in stones_iter:  # enumerate(input.split(" ")):
            s1, s2 = rules(s)
            # print(i, "- ", s, s1, s2, stones)
            stones[i] = s1
            if s2:
                stones.insert(i + 1, s2)
                next(islice(stones_iter, 1, 1), None)
    return len(stones)


# Very fast method with dict
def part1(input: str):
    stones = [int(s) for s in parse_input(input)]
    number_map = {}
    for stone in stones:
        if stone in number_map.keys():
            number_map[stone] += 1
        else:
            number_map[stone] = 1
    for i in range(75):
        rules_map(number_map)
    return sum([v for k, v in number_map.items()])


# Numpy try, a lot faster than first try but far from fast enough
def part2(input: str):
    stones = numpy.array([int(i) for i in input.split(" ")])
    for n in range(75):
        mask1 = stones == 0
        mask2 = (numpy.int32(numpy.log10(stones)) + 1) % 2 == 1
        mask3 = numpy.flatnonzero(numpy.logical_not(numpy.logical_or(mask1, mask2)))
        stones = numpy.where(mask2, stones * 2024, stones)
        stones = numpy.where(mask1, 1, stones)
        div = 10 ** ((numpy.int32(numpy.log10(stones[mask3])) + 1) // 2)
        new_stones1 = stones[mask3] // div
        new_stones2 = stones[mask3] % div
        stones[mask3] = new_stones2
        stones = numpy.insert(stones, mask3, new_stones1)

    return len(stones)


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
