#%%
import collections as ct
#%%
def prep_line(line):
    a, b = line.split(" -> ")
    a = tuple(map(int, a.split(",")))
    b = tuple(map(int, b.split(",")))
    return a, b

#%%
def to_points(line):
    a, b = line
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    points = []
    if (dx == 0) & (dy == 0):
        points.append((a[0], a[1]))
    elif dx == 0:
        start = a[1] if dy > 0 else b[1]
        for y in range(abs(dy)+1):
            points.append((a[0], y + start))
    elif dy == 0:
        start = a[0] if dx > 0 else b[0]
        for x in range(abs(dx)+1):
            points.append((x + start, a[1]))
    else:
        for x, y in zip(range(abs(dx)+1), range(abs(dy)+1)):
            points.append(
                (x*(1 if dx > 0 else -1)+a[0], 
                y*(1 if dy > 0 else -1)+a[1]))

    return points

#%%
def filter_hv(line):
    a, b = line
    dx = abs(b[0] - a[0])
    dy = abs(b[1] - a[1])
    if (dx==0) | (dy==0):
        return True
    else:
        return False

#%%
def get_data():
    with open("./data/input5.txt") as fp:
        data = fp.readlines()

    return list(map(prep_line, data))

def count_overlaps(points):
    counter = ct.Counter(points)
    return sum(1 if count > 1 else 0 for _, count in counter.items())

# %%
def part1():
    lines = get_data()
    points = [item for sub in map(to_points, filter(filter_hv, lines)) for item in sub]
    return count_overlaps(points)    

def part2():
    lines = get_data()
    points = [item for sub in map(to_points, lines) for item in sub]
    return count_overlaps(points)

if __name__ == "__main__":
    print(f"Day5 part 1 result: {part1()}")
    print(f"Day5 part 2 result: {part2()}")
