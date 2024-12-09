import itertools
from functools import cmp_to_key

import common

test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
test_input_part_2 = None
test_answer_1 = 143
test_answer_2 = 123


def parse_input(input: str):
    rules = [(int(r.split("|")[0]), int(r.split("|")[1])) for r in input.split("\n\n")[0].split("\n")]
    seqs = [[int(i) for i in s.split(",")] for s in input.split("\n\n")[1].split("\n")]
    all_pairs = [list(itertools.combinations(seq, 2)) for seq in seqs]
    return rules, seqs, all_pairs


def part1(input: str):
    rules, seqs, all_pairs = parse_input(input)
    sum = 0
    for i, pairs in enumerate(all_pairs):
        for pair in pairs:
            if (pair[1], pair[0]) in rules:
                break
        else:
            sum += seqs[i][len(seqs[i]) // 2]
    return sum


def get_bad_seqs(rules, seqs, all_pairs):
    bad_seqs = []
    for i, pairs in enumerate(all_pairs):
        for pair in pairs:
            if (pair[1], pair[0]) in rules:
                bad_seqs.append(seqs[i])
                break
    return bad_seqs


def part2(input: str):
    rules, seqs, all_pairs = parse_input(input)
    bad_seqs = get_bad_seqs(rules, seqs, all_pairs)
    sum = 0
    for seq in bad_seqs:
        good_seq = sorted(seq, key=cmp_to_key(lambda a, b: -1 if (a, b) in rules else 0))
        sum += good_seq[len(seq) // 2]
    return sum


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
