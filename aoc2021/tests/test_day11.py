import pytest
from aoc.day11 import Cavern, Octopus

steps = [
    """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""",
    """
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637
""",
    """
8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848
""",
]


small = [
    """
11111
19991
19191
19991
11111
""",
    """
34543
40004
50005
40004
34543
""",
]


def state(n, source):
    return [
        [int(item) for item in line.strip()] for line in source[n].strip().split("\n")
    ]


@pytest.mark.parametrize(
    "start,end",
    [
        (state(0, small), state(1, small)),
        (state(0, steps), state(1, steps)),
        (state(1, steps), state(2, steps)),
    ],
)
def test_step1(start, end):
    cavern = Cavern([[Octopus(i) for i in line] for line in start])
    cavern.update()

    print(cavern)
    print("\n" + "\n".join("".join(str(item) for item in line) for line in end))

    assert all(
        a.energy == b
        for line_a, line_b in zip(cavern.data, end)
        for a, b in zip(line_a, line_b)
    )

def test_is_valid_neighbor():
    cavern = Cavern([[Octopus(i) for i in line] for line in state(2, steps)])
    print(cavern.h, cavern.w)
    assert 9+1==cavern.h, "Example should exceed bounds"
    assert cavern.is_valid_neighbor(9, 1, 0, 0) == False
