import itertools
import re

import common

test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
test_input_part_2 = None
test_answer_1 = 14
test_answer_2 = 34


def parse_input(input: str):
    size = (len(input.splitlines()[0]), len(input.splitlines()))
    input = input.replace("\n", "")
    freqs = list(set(input))
    freqs.remove(".")
    antennas = {}
    for f in freqs:
        antennas[f] = [(m.start() % size[0], m.start() // size[0]) for m in list(re.finditer(f, input))]
    return antennas, size


def in_bounds(antenna, size):
    return 0 <= antenna[0] < size[0] and 0 <= antenna[1] < size[1]


def harmonics_antinodes(pair, size, stop=False):
    antenna_1, antenna_2 = pair[0], pair[1]
    dir = (antenna_2[0] - antenna_1[0], antenna_2[1] - antenna_1[1])
    nodes = [antenna_1, antenna_2] if not stop else []
    for start in [(-1, antenna_1), (1, antenna_2)]:
        current_node = (start[1][0] + start[0] * dir[0], start[1][1] + start[0] * dir[1])
        while in_bounds(current_node, size):
            nodes.append(current_node)
            current_node = (current_node[0] + start[0] * dir[0], current_node[1] + start[0] * dir[1])
            if stop:
                break
    return nodes


def all_pairs(antennas):
    return list(itertools.permutations(antennas, 2))


def part1(input: str):
    all_freqs, size = parse_input(input)
    all_antinodes = set()
    [[all_antinodes.add(a) for a in harmonics_antinodes(pair, size, stop=True)] for freq in all_freqs.keys() for pair in all_pairs(all_freqs[freq])]
    return len(all_antinodes)


def part2(input: str):
    all_freqs, size = parse_input(input)
    all_antinodes = set()
    [[all_antinodes.add(a) for a in harmonics_antinodes(pair, size)] for freq in all_freqs.keys() for pair in all_pairs(all_freqs[freq])]
    return len(all_antinodes)


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
