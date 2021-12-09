import io
import time

input_ = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
"""

# input_ = """dab eafb ab | cdfeb fcadb cdfeb cdbaf"""

input_ = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""

input_ = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def get_input(prod=False):
    if prod:
        return open("input.txt", "r")
    else:
        return io.StringIO(input_)


def print_mapping(possible=True):
    print("Mapping...")
    if possible:
        for key in mapping.keys():
            print(f"{key}: {mapping[key]['possible']}")
    else:
        for key in mapping.keys():
            print(f"{key}: {mapping[key]['excluded']}")


def invert_mapping():
    inv_map = {v["possible"][0]: k for k, v in mapping.items()}
    return inv_map


def invert_patterns():
    inv_map = {str(v): k for k, v in PATTERNS.items()}
    return inv_map


def trim_done_letters(real_letter_, last_letter_):
    global signal_done_letters
    global mapping

    trimming_q = [{"key": real_letter_, "value": last_letter_}]
    while len(trimming_q) > 0:
        key_value_pair = trimming_q.pop(0)
        key_ = key_value_pair["key"]
        letter_ = key_value_pair["value"]
        print(f"LAST LETTER {letter_}")
        signal_done_letters.add(letter_)
        for key in mapping.keys():
            if key != key_:
                if letter_ in mapping[key]["possible"]:
                    mapping[key]["possible"].remove(letter_)
                    mapping[key]["excluded"].append(letter_)

                    if len(mapping[key]["possible"]) == 1 and \
                            mapping[key]["possible"][0] not in signal_done_letters and \
                            mapping[key]["possible"][0] not in trimming_q:
                        trimming_q.append({"key": key, "value": mapping[key]["possible"][0]})


if __name__ == "__main__":
    PATTERNS = {0: ["a", "b", "c", "e", "f", "g"],
                1: ["c", "f"],
                2: ["a", "c", "d", "e", "g"],
                3: ["a", "c", "d", "f", "g"],
                4: ["b", "c", "d", "f"],
                5: ["a", "b", "d", "f", "g"],
                6: ["a", "b", "d", "e", "f", "g"],
                7: ["a", "c", "f"],
                8: ["a", "b", "c", "d", "e", "f", "g"],
                9: ["a", "b", "c", "d", "f", "g"]}

    line_num = -1
    total = 0
    file = get_input(prod=True)
    first_line = True
    while True:
        line_num += 1
        print(f"line {line_num}")
        line = file.readline()
        if not line:
            break
        line = line.strip()
        signals, outputs = line.split("|")
        outputs = outputs.split()
        signals = signals.split()

        mapping = {"a": {"possible": [], "excluded": []},
                   "b": {"possible": [], "excluded": []},
                   "c": {"possible": [], "excluded": []},
                   "d": {"possible": [], "excluded": []},
                   "e": {"possible": [], "excluded": []},
                   "f": {"possible": [], "excluded": []},
                   "g": {"possible": [], "excluded": []}}
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        signal_done_letters = set()
        for signal_word in signals:
            possible_numbers = []
            for num_ in numbers:
                if len(signal_word) == len(PATTERNS[num_]):
                    possible_numbers.append(num_)

            for item in signal_done_letters:
                signal_word.replace(item, "")

            possible_letters = []
            for _ in possible_numbers:
                possible_letters += PATTERNS[_]
            possible_real_letters_ = set(possible_letters)

            remainder_letters = set(mapping.keys()) - possible_real_letters_
            hit_letters = []
            for index, real_letter in enumerate(possible_real_letters_):
                if len(possible_numbers) == possible_letters.count(real_letter):
                    if len(mapping[real_letter]["possible"]) == 0:
                        mapping[real_letter]["possible"] = [_ for _ in signal_word]
                    else:
                        items_to_remove = []
                        for possible_letter in mapping[real_letter]["possible"]:
                            if possible_letter not in signal_word:
                                items_to_remove.append(possible_letter)

                        for item in items_to_remove:
                            mapping[real_letter]["possible"].remove(item)
                            mapping[real_letter]["excluded"].append(item)

                        if len(mapping[real_letter]["possible"]) == 1 and \
                                mapping[real_letter]["possible"][0] not in signal_done_letters:
                            last_letter = mapping[real_letter]["possible"][0]
                            trim_done_letters(real_letter, last_letter)

                if len(signal_done_letters) > 0:
                    print(f"signal_done_letters: {signal_done_letters}")

            print_mapping()

        done_keys_values = []
        not_done_keys = []
        for key in mapping.keys():
            if len(mapping[key]["possible"]) == 1:
                done_keys_values.append(mapping[key]["possible"][0])
            else:
                not_done_keys.append(key)

        if len(not_done_keys) > 1:
            print("oh no...")
        elif len(not_done_keys) == 1:
            for value in done_keys_values:
                if value in mapping[not_done_keys[0]]["possible"]:
                    mapping[not_done_keys[0]]["possible"].remove(value)
                    mapping[not_done_keys[0]]["excluded"].append(value)
        print_mapping()

        inv_mapping = invert_mapping()
        inv_patters = invert_patterns()

        num_string = ""
        for output_word in outputs:
            new_word = []
            for letter in output_word:
                new_word.append(inv_mapping[letter])

            number = inv_patters[str(sorted(new_word))]
            print(number)
            num_string += str(number)
            #if number in [1, 4, 7, 8]:
            #    total += 1
        total += int(num_string)
    print(total)
