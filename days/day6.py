import re

import common

test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
test_input_part_2 = None
test_answer_1 = 41
test_answer_2 = 6

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def move_fast(pos, dir_i, obstacles: list):
    d = dirs[dir_i]
    obstacles.sort(key=lambda o: d[0] * o[0] + d[1] * o[1])
    i = 1 if dir_i in [1, 3] else 0
    obstacle = list(filter(lambda o: o[i] == pos[i] and d[(i + 1) % 2] * o[(i + 1) % 2] > d[(i + 1) % 2] * pos[(i + 1) % 2], obstacles))
    if not obstacle:
        return None, None
    obstacle = obstacle[0]
    next_pos = (obstacle[0] - d[0], obstacle[1] - d[1])
    dir_i = (dir_i + 1) % len(dirs)
    return next_pos, dir_i


def move(pos, dir_i, obstacles):
    # up (0, -1)
    # ri (1, 0)
    # do (0, 1)
    # le (-1, 0)
    next_pos = (pos[0] + dirs[dir_i][0], pos[1] + dirs[dir_i][1])
    while next_pos in obstacles:
        dir_i = (dir_i + 1) % len(dirs)
        next_pos = (pos[0] + dirs[dir_i][0], pos[1] + dirs[dir_i][1])
    return next_pos, dir_i


def parse_input(input: str):
    size = (len(input.splitlines()[0]), len(input.splitlines()))
    input = input.replace("\n", "")
    obstacles = [(m.start() % size[0], m.start() // size[0]) for m in list(re.finditer("#", input))]
    start_pos = (input.find("^") % size[0], input.find("^") // size[0])
    return start_pos, obstacles, size


def get_visited(current_pos, obstacles, size):
    visited = {current_pos}
    history = []
    current_dir_i = 0
    while 0 <= current_pos[0] < size[0] and 0 <= current_pos[1] < size[1]:
        current_pos, current_dir_i = move(current_pos, current_dir_i, obstacles)
        visited.add(current_pos)
        h = (current_pos, current_dir_i)
        if h in history:
            return None
        history.append(h)
    if current_pos[0] in (-1, 10) or current_pos[1] in (-1, 10):
        visited.remove(current_pos)
    return visited


def get_visited_fast(current_pos, obstacles, size):
    visited = {current_pos}
    history = []
    current_dir_i = 0
    while 0 <= current_pos[0] < size[0] and 0 <= current_pos[1] < size[1]:
        current_pos, current_dir_i = move_fast(current_pos, current_dir_i, obstacles)
        if not current_pos:
            return visited
        visited.add(current_pos)
        h = (current_pos, current_dir_i)
        if h in history:
            return None
        history.append(h)
    if current_pos[0] in (-1, 10) or current_pos[1] in (-1, 10):
        visited.remove(current_pos)
    return visited


def part1(input: str):
    current_pos, obstacles, size = parse_input(input)
    visited = get_visited(current_pos, obstacles, size)
    return len(visited)


def part2(input: str):
    current_pos, obstacles, size = parse_input(input)
    visited = get_visited(current_pos, obstacles, size)
    visited.remove(current_pos)
    sum = 0
    for i, new_obs in enumerate(visited):
        new_obstacles = [*obstacles, new_obs]
        if not get_visited_fast(current_pos, new_obstacles, size):
            sum += 1
    return sum


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
