import io
import time

import numpy as np

input_ = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def get_input(prod=False):
    if prod:
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)


def process_remaining(leftover):
    inv = [mapping[value] for value in reversed(leftover)]
    score = 0
    for value in inv:
        score *= 5
        score += score_guide_2[value]

    return score


if __name__ == "__main__":
    score_guide = {")": 3,
                   "]": 57,
                   "}": 1197,
                   ">": 25137}

    score_guide_2 = {")": 1,
                     "]": 2,
                     "}": 3,
                     ">": 4}

    mapping = {"(":")",
               "[":"]",
               "{":"}",
               "<":">"}

    score = 0
    file = get_input(prod=True)
    remainder = []
    while True:
        line = file.readline()

        if not line:
            break
        line = line.strip()

        values = list(line)

        done = False
        opens = []
        for value in values:
            if value in mapping.keys():
                opens.append(value)
            else:
                last_value = opens.pop()
                if mapping[last_value] != value:
                    score += score_guide[value]
                    done = True
                    break

        if not done:
            remainder.append(values)
    print(score)

    scores = []
    for line in remainder:
        opens = []
        for value in line:
            if value in mapping.keys():
                opens.append(value)
            else:
                last_value = opens.pop()

        scores.append(process_remaining(opens))

    print(np.median(scores))


