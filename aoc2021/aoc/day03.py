

def load_data():
    with open("data/input3.txt") as fp:
        data = fp.readlines()
    return data



def compute_most_common(data):
    n_bits = len(data[0])-1
    one_count = [0 for _ in range(n_bits)]
    for row in data:
        for bit in range(n_bits):
            one_count[bit] += int(row[bit])
    return [1 if bit >= (len(data)/2) else 0 for bit in one_count]

def compute_least_common(data):
    return [0 if bit else 1 for bit in compute_most_common(data)]

def prune_list(data, bit, bit_val):
    return list(filter(lambda item: int(item[bit])==int(bit_val), data))
    
def iterate(data, ref_func):
    n_bits = len(data[0])-1
    candidates = data.copy()
    for bit in range(n_bits):
        reference = ref_func(candidates)
        if len(candidates) == 1:
            return int(candidates[0],2)
        else:
            pruned = prune_list(candidates, bit, reference[bit])
            if len(pruned) > 0:
                candidates = pruned
    return int(candidates[0],2)

def part1():
    data = load_data()
    most_common = compute_most_common(data)
    least_common = compute_least_common(data)
    gamma = int("".join(str(bit) for bit in most_common),2)
    epsilon = int("".join(str(bit) for bit in least_common), 2)

    return gamma*epsilon

def part2():
    data = load_data()
    oxy = iterate(data, compute_most_common)
    co2 = iterate(data, compute_least_common)
    return co2*oxy


if __name__ == "__main__":
    print(f"Result day 3 part 1: {part1()}")
    print(f"Result day 3 part 2: {part2()}")
