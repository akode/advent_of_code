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

close = {value: key for key, value in pairs.items()}

def completion_score(completion):
    value = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    total = 0
    for item in completion:
        total = total*5 + value[item]
    return total
    
def part1():
    data = load_data()
    score = 0
    non_corrupted = []
    for line in data:
        stack = deque()
        line = line.strip()
        for item in line:
            if item in "{[<(":
                stack.append(item)
            else:
                if stack.pop() != pairs[item]:
                    score += cost[item]
                    stack.clear()
                    break
        if len(stack) != 0:
            non_corrupted.append(line)

    return score, non_corrupted

def part2(non_corrupted):
    completion_scores = []
    for line in non_corrupted:
        stack = deque()
        for item in line:
            if item in "{[<(":
                stack.append(item)
            else:
                stack.pop()
        completion = [close[item] for item in reversed(stack)]
        completion_scores.append(completion_score(completion))
    completion_scores = sorted(completion_scores)
    return completion_scores[len(completion_scores)//2]

if __name__ == "__main__":
    score, non_corrupted = part1()
    print(f"Result day 10 part 1: {score}")
    print(f"Result day 10 part 2: {part2(non_corrupted)}")
