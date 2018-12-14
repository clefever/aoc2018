def part1(puzzle_input):
    recipes = [3, 7]
    elf1_i, elf2_i = 0, 1

    while True:
        next_recipes = recipes[elf1_i] + recipes[elf2_i]
        rec_str = str(next_recipes)
        recipes.extend([int(c) for c in rec_str])
        elf1_i += 1 + recipes[elf1_i]
        elf2_i += 1 + recipes[elf2_i]
        if elf1_i > len(recipes)-1:
            elf1_i = elf1_i % len(recipes)
        if elf2_i > len(recipes)-1:
            elf2_i = elf2_i % len(recipes)
        if len(recipes) > 10 + puzzle_input:
            break

    return "".join([str(i) for i in recipes[puzzle_input:puzzle_input+10]])

def part2(puzzle_input):
    sequence = [int(c) for c in str(puzzle_input)]
    recipes = [3, 7]
    elf1_i, elf2_i = 0, 1

    while True:
        for _ in range (1000000):
            next_recipes = recipes[elf1_i] + recipes[elf2_i]
            rec_str = str(next_recipes)
            recipes.extend([int(c) for c in rec_str])
            elf1_i += 1 + recipes[elf1_i]
            elf2_i += 1 + recipes[elf2_i]
            if elf1_i > len(recipes)-1:
                elf1_i = elf1_i % len(recipes)
            if elf2_i > len(recipes)-1:
                elf2_i = elf2_i % len(recipes)
        
        for r in range(len(recipes)-len(sequence)):
            if recipes[r:r+len(sequence)] == sequence:
                return r

def main():
    puzzle_input = 556061
    print(part1(puzzle_input))
    print(part2(puzzle_input))

if __name__ == "__main__":
    main()
