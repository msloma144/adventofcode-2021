import io
import time
from collections import Counter

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


if __name__ == "__main__":
    score_guide = {")": 1,
                   "]": 2,
                   "}": 3,
                   ">": 4}

    mapping = {"(":")",
               "[":"]",
               "{":"}",
               "<":">"}

    score = 0
    file = get_input(prod=True)
    correct = ['(', ')', '<', '>', '[', ']', '{', '}']
    while True:
        line = file.readline()
        print(line)

        if not line:
            break
        line = line.strip()

        openers = 0
        closers = 0
        incomplete = False
        bad_value = None
        values = list(line)
        done = False
        #keys, values_ = zip(*sorted(zip(Counter(values).keys(), Counter(values).values()), key=lambda x: x[0]))
        #keys = list(keys)
        #values_ = list(values_)
        #for value in values:
        #    if value in mapping:
        #        openers += 1
        #    else:
        #        closers += 1

        if openers == closers:
            opens = []
            for value in values:
                if value in mapping.keys():
                    opens.append(value)
                else:
                    last_value = opens.pop()
                    if mapping[last_value] != value:
                        score += score_guide[value]
                        break
       #for index, key in enumerate(correct):
       #    try:
       #        if key != keys[index]:
       #            keys.insert(index, correct[index])
       #            values_.insert(index, 0)
       #    except IndexError:
       #        keys.insert(index, correct[index])
       #        values_.insert(index, 0)

       #odds = values_[1::2]
       #evens = values_[::2]

       #for index in range(len(evens)):
       #    if evens[index] - odds[index] > 1:
       #        print("incomplete")
       #        print(values_)
       #        incomplete = True
       #        break

       #if not incomplete:

       #    while len(values) > 0:
       #        if len(values) == 0:
       #            break
       #        if len(line) % 2 == 1:
       #            break

       #        if values[0] == values[-1]:
       #            del values[0]
       #            del values[-1]
       #        else:
       #            bad_value = values[-1]
       #            break



    print(score)

