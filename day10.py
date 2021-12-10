from collections import deque

def load_data():
    with open("./data/input10.txt") as fp:
        return fp.readlines()


cost = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

pairs = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<"
}
    
def part1():
    data = load_data()
    stack = deque()
    score = 0
    corrupted = 0
    for line in data:
        line = line.strip()
        for item in line:
            if item in "{[<(":
                stack.append(item)
            else:
                if stack.pop() != pairs[item]:
                    score += cost[item]
                    corrupted += 1
                    break

        
    print(corrupted)
    return score

def part2():
    data = load_data()
    return None

if __name__ == "__main__":
    print(f"Result day 10 part 1: {part1()}")
    print(f"Result day 10 part 2: {part2()}")
