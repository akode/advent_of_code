from collections import deque


class Octopus:
    def __init__(self, energy) -> None:
        self.energy = energy
        self.flashed = False

    def should_flash(self):
        return (self.energy > 9) & (self.flashed == False)

    def reset(self):
        self.energy = 0
        self.flashed = False

    def __repr__(self) -> str:
        return f"Octopus(energy={self.energy}, flashed={self.flashed})"


class Cavern:
    def __init__(self, data) -> None:
        self.data = data
        self.w = len(data[0])
        self.h = len(data)
        self.total_flashes = 0
        self.stack = deque()

    def increment(self):
        for y in range(self.h):
            for x in range(self.w):
                self.data[y][x].energy += 1

    def reset_energy(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.data[y][x].energy > 9:
                    self.data[y][x].reset()

    def is_valid_neighbor(self, y, dy, x, dx):
        return (
            ((dx != 0) & (dy != 0))
            & (x + dx >= 0)
            & (x + dx < self.w)
            & (y + dy >= 0)
            & (y + dy < self.h)
        )

    def get_neighbors(self, y, x):
        return (
            (x, y)
            for dy in [-1, 0, 1]
            for dx in [-1, 0, 1]
            if self.is_valid_neighbor(y, dy, x, dx) & (self.data[y][x].flashed == False)
        )

    def flash(self):
        n_flashes = 0
        for y in range(self.h):
            for x in range(self.w):
                if self.data[y][x].should_flash():
                    n_flashes += 1
                    self.data[y][x].flashed = True
                    self.stack.extend(self.get_neighbors(y, x))
        while len(self.stack) > 0:
            x, y = self.stack.pop()
            self.data[y][x].energy += 1
            if self.data[y][x].should_flash():
                n_flashes += 1
                self.data[y][x].flashed = True
                self.stack.extend(self.get_neighbors(y, x))
        return n_flashes

    def update(self):
        self.increment()
        n_flashes = self.flash()
        self.total_flashes += n_flashes
        self.reset_energy()

    def run(self, n=100):
        for i in range(n):
            self.update()
            print(f"Iteration {i}, flashes {self.total_flashes}")
            
        return self.total_flashes

    def __repr__(self) -> str:
        return "\n".join("".join(str(item.energy) for item in line) for line in self.data)


def load_data():
    with open("./data/input11.txt") as fp:
        data = fp.readlines()
    return [[Octopus(int(item)) for item in line.strip()] for line in data]


def part1():
    data = load_data()
    cavern = Cavern(data)
    total_flashes = cavern.run(100)
    return total_flashes


def part2():
    return None


if __name__ == "__main__":
    print(f"Result day 11 part 1: {part1()}")
    print(f"Result day 11 part 2: {part2()}")
