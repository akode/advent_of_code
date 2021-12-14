
#%%
class Board:
    def __init__(self, data) -> None:
        self.data = data
        self.marks = [[0 for _ in r] for r in data]
        self.won = False

    def check(self, number):
        if self.won:
            return False
        else:
            new_mark = self.mark_number(number)
            if new_mark:
                if self.bingo():
                    self.won = True
                    return True
            else:
                return False

    def mark_number(self, number):
        return_val = False
        for row_idx, row in enumerate(self.data):
            try:
                col_idx = row.index(number)
                self.marks[row_idx][col_idx] = 1
                return_val = True
            except ValueError:
                pass
        return return_val

    def bingo(self):
        return self.row_bingo() or self.col_bingo()

    def row_bingo(self):
        for r in self.marks:
            if sum(r) == 5:
                return True
        return False

    def col_bingo(self):
        for c in zip(*self.marks):
            if sum(c) == 5:
                return True
        return False

    def __repr__(self) -> str:
        return self.data.__repr__()

    def compute_score(self, last_number):
        sum_of_unmarked = 0
        for r, mr in zip(self.data, self.marks):
            for c, mc in zip(r, mr):
                if mc == 0:
                    sum_of_unmarked += c

        return last_number * sum_of_unmarked
                 

# %%
def build_boards(board_data):
    boards = []
    board = []
    for line in board_data:
        if line == "\n":
            boards.append(Board(board))
            board = []
        else:
            board.append(list(map(int, line.split())))
    return boards

# %%
def run_game_p1(number_seq, boards):
    for num in number_seq:
        for board in boards:
            if board.check(num):
                return board.compute_score(num)

def run_game_p2(number_seq, boards):
    n_boards = len(boards)
    n_winns = 0
    for num in number_seq:
        for board in boards:
            if board.check(num):
                n_winns +=1
                if n_winns == n_boards:
                    return board.compute_score(num)
#%%
def prepare_game():
    with open("./data/input4.txt") as fp:
        data = fp.readlines()

    number_seq = map(int, data[0].split(","))
    boards = build_boards(data[2:])
    return number_seq, boards


if __name__ == "__main__":
    number_seq, boards = prepare_game()
    winner = run_game_p1(number_seq, boards)
    print(f"Part 1 winning score: {winner}")
    number_seq, boards = prepare_game()
    winner = run_game_p2(number_seq, boards)
    print(f"Part 2 winning score: {winner}")

