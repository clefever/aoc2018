from pathlib import Path

def run_generations(num_gens, initial_state, rules):
    first_pot_num = 0
    for g in range(num_gens):
        left = initial_state[:5].find('#')
        if left != -1:
            initial_state = ('.' * (5-left)) + initial_state
        right = initial_state[len(initial_state)-5:].rfind('#')
        if right != -1:
            initial_state = initial_state + ('.' * (right+1) )
        next_state = ''
        for i in range(2, len(initial_state) - 2):
            window = initial_state[i-2:i+3]
            output = ' '
            for line in rules:
                if window == line[:5]:
                    output = line[9]
            if output != ' ':
                next_state += output
            else:
                next_state += "."
        if left != -1:
            first_pot_num = first_pot_num - ((5-left) - 2)
        else:
            first_pot_num += 2
        initial_state = next_state

    total = 0
    pot_num = first_pot_num
    for c in initial_state:
        if c == "#":
            total += pot_num
        pot_num += 1
    return total

def get_params(input_str):
    lines = input_str.splitlines()
    initial_state = lines[0].split(' ')[2]
    rules = lines[2:]
    return initial_state, rules

def part1(input_str):
    params = get_params(input_str)
    return run_generations(20, params[0], params[1])

def part2(input_str):
    params = get_params(input_str)
    generations = 500
    s1 = run_generations(generations, params[0], params[1])
    s2 = run_generations(generations+1, params[0], params[1])
    return (s2-s1) * (50000000000 - generations) + s1

def main():
    input_str = Path("input").read_text()
    print(part1(input_str))
    print(part2(input_str))

if __name__ == "__main__":
    main()
