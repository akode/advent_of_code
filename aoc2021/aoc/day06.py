import collections as ct

def load_data():
    with open("./data/input6.txt") as fp:
        data = fp.read()
    return [int(iter) for iter in data.split(",")]

def part1(n_days=80):
    data = load_data()

    for _ in range(n_days):
        data = [[6,8] if fish==0 else [fish-1] for fish in data]
        data = [item for sub in data for item in sub]

    return len(data)

def cluster(data):
    counter = ct.Counter(data)
    cluster = ct.defaultdict(int)
    for age in range(9):
        cluster[age] = counter[age]
    return cluster

def update(data):
    new_data = ct.defaultdict(int)
    for age, count in data.items():
        if age == 0:
            new_data[6] += count
            new_data[8] += count
        else:
            new_data[age-1] += count
    return new_data


def part2(n_days=256):
    data = load_data()
    data = cluster(data)
    for _ in range(n_days):
        data =update(data)

    return sum(count for _, count in data.items())
    

if __name__ == "__main__":
    print(f"Result part 1: {part1()}")
    print(f"Result part 2: {part2()}")
