import os
import re

import common
import numpy as np

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
test_input_part_2 = None
test_answer_1 = 18
test_answer_2 = 9
day = os.path.basename(__file__).split(".")[0]


def count_matches(input, word):
    return sum([len(re.findall(word, "".join(row))) for row in input])


def parse_input(input):
    return np.array([[char for char in line] for line in input.split("\n")])


def to_diag(input_2d):
    return [np.diag(input_2d, k) for k in range(-len(input_2d) + 1, len(input_2d))]


def part1(input: str):
    word = "XMAS"
    input_2d = parse_input(input)
    horizontal = count_matches(input_2d, word) + count_matches(np.flip(input_2d), word)
    vertical = count_matches(input_2d.transpose(), word) + count_matches(np.flip(input_2d).transpose(), word)
    diag1 = count_matches(to_diag(input_2d), word) + count_matches(to_diag(np.flip(input_2d)), word)
    diag2 = count_matches(to_diag(np.flip(input_2d, 1)), word) + count_matches(to_diag(np.flip(np.flip(input_2d), 1)), word)
    return horizontal + vertical + diag1 + diag2


def check_x_mas(w):
    is_xmas = w[0][0] == "M" and w[0][2] == "S" and w[1][1] == "A" and w[2][0] == "M" and w[2][2] == "S"
    return 1 if is_xmas else 0


def part2(input: str):
    parsed = parse_input(input)
    windows = np.lib.stride_tricks.sliding_window_view(parsed, (3, 3))
    tot = 0
    for i in range(windows.shape[0]):
        for j in range(windows.shape[1]):
            win = windows[i][j]
            tot += check_x_mas(win)
            tot += check_x_mas(np.rot90(win))
            tot += check_x_mas(np.rot90(np.rot90(win)))
            tot += check_x_mas(np.rot90(np.rot90(np.rot90(win))))
    return tot


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
