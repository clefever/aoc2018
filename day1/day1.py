from collections import defaultdict
from pathlib import Path

def parse_changes(input_str):
    return sum([int(param) for param in input_str.splitlines()])

def first_repeated_freq(input_str):
    changes = [int(param) for param in input_str.splitlines()]
    freqs = set([0])
    curr_freq = 0
    while True:
        for change in changes:
            curr_freq += change
            if curr_freq in freqs:
                return curr_freq
            freqs.add(curr_freq)

def main():
    input_str = Path("input").read_text()
    print(parse_changes(input_str))
    print(first_repeated_freq(input_str))

if __name__ == "__main__":
    main()
