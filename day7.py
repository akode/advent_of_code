
def load_data():
    with open("./data/input7.txt") as fp:
        data = fp.read().split(",")
    return [int(item) for item in data]

def find_min_pos(data):
    max_val = max(data)
    dist = [sum(abs(v-i) for v in data) for i in range(max_val)]
    return min(dist)

def part1():
    data = load_data()
    return find_min_pos(data)

if __name__ == "__main__":
    print(f"Day 7 part 1 result: {part1()}")
