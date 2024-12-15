from collections import namedtuple

import common

test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
test_input_part_2 = None
test_answer_1 = 480
test_answer_2 = 0


Point = namedtuple("Point", "X Y")
Machine = namedtuple("Machine", "A B P")


def parse_input(input: str, add_zeros=False):
    machines = []
    for m in input.split("\n\n"):
        i = m.split("\n")
        added_zeros = 10000000000000 if add_zeros else 0
        machines.append(
            Machine(
                Point((int(i[0][12:].split(",")[0])), int(i[0].split("+")[-1])),
                Point(int((i[1][12:].split(",")[0])), int(i[1].split("+")[-1])),
                Point(added_zeros + int(i[2][9:].split(",")[0]), added_zeros + int(i[2].split("=")[-1])),
            )
        )
    return machines


def solve(machines):
    answer = 0
    for i, m in enumerate(machines):
        nB = (m.A.Y * m.P.X - m.A.X * m.P.Y) / (m.A.Y * m.B.X - m.A.X * m.B.Y)
        nA = (m.P.X - m.B.X * nB) / m.A.X
        if not nA.is_integer() or not nB.is_integer():
            print(f"Machine {i} has no solution.")  # nA:{nA},nB:{nB} -> {m}")
            continue
        print(f"Machine {i} solution: nA:{nA},nB:{nB}")
        answer += 3 * nA + nB

    return int(answer)


def part1(input: str):
    machines = parse_input(input)
    answer = solve(machines)
    return answer


def part2(input: str):
    machines = parse_input(input, add_zeros=True)
    answer = solve(machines)
    return answer


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
