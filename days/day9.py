import common

test_input = """2333133121414131402"""
test_input_part_2 = None
test_answer_1 = 1928
test_answer_2 = 2858


def parse_input(input: str):
    disk = []
    files = []
    id = 0
    for i, char in enumerate(input):
        if i % 2 == 0:
            [disk.append(chr(id)) for i in range(int(char))]
            [files.append(id) for i in range(int(char))]
            id += 1
        else:
            [disk.append(".") for i in range(int(char))]
        disk.append(" ")
        print(disk)
    return disk, files


def part1(input: str):
    disk, files = parse_input(input)
    empties = list(filter(lambda i: i is not None, [i if file == "." else None for i, file in enumerate(disk)]))
    files = sorted(files, reverse=True)[: len(empties)]
    # print(disk, files, empties)
    for i, e in enumerate(empties):
        disk[e] = files.pop(0)
    disk[-len(empties) :] = []
    # print(disk, files, empties)
    return sum([d * i for i, d in enumerate(disk)])


def parse_input_2(input):
    disk = []
    files = []
    id = 0
    for i, char in enumerate(input):
        if i % 2 == 0:
            disk.append("".join([chr(id)] * int(char)))
            id += 1
        else:
            if char == "0":
                continue
            disk.append("".join(["."] * int(char)))
    files = list(reversed(list(filter(lambda f: "." not in f and f != "", disk))))
    return disk, files


def part2(input: str):
    disk, files = parse_input_2(input)
    for x, f in enumerate(files):
        # print(f"{x}/{len(files)}", end="\r")
        len_file = len(f)
        file_i = disk.index(f)
        for j in range(file_i):
            if "." not in disk[j]:
                continue
            len_empty = len(disk[j])
            if len_file <= len_empty:
                disk[j] = f
                disk[file_i] = "." * len(f)
                if len_empty > len_file:
                    disk.insert(j + 1, "".join(["."] * (len_empty - len_file)))
                # TODO disk = ["".join(g) for k, g in groupby("".join(disk))]
                break
    # print(disk)
    disk = "".join(disk)
    # print(disk)
    return sum([ord(d) * i if d != "." else 0 for i, d in enumerate(disk)])


if __name__ == "__main__":
    common.run(part1, part2, test_input, test_answer_1, test_answer_2, test_input_part_2)
