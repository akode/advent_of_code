import collections as ct

def prep_replaces(item):
    pattern, insert = item.split(" -> ")
    return pattern, [pattern[0] + insert, insert + pattern[1]]

def split_seq(string):
    return [string[i:i+2] for i in range(len(string)-1)]

def combine_seq(items):
    return items[0] + "".join(item[1:] for item in items[1:])

def load_data():
    with open("./data/input14.txt") as fp:
        data = fp.read()
    start_seq, replaces = data.split("\n\n")
    return start_seq, dict(prep_replaces(item) for item in replaces.strip().split("\n"))

def part1(n=10):
    seq, replaces = load_data()
    seq = ct.Counter(split_seq(seq))

    for i in range(n):
        print(f"Iteration {i}; Length {len(seq)}", end="\r")
        seq = [rep for item in seq for rep in replaces.get(item, [item])]

    seq = combine_seq(seq)
    counts = ct.Counter(seq)
    counts = counts.most_common()
    return counts[0][1] - counts[-1][1]


def part2(n=40):
    seq, replaces = load_data()
    first_pair = seq[:2]

    seq = ct.Counter(split_seq(seq))

    for i in range(n):
        print(f"Iteration {i}; Length {len(seq)}", end="\r")
        new_seq = ct.defaultdict(int)
        first_pair = replaces.get(first_pair, [first_pair])[0]
        for pair, count in seq.items():
            for rep in replaces.get(pair, [pair]):
                new_seq[rep] += count
        seq = new_seq 

    counts = ct.defaultdict(int)
    for pair, count in seq.items():
        counts[pair[1]] += count

    counts[first_pair[0]] += 1
    counts = sorted(counts.items(), key=lambda x: -x[1])
    return counts[0][1] - counts[-1][1]


if __name__ == "__main__":
    print(f"Result day 14 part 1: {part1()}")
    print(f"Result day 14 part 2: {part2()}")
