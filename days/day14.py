import common

test_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
test_input_part_2 = None
test_answer_1 = 12
test_answer_2 = 0


def parse_input(input: str):
    robots = [
        (
            int(line.split(" ")[0].split("=")[1].split(",")[0]),
            int(line.split(" ")[0].split(",")[1]),
            int(line.split(" ")[1].split("=")[1].split(",")[0]),
            int(line.split(" ")[1].split(",")[1]),
        )
        for line in input.splitlines()
    ]
    size = (101, 103)  # (101, 103)
    return robots, size


def quadrant(robots, x1, x2, y1, y2):
    return sum([1 if x1 <= p[0] < x2 and y1 <= p[1] < y2 else 0 for p in robots])


def part1(input: str):
    robots, size = parse_input(input)
    f_pos = [((r[0] + r[2] * 100) % size[0], (r[1] + r[3] * 100) % size[1]) for r in robots]
    ans = quadrant(f_pos, 0, size[0] // 2, 0, size[1] // 2)
    ans *= quadrant(f_pos, size[0] // 2 + 1, size[0], 0, size[1] // 2)
    ans *= quadrant(f_pos, 0, size[0] // 2, size[1] // 2 + 1, size[1])
    ans *= quadrant(f_pos, size[0] // 2 + 1, size[0], size[1] // 2 + 1, size[1])
    return ans


def display(robots, size):
    string = ""
    for y in range(size[1]):
        for x in range(size[0]):
            c = " "
            for r in robots:
                if r[0] == x and r[1] == y:
                    c = "*"
                    break
            string += c
        string += "\n"
    return string


def check_series(robots, l=5):
    count = 0
    for i in range(1, len(robots)):
        prev, current = robots[i - 1], robots[i]
        if prev[0] + 1 == current[0] and prev[1] == current[1]:
            count += 1
        else:
            count = 0
        if count >= l:
            return True
    return False


def part2(input: str):
    robots, size = parse_input(input)
    for s in range(0, 10000):
        print(s)
        f_pos = list(set([((r[0] + r[2] * s) % size[0], (r[1] + r[3] * s) % size[1]) for r in robots]))
        f_pos = sorted(f_pos, key=lambda p: p[0])
        f_pos = sorted(f_pos, key=lambda p: p[1])
        if check_series(f_pos):
            string = display(f_pos, size)
            if "***********" in string:
                print("-" * size[0])
                print(f"After {s} seconds :")
                print()
                print(string)
                print("-" * size[0])
                exit()
    return 0


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
