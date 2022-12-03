def prep_fold(item):
    axis, pos = item.split("=")
    return 0 if axis[-1]=="x" else 1, int(pos)

def prep_pattern(item):
    x,y = item.split(",")
    return [int(x), int(y)]

def load_data():
    with open("./data/input13.txt") as fp:
        pattern, instructions = fp.read().strip().split("\n\n")
    return [prep_pattern(item) for item in pattern.split("\n")], [prep_fold(item) for item in instructions.split("\n")]

def convert_point(item, axis, pos):
    if item[axis] > pos:
        item[axis] = 2*pos-item[axis]
    return item

def print_pattern(pattern):
    w = max(item[0] for item in pattern)+1
    h = max(item[1] for item in pattern)+1
    pp = [[" " for _ in range(w)] for _ in range(h)]
    for i in pattern:
        pp[i[1]][i[0]] = "0"
    print("\n".join("".join(str(i) for i in line) for line in pp))

def part1():
    pattern, instructions = load_data()
    new_pattern = pattern
    axis, pos = instructions[0]
    new_pattern = [convert_point(item, axis, pos) for item in new_pattern]
    
    return len(set(tuple(item) for item in new_pattern))

def part2():
    pattern, instructions = load_data()
    new_pattern = pattern
    for axis, pos in instructions:
        new_pattern = [convert_point(item, axis, pos) for item in new_pattern]
    
    print_pattern(new_pattern)
    return len(set(tuple(item) for item in new_pattern))

if __name__ == "__main__":
    print(f"Result day 13 part 1: {part1()}")
    print(f"Result day 13 part 2: {part2()}")
