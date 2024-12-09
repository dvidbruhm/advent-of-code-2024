import argparse
import os
import time
from typing import Callable

import __main__


def main(part: str, part1: Callable, part2: Callable, day: str):
    with open(f"inputs/input_{day}.txt") as f:
        text = f.read()
        start = time.time()
        answer = part1(text) if part == "part1" else part2(text)
        elapsed = time.time() - start
        print(f"Answer: {answer}\nTook {elapsed} s")


def test(part: str, part1: Callable, part2: Callable, test_input: str, test_answer_1: int, test_answer_2: int, test_input_part_2: str = None):
    start = time.time()
    result = part1(test_input) if part == "part1" else part2(test_input_part_2 if test_input_part_2 else test_input)
    elapsed = time.time() - start
    answer = test_answer_1 if part == "part1" else test_answer_2
    if answer == result:
        print(f"Right answer: {answer}!\nTook {elapsed}")
    else:
        print(f"Answer: {answer}\nResult: {result}\nTook {elapsed}")


def run(part1: Callable, part2: Callable, test_input: str, test_answer_1: int, test_answer_2: int, test_input_part_2: str = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("part")
    parser.add_argument("mode")
    args = parser.parse_args()
    day = os.path.basename(__main__.__file__).split(".")[0]
    if args.mode == "test":
        test(args.part, part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
    if args.mode == "main":
        main(args.part, part1, part2, day)
