
def load_data():
    with open("./data/input6.txt") as fp:
        data = fp.read()
    return [int(iter) for iter in data.split(",")]

def part1(n_days=256):
    data = load_data()

    for _ in range(n_days):
        data = [[6,8] if fish==0 else [fish-1] for fish in data]
        data = [item for sub in data for item in sub]
        print(len(data))

    return len(data)
    

if __name__ == "__main__":
    print(f"Result part 1: {part1()}")
