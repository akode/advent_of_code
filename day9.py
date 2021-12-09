
def load_data():
    with open("./data/input9.txt") as fp:
        return [line.strip() for line in fp.readlines()]


def risk(x, y, data):
    return 1 + int(data[y][x])

def is_low_point(x, y, w, h, data):
    self = int(data[y][x])
    adjacents = [int(data[d][x]) for d in [y-1, y+1] if (d >= 0) & (d < h)] + \
        [int(data[y][d]) for d in [x-1, x+1] if (d >= 0) & (d < w)]
    return all(adj > self for adj in adjacents)

def part1():
    data = load_data()
    w = len(data[0])
    h = len(data)

    total_risk = 0
    for x in range(w):
        for y in range(h):
            if is_low_point(x, y, w, h, data):
                total_risk += risk(x, y, data)

    return total_risk

def part2():
    pass


if __name__ == "__main__":
    print(f"Result day 9 part 1: {part1()}")
    print(f"Result day 9 part 1: {part2()}")
