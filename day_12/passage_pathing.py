import io
import time
from collections import Counter
import numpy as np

input_ = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""



input_ = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

#input_ = """start-A
#start-b
#A-c
#A-b
#b-d
#A-end
#b-end"""

def get_input(prod=False):
    if prod:
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)


def read_file(file):
    transitions = {}

    while True:
        line = file.readline()
        if not line:
            break
        start, end = line.strip().split("-")
        if start not in transitions:
            transitions[start] = []
        transitions[start].append(end)

        if end not in transitions:
            transitions[end] = []
        transitions[end].append(start)

    file.close()
    return transitions


def is_safe(current_path, new_node):
    if IS_PART_2:
        return is_safe_prt2(current_path, new_node)

    if new_node[0] == new_node[0].lower():
        if new_node in current_path:
            return False

    return True


def is_safe_prt2(current_path, new_node):
    small_values = []
    double_allowed = True
    for value in current_path:
        if value[0] == value[0].lower():
            if value not in small_values:
                small_values.append(value)
            else:
                double_allowed = False

    if new_node[0] == new_node[0].lower():
        if new_node in small_values and not double_allowed:
            return False

    return True


def go_deeper(current_path):
    current_node = current_path[-1]
    to_explore = transitions.get(current_node, [])
    possible_paths = []
    if current_node == "end":
        return [current_path]

    for new_node in to_explore:
        if new_node != "start" and is_safe(current_path, new_node):
            temp_path = list(current_path)
            temp_path.append(new_node)
            paths = go_deeper(temp_path)
            for path in paths:
                possible_paths.append(path)

    return possible_paths


if __name__ == "__main__":
    start_time = time.time()
    file = get_input(prod=True)
    IS_PART_2 = True
    transitions = read_file(file)

    paths = []
    current_path = ["start"]
    possible_paths = go_deeper(current_path)
    #for path in possible_paths:
    #    print(path)
    print(len(possible_paths))
    print(f"time: {time.time() - start_time}")





