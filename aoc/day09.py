import collections as ct
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    with open("./data/input9.txt") as fp:
        return [list(line.strip()) for line in fp.readlines()]


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


def first_region(regions, key):
    if regions[key] in regions:
        return first_region(regions, regions[key])
    else:
        return regions[key]


def part2():
    data = load_data()
    print("\n".join("".join(line) for line in data)+"\n")
    img = np.array(data, dtype=np.float32)
    w = len(data[0])
    h = len(data)
    regions = {}
    max_region = 0
    for y in range(h):
        for x in range(w):
            if data[y][x] == "9":
                data[y][x] = "X"
            else:
                if x==0:
                    l = "X"
                else:
                    l = data[y][x-1]
                    
                if y==0:
                    u = "X"
                else:
                    u = data[y-1][x]
                    
                if (l != "X") & (u != "X"):
                    if l != u:
                        # merge regions
                        regions[l] = u

                    data[y][x] = l
                elif (u != "X"):
                    data[y][x] = u
                elif (l != "X"):
                    data[y][x] = l
                else:
                    data[y][x] = max_region
                    max_region += 1

    regions = {key: first_region(regions, key) for key in regions.keys()}
    assert len(set(regions.keys()).intersection(set(regions.values()))) == 0
    print(regions)
    for y in range(h):
        for x in range(w):
            val = data[y][x]
            if val in regions:
                data[y][x] = regions[val]
    
    assert len(data[0]) == w
    assert len(data) == h
    print(img)

    plt.imshow(img, cmap="gray")  
    plt.savefig('input.png')  
    print("\n".join(line.__repr__() for line in data ))
    regions_counter = ct.Counter(item for line in data for item in line)
    print(regions_counter.most_common(4)[1:])
    return reduce(lambda a,b: a*b, (count for _, count in regions_counter.most_common(4)[1:]))


if __name__ == "__main__":
    print(f"Result day 9 part 1: {part1()}")
    print(f"Result day 9 part 2: {part2()}")
