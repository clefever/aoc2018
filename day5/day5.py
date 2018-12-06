from pathlib import Path

def reactive_index(str):
    for i in range(len(str)-1):
        if str[i] != str[i+1] and str[i].upper() == str[i+1].upper():
            return i
    return -1

def remove_unit(str, ch):
    return "".join([c for c in str if ch.upper() != c.upper()])

def part1(input_str):
    input_str = input_str.strip('\n')
    while True:
        index = reactive_index(input_str)
        if index == -1:
            break
        input_str = input_str[:index] + input_str[index+2:]
    print(len(input_str))

# TODO: This takes way too long
def part2(input_str):
    letters = "abcdefghijklmnopqrstuvwxyz"
    input_str = input_str.strip('\n')
    results = {}
    for l in letters:
        s = remove_unit(input_str, l)
        while True:
            index = reactive_index(s)
            if index == -1:
                break
            s = s[:index] + s[index+2:]
        results[l] = len(s)
    print(results)

def main():
    input_str = Path("input").read_text()
    part1(input_str)
    part2(input_str)


if __name__ == "__main__":
    main()
