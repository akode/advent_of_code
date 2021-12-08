import collections as ct

Example = ct.namedtuple("Example", "input output")


def load_data():
    with open("./data/input8.txt") as fp:
        data = fp.readlines()
    return [line2example(line) for line in data]


def line2example(line):
    input, output = [
        [sort(item) for item in part.strip().split(" ")] for part in line.split("|")
    ]
    return Example(input=input, output=output)


def part1():
    data = load_data()
    return sum(len(item) in {2, 3, 4, 7} for example in data for item in example.output)


def sort(string):
    return "".join(sorted(string))


class Configuration:
    def __init__(self, input):
        by_len = ct.defaultdict(list)
        for item in input:
            by_len[len(item)].append(item)

        one = by_len[2][0]
        seven = by_len[3][0]
        four = by_len[4][0]
        eight = by_len[7][0]

        self.conf = {
            one: 1,
            four: 4,
            seven: 7,
            eight: 8,
        }

        # find 9
        nine_pattern = set(four).difference(one).union(four)
        for item in by_len[6]:
            if nine_pattern.issubset(item) and item not in self.conf:
                self.conf[item] = 9
                break

        assert len(self.conf.items()) == 5, sorted(self.conf.items(), key=lambda item: item[1])

        # find 3
        for item in by_len[5]:
            if set(one).issubset(item) and item not in self.conf:
                self.conf[item] = 3
        
        assert len(self.conf.items()) == 6, sorted(self.conf.items(), key=lambda item: item[1])

        # Finding 5 and 6
        five_six_pattern = set(four).difference(one)
        for item in by_len[6]:
            if five_six_pattern.issubset(item) and item not in self.conf:
                self.conf[item] = 6
                break
        assert len(self.conf.items()) == 7, sorted(self.conf.items(), key=lambda item: item[1])
        
        for item in by_len[5]:
            if five_six_pattern.issubset(item) and item not in self.conf:
                self.conf[item] = 5
                break
        assert len(self.conf.items()) == 8, sorted(self.conf.items(), key=lambda item: item[1])

        # Finding 2
        for item in by_len[5]:
            if item not in self.conf:
                self.conf[item] = 2
                break
        assert len(self.conf.items()) == 9, sorted(self.conf.items(), key=lambda item: item[1])

        # Finding 0
        for item in by_len[6]:
            if item not in self.conf:
                self.conf[item] = 0
                break

        assert len(self.conf.items()) == 10, sorted(self.conf.items(), key=lambda item: item[1])
        assert len(set(self.conf.keys())) == 10, sorted(self.conf.items(), key=lambda item: item[1])
        assert len(set(self.conf.values())) == 10, sorted(self.conf.items(), key=lambda item: item[1])

    def decode(self, output):
        return int("".join(str(self.conf[sort(item)]) for item in output))


def process(example):
    configuration = Configuration(example.input)
    # print(configuration.conf)
    return configuration.decode(example.output)


def part2():
    """There are 4 numbers which can be determened by the number of lit segments alone:

    - len 2 => 1
    - len 3 => 7
    - len 4 => 4
    - len 7 => 8

    # Findind 9
    If we remove the 2 wires of 1 from 7 we have determined the top segment wire.
    Now we can add this wire to 4 so we obtain an incomplete 9 (bottom wire is missing). 9 is the only 6 wire number containing all these wires.

    # Finding 3
    3 is the only 5 wire number which contains all wires of 1.

    # Finding 5 and 6
    If we remove the 1 wires from the 4 wires we obtain a wire pattern which is contained only in the wires of 5 and 6.
    If the number of wires of the matched pattern is 5 then it is a 5, if it is 6 then we have a 6.

    # Finding 2 and 0
    2 and 0 are the two remaining 5 and 6 wires numbers and can be found by exclusion.

    """
    data = load_data()
    decoded = [process(example) for example in data]
    # print([item.output for item in data])
    # print(decoded)
    return sum(decoded)


if __name__ == "__main__":
    print(f"Day 8 part 1: {part1()}")
    print(f"Day 8 part 2: {part2()}")
