import collections as ct

Example = ct.namedtuple("Example", "input output")

def load_data():
    with open("./data/input8.txt") as fp:
        data = fp.readlines()
    return [
         line2example(line)
    for line in data ]

def line2example(line):
    input, output = [part.strip().split(" ") for part in line.split("|")]
    return Example(input=input, output=output)

def part1():
    data = load_data()
    return sum(len(item) in {2, 3, 4, 7} for example in data for item in example.output)

if __name__ == "__main__":
    print(f"Day 7 part 1: {part1()}")
