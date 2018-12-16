import ast
from pathlib import Path

def addr(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]] + arr[i[2]]
    return arr

def addi(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]] + i[2]
    return arr

def mulr(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]] * arr[i[2]]
    return arr

def muli(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]] * i[2]
    return arr

def banr(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]] & arr[i[2]]
    return arr

def bani(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]] & i[2]
    return arr

def borr(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]] | arr[i[2]]
    return arr

def bori(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]] | i[2]
    return arr

def setr(rs, i):
    arr = rs[:]
    arr[i[3]] = arr[i[1]]
    return arr

def seti(rs, i):
    arr = rs[:]
    arr[i[3]] = i[1]
    return arr

def gtir(rs, i):
    arr = rs[:]
    arr[i[3]] = 1 if i[1] > arr[i[2]] else 0
    return arr

def gtri(rs, i):
    arr = rs[:]
    arr[i[3]] = 1 if arr[i[1]] > i[2] else 0
    return arr

def gtrr(rs, i):
    arr = rs[:]
    arr[i[3]] = 1 if arr[i[1]] > arr[i[2]] else 0
    return arr

def eqir(rs, i):
    arr = rs[:]
    arr[i[3]] = 1 if i[1] == arr[i[2]] else 0
    return arr

def eqri(rs, i):
    arr = rs[:]
    arr[i[3]] = 1 if arr[i[1]] == i[2] else 0
    return arr

def eqrr(rs, i):
    arr = rs[:]
    arr[i[3]] = 1 if arr[i[1]] == arr[i[2]] else 0
    return arr

functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def filter_dict(func_dict):
    filtered = {}
    while True:
        to_delete = []
        for kv in func_dict.items():
            if len(kv[1]) == 1:
                filtered[kv[0]] = kv[1][0]
                to_delete.append(kv)
        for kv in to_delete:
            del func_dict[kv[0]]
            for i in func_dict.items():
                if kv[1][0] in i[1]:
                    i[1].remove(kv[1][0])
        len_ones = [len(kv[1]) == 1 for kv in func_dict.items()]
        if len(func_dict) == 0 and all(len_ones):
            break
    return filtered

def part1(input_str):
    lines = input_str.split("\n\n\n")[0].splitlines()
    lines = list(filter(None, lines))
    before = []
    instruction = []
    after = []
    total = 0

    for line in lines:
        if "Before" in line:
            before = ast.literal_eval(line[8:])
        elif "After" not in line:
            instruction = list(map(int, line.split(' ')))
        else:
            after = ast.literal_eval(line[8:])
            count = 0
            for f in functions:
                if after == f(before, instruction):
                    count += 1
            if count >= 3:
                total += 1

    return total

def part2(input_str):
    lines = input_str.split("\n\n\n")[0].splitlines()
    lines = list(filter(None, lines))
    before = []
    instruction = []
    after = []
    func_dict = {}

    for line in lines:
        if "Before" in line:
            before = ast.literal_eval(line[8:])
        elif "After" not in line:
            instruction = list(map(int, line.split(' ')))
        else:
            after = ast.literal_eval(line[8:])
            funcs = []
            for f in functions:
                if after == f(before, instruction):
                    funcs.append(f)
            if instruction[0] in func_dict:
                mapping = func_dict[instruction[0]]
                common = list(set(funcs) & set(mapping))
                func_dict[instruction[0]] = common
            else:
                func_dict[instruction[0]] = funcs

    opcode_dict = filter_dict(func_dict)

    registers = [0] * 4

    lines = input_str.split("\n\n\n")[1].splitlines()
    lines = list(filter(None, lines))
    instruction = []

    for line in lines:
        instruction = list(map(int, line.split(' ')))
        f = opcode_dict[instruction[0]]
        registers = f(registers, instruction)

    return registers[0]

def main():
    input_str = Path("input").read_text()
    print(part1(input_str))
    print(part2(input_str))

if __name__ == "__main__":
    main()
