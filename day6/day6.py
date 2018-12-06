from collections import defaultdict
from pathlib import Path

def part1(input_str):
    inputs = input_str.splitlines()
    coords = []
    for i in inputs:
        split = i.split(', ')
        coords.append((int(split[0]), int(split[1])))
    min_x, min_y, max_x, max_y = 999999, 999999, 0, 0
    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[0] < min_x:
            min_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[0]
        if coord[1] < min_y:
            min_y = coord[0]
    edge_coords = []
    for coord in coords:
        if coord[0] != min_x and coord[0] != max_x and coord[1] != max_y and coord[1] != min_y:
            edge_coords.append(coord)
    dic = defaultdict(int)
    for i in range(max_x+1):
        for j in range(max_y+1):
            closest = 999999
            c_coords = []
            for coord in coords:
                if abs(i - coord[0]) + abs(j - coord[1]) == closest:
                    c_coords.append(coord)
                if abs(i - coord[0]) + abs(j - coord[1]) < closest:
                    closest = abs(i - coord[0]) + abs(j - coord[1])
                    c_coords = [coord]
            if len(c_coords) == 1:
                dic[c_coords[0]] += 1

    dic2 = defaultdict(int)
    for i in range(-200, max_x+200):
        for j in range(-200, max_y+200):
            closest = 999999
            c_coords = []
            for coord in coords:
                if abs(i - coord[0]) + abs(j - coord[1]) == closest:
                    c_coords.append(coord)
                if abs(i - coord[0]) + abs(j - coord[1]) < closest:
                    closest = abs(i - coord[0]) + abs(j - coord[1])
                    c_coords = [coord]
            if len(c_coords) == 1:
                dic2[c_coords[0]] += 1

    max_area = 0
    for coord in edge_coords:
        if coord in dic and dic[coord] == dic2[coord]:
            if dic[coord] > max_area:
                max_area = dic[coord]
    
    print(max_area)

def part2(input_str):
    inputs = input_str.splitlines()
    coords = []
    for i in inputs:
        split = i.split(', ')
        coords.append((int(split[0]), int(split[1])))
    min_x, min_y, max_x, max_y = 999999, 999999, 0, 0
    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[0] < min_x:
            min_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[0]
        if coord[1] < min_y:
            min_y = coord[0]
    region_size = 0
    for i in range(max_x+1):
        for j in range(max_y+1):
            sum = 0
            for coord in coords:
                sum += abs(i - coord[0]) + abs(j - coord[1])
            if sum < 10000:
                region_size += 1
                
    print(region_size)

def main():
    input_str = Path("input").read_text()
    part1(input_str)
    part2(input_str)

if __name__ == "__main__":
    main()
