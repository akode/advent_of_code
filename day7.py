from functools import lru_cache

def load_data():
    with open("./data/input7.txt") as fp:
        data = fp.read().split(",")
    return [int(item) for item in data]

def find_min_pos(data):
    max_val = max(data)
    dist = [sum(abs(v-i) for v in data) for i in range(max_val)]
    return min(dist)

@lru_cache
def dist2cost(dist):
    return sum(range(1,dist+1))

def find_min_pos_p2(data):
    max_val = max(data)
    cost = [0]*max_val
    for i in range(max_val):
        for v in data:
            dist = abs(v-i)
            cost[i] += dist2cost(dist)
    return min(cost)

def part1():
    data = load_data()
    return find_min_pos(data)

def part2():
    data = load_data()
    return find_min_pos_p2(data)

if __name__ == "__main__":
    print(f"Day 7 part 1 result: {part1()}")
    print(f"Day 7 part 2 result: {part2()}")
