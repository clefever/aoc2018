from collections import defaultdict
from pathlib import Path

def checksum(input_str):
    inputs = input_str.splitlines()
    threes = twos = 0
    for i in inputs:
        twos_done, threes_done = False, False
        char_dict = defaultdict(int)
        for c in i:
            char_dict[c] += 1
        for kv in char_dict.items():
            if kv[1] == 2:
                if not twos_done:
                    twos += 1
                    twos_done = True
            if kv[1] == 3:
                if not threes_done:
                    threes += 1
                    threes_done = True
    return threes * twos

def common_letters(input_str):
    inputs = input_str.splitlines()
    for word_pos in range(len(inputs)):
        if word_pos < len(inputs) - 1:
            for word1_pos in range(word_pos+1, len(inputs)):
                errors = 0
                for char_pos in range(len(inputs[word_pos])):
                    if inputs[word_pos][char_pos] != inputs[word1_pos][char_pos]:
                        errors += 1
            
                if errors <= 1:
                    print(inputs[word_pos] + ", " + inputs[word1_pos])
                    return

def main():
    input_str = Path("input").read_text()
    print(checksum(input_str))
    print(common_letters(input_str))

if __name__ == "__main__":
    main()
