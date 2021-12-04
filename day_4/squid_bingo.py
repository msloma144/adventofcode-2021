import io
import time
import numpy as np
import sys

input_ = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def get_input(prod=False):
    if prod:
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)


def check_win_condition(board):
    # for diagonal checking
    #if np.diag(board).sum() == -5:
    #    return True

    #if np.diag(np.fliplr(board)).sum() == -5:
    #    return True

    hor = board.sum(axis=0)
    if -5 in hor:
        return True

    vert = board.sum(axis=1)
    if -5 in vert:
        return True

    return False


def process_board(board, numbers_drawn, full_process=False):
    board_ = np.array(board, dtype=np.int)

    moves_needed = 0
    moves_tallied = 0
    for number in numbers_drawn:
        moves_needed += 1
        index = np.where(board_ == number)
        if len(index) != 0 and index[0].size != 0:
            board_[index] = -1
            moves_tallied += 1

            if check_win_condition(board_):
                if full_process:
                    sum_of_unmarked = board_.sum() + moves_tallied
                    return moves_needed, sum_of_unmarked, int(number)
                break

    return moves_needed, board


if __name__ == "__main__":
    FIND_BEST_BOARD = True
    start_time = time.time()
    numbers_drawn = []
    board = []
    best_score = sys.maxsize * 2 + 1 if FIND_BEST_BOARD else -sys.maxsize - 1
    best_board = None

    file = get_input(prod=True)
    first_line = True
    while True:
        line = file.readline()

        if not line:
            break
        line = line.strip()

        if first_line:
            first_line = False
            numbers_drawn = [int(value) for value in line.split(",")]
        else:
            if line != "":
                board.append(line.split())

        if len(board) == 5:
            moves_needed, board_ = process_board(board, numbers_drawn)
            if FIND_BEST_BOARD:
                if moves_needed < best_score:
                    best_score = moves_needed
                    best_board = board_
            else:
                if moves_needed > best_score:
                    best_score = moves_needed
                    best_board = board_
            board = []

    file.close()

    if best_board is not None:
        moves_needed, sum_of_unmarked, number = process_board(best_board, numbers_drawn, full_process=True)
        print(f"Final Score: {sum_of_unmarked * number}")

    print(f"Time (s): {time.time()-start_time}")