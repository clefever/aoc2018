from collections import defaultdict
from pathlib import Path

class PosVelPair:

    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def move(self, reverse=False):
        if reverse:
            newPosx = self.pos[0] - self.vel[0]
            newPosy = self.pos[1] - self.vel[1]
            self.pos = (newPosx, newPosy)
        else:
            newPosx = self.pos[0] + self.vel[0]
            newPosy = self.pos[1] + self.vel[1]
            self.pos = (newPosx, newPosy)


def calculate_message(input_str):
    inputs = input_str.splitlines()
    infos = []
    max_x = max_y = -999999
    min_x = min_y = 999999
    for line in inputs:
        info = line
        pos = (int(info[10:16]), int(info[17:24])) # TODO: Use regex for these
        vel = (int(info[36:38]), int(info[39:42]))
        if pos[0] > max_x:
            max_x = pos[0]
        if pos[0] < min_x:
            min_x = pos[0]
        if pos[1] > max_y:
            max_y = pos[1]
        if pos[1] < min_y:
            min_y = pos[1]
        infos.append(PosVelPair(pos, vel))

    smallest_area = 9999999999999
    b_mi_x = b_mi_y = 999999
    b_ma_x = b_ma_y = -999999
    count = 0

    for _ in range(15000):
        count += 1
        mi_x = mi_y = 999999
        ma_x = ma_y = -999999
        grid = defaultdict(bool)
        for p in infos:
            p.move()
            grid[p.pos] = True
        for p in infos:
            if p.pos[0] < mi_x:
                mi_x = p.pos[0]
            if p.pos[0] > ma_x:
                ma_x = p.pos[0]
            if p.pos[1] < mi_y:
                mi_y = p.pos[1]
            if p.pos[1] > ma_y:
                ma_y = p.pos[1]
        area = (ma_x-mi_x)*(ma_y-mi_y)
        if area <= smallest_area:
            smallest_area = area
            b_mi_x = mi_x
            b_mi_y = mi_y
            b_ma_x = ma_x
            b_ma_y = ma_y
        else:
            grid = defaultdict(bool)
            for p in infos:
                p.move(True)
                grid[p.pos] = True
            break

    lines = ""
    for i in range(b_mi_y, b_ma_y+1):
        for j in range(b_mi_x, b_ma_x+1):
            if grid[(j, i)]:
                lines += "#"
            else:
                lines += "."
        lines += "\n"

    return lines, count-1

def main():
    input_str = Path("input").read_text()
    result = calculate_message(input_str)
    print(result[0])
    print(result[1])

if __name__ == "__main__":
    main()
