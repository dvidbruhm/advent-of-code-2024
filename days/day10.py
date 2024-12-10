import common
import networkx as nx
import numpy as np

test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
test_input_part_2 = None
test_answer_1 = 36
test_answer_2 = 81


def parse_input(input: str):
    hmap = np.array([[int(char) for char in line] for line in input.split("\n")])
    graph = nx.DiGraph()
    size = (len(input.splitlines()[0]), len(input.splitlines()))
    starts, ends = [], []
    for y, line in enumerate(hmap):
        for x, num in enumerate(line):
            if num == 0:
                starts.append((x, y))
            if num == 9:
                ends.append((x, y))

            graph.add_node((x, y))

            if x - 1 >= 0 and hmap[y][x - 1] - num == 1:
                graph.add_edge((x, y), (x - 1, y))
            if x + 1 < size[0] and hmap[y][x + 1] - num == 1:
                graph.add_edge((x, y), (x + 1, y))
            if y - 1 >= 0 and hmap[y - 1][x] - num == 1:
                graph.add_edge((x, y), (x, y - 1))
            if y + 1 < size[1] and hmap[y + 1][x] - num == 1:
                graph.add_edge((x, y), (x, y + 1))

    return graph, starts, ends


def part1(input: str):
    graph, starts, ends = parse_input(input)
    answer = sum([sum([nx.has_path(graph, s, e) for e in ends]) for s in starts])
    return answer


def part2(input: str):
    graph, starts, ends = parse_input(input)
    paths = [[nx.all_simple_paths(graph, s, e) for e in ends] for s in starts]
    answer = sum([sum([sum(1 for _ in p) for p in path]) for path in paths])
    return answer


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
