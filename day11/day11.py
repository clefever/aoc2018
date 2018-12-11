class FuelCell:
    def __init__(self, x, y, serial):
        self.x = x
        self.y = y
        self.serial = serial

    def get_rackId(self):
        return self.x + 10

    def get_powerLevel(self):
        intermediate = ((self.get_rackId() * self.y) + self.serial) * self.get_rackId()
        return -5 if len(str(intermediate)) < 3 else int(str(intermediate)[-3]) - 5

def generate_grid(grid_size, serial):
    grid = {}
    for i in range(1, grid_size+1):
        for j in range(1, grid_size+1):
            fc = FuelCell(i, j, serial)
            grid[(i, j)] = fc.get_powerLevel()
    return grid

def part1(grid_size, serial):
    grid = generate_grid(grid_size, serial)
    max = max_x = max_y = 0

    for i in range (1, grid_size-1):
        for j in range(1, grid_size-1):
            sum = grid[i,j] + grid[i+1,j] + grid[i+2,j] + grid[i,j+1] + grid[i+1,j+1] + grid[i+2,j+1] + grid[i,j+2] + grid[i+1,j+2] + grid[i+2,j+2]    
            if sum > max:
                max = sum
                max_x = i
                max_y = j

    return max_x, max_y

def part2(grid_size, serial):
    grid = generate_grid(grid_size, serial)
    max = max_x = max_y = max_s = 0
    sum_dict = {}

    for s in range(1, grid_size+1):
        for i in range(1, (grid_size+1)-(s-1)):
            for j in range(1, (grid_size+1)-(s-1)):
                sum = 0
                if s % 2 == 0 and s != 2:
                    sub = s//2
                    sum = sum_dict[(i,j,sub)] + sum_dict[(i+sub,j,sub)] + sum_dict[(i,j+sub,sub)] + sum_dict[(i+sub,j+sub,sub)]
                    sum_dict[(i, j, s)] = sum
                elif s % 2 == 1 and s != 1:
                    sub = s-1
                    sum = sum_dict[(i,j,sub)] + sum_dict[(i+1,j+1,sub)] + grid[(i+sub,j)] + grid[(i,j+sub)] - sum_dict[(i+1,j+1,s-2)]
                    sum_dict[(i, j, s)] = sum
                else:
                    for k in range(s):
                        for l in range(s):
                            sum += grid[(i+k,j+l)]
                    sum_dict[(i, j, s)] = sum
                if sum > max:
                    max = sum
                    max_x = i
                    max_y = j
                    max_s = s

    return max_x, max_y, max_s

def main():
    puzzle_input = 9995
    grid_size = 300
    print(part1(grid_size, puzzle_input))
    print(part2(grid_size, puzzle_input))

if __name__ == "__main__":
    main()
