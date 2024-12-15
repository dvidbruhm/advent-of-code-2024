from collections import deque

import common
import numpy as np

test_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
test_input = """AAAA
BBCD
BBCC
EEEC"""
test_input_part_2 = None
test_answer_1 = 1930
test_answer_2 = 1206


def parse_input(input: str):
    return np.array([[char for char in line] for line in input.split("\n")])


def get_group(start, garden, size):
    group = garden[start[1], start[0]]
    # print(group, start)
    queue = deque([start])
    visited = [start]

    while len(queue) > 0:
        node = queue.popleft()
        # print(node)
        right = (node[0] + 1, node[1])
        left = (node[0] - 1, node[1])
        up = (node[0], node[1] - 1)
        down = (node[0], node[1] + 1)

        if right[0] < size[0] and garden[right[1], right[0]] == group:
            if right not in visited:
                queue.append(right)
                visited.append(right)
        if left[0] >= 0 and garden[left[1], left[0]] == group:
            if left not in visited:
                queue.append(left)
                visited.append(left)
        if up[1] >= 0 and garden[up[1], up[0]] == group:
            if up not in visited:
                queue.append(up)
                visited.append(up)
        if down[1] < size[1] and garden[down[1], down[0]] == group:
            if down not in visited:
                queue.append(down)
                visited.append(down)

    # print(visited)
    return visited


def get_perim(visited):
    perim = 0
    for x, y in visited:
        perim += 1 if (x + 1, y) not in visited else 0
        perim += 1 if (x - 1, y) not in visited else 0
        perim += 1 if (x, y + 1) not in visited else 0
        perim += 1 if (x, y - 1) not in visited else 0
    return perim


def get_num_sides(visited):
    print(visited)
    # visited = sorted(visited, key=lambda v: v[1])
    # visited = sorted(visited, key=lambda v: v[0])
    # print(visited)
    perim_points = set()
    for x, y in visited:
        if (x + 1, y) not in visited:
            perim_points.update([(x + 1, y), (x + 1, y + 1)])
        if (x - 1, y) not in visited:
            perim_points.update([(x, y), (x, y + 1)])
        if (x, y + 1) not in visited:
            perim_points.update([(x, y + 1), (x + 1, y + 1)])
        if (x, y - 1) not in visited:
            perim_points.update([(x, y), (x + 1, y)])
    print(perim_points)
    perim_points = sorted(list(perim_points), key=lambda v: v[1])
    perim_points = sorted(perim_points, key=lambda v: v[0])
    print(perim_points)
    return 0


def part1(input: str):
    garden = parse_input(input)
    size = (len(garden[0]), len(garden))
    visited = []
    total = 0
    for y in range(size[1]):
        for x in range(size[0]):
            pos = (x, y)
            if pos in visited:
                continue
            v = get_group(pos, garden, size)
            area = len(v)
            perim = get_perim(v)

            visited = visited + v
            total += area * perim

    return total


def part2(input: str):
    garden = parse_input(input)
    size = (len(garden[0]), len(garden))
    visited = []
    total = 0
    for y in range(size[1]):
        for x in range(size[0]):
            pos = (x, y)
            if pos in visited:
                continue
            v = get_group(pos, garden, size)
            area = len(v)
            print("-----new group-----")
            nb_sides = get_num_sides(v)

            visited = visited + v
            total += area * nb_sides

    return total


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
