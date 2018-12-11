from collections import defaultdict
from pathlib import Path

class Square:
    def __init__(self, id, l_margin, t_margin, width, height):
        self.id = id
        self.l_margin = l_margin
        self.t_margin = t_margin
        self.width = width
        self.height = height

def part1(input_str):
    grid = defaultdict(int)
    count = 0
    grid_strs = input_str.splitlines()
    for line in grid_strs:
        tokens = line.split(' ')
        margins = tokens[2].split(',')
        sizes = tokens[3].split('x')
        s = Square(tokens[0][1:], int(margins[0]), int(margins[1][:-1]), int(sizes[0]), int(sizes[1]))
        for i in range(s.t_margin, s.height + s.t_margin):
            for j in range(s.l_margin, s.width + s.l_margin):
                grid[(i, j)] += 1

    for item in grid.items():
        if item[1] > 1:
            count += 1

    return count

def part2(input_str):
    grid = defaultdict(int)
    squares = []
    grid_strs = input_str.splitlines()
    for line in grid_strs:
        tokens = line.split(' ')
        margins = tokens[2].split(',')
        sizes = tokens[3].split('x')
        s = Square(tokens[0][1:], int(margins[0]), int(margins[1][:-1]), int(sizes[0]), int(sizes[1]))
        squares.append(s)
        for i in range(s.t_margin, s.height + s.t_margin):
            for j in range(s.l_margin, s.width + s.l_margin):
                grid[(i, j)] += 1

    for s in squares:
        unique = True
        for i in range(s.t_margin, s.height + s.t_margin):
            for j in range(s.l_margin, s.width + s.l_margin):
                if grid[(i, j)] > 1:
                    unique = False

        if unique:
            return s.id

def main():
    input_str = Path("input").read_text()
    print(part1(input_str))
    print(part2(input_str))

if __name__ == "__main__":
    main()
