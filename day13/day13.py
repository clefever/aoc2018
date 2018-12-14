from pathlib import Path

def part1(input_str):
    lines = input_str.splitlines()
    track_dict = {}
    cart_list = []
    height = len(lines)
    width = len(lines[0])
    carts = ">v<^"

    for y in range(height):
        for x in range(width):
            track_dict[x,y] = lines[y][x]
    
    cid = 0
    for y in range(height):
        for x in range(width):
            if track_dict[x,y] in carts:

                cart_list.append((x, y, track_dict[x,y], 0, cid))
                cid += 1

                if track_dict[x,y] == ">" or track_dict[x,y] == "<":
                    track_dict[x,y] = "-"
                elif track_dict[x,y] == "^" or track_dict[x,y] == "v":
                    track_dict[x,y] = "|"

    while True:
        for i in range(len(cart_list)):
            move_dir = None
            if cart_list[i][2] == ">":
                move_dir = (1,0)
            elif cart_list[i][2] == "v":
                move_dir = (0,1)
            elif cart_list[i][2] == "<":
                move_dir = (-1,0)
            else:
                move_dir = (0,-1)

            next_section = (cart_list[i][0]+move_dir[0],cart_list[i][1]+move_dir[1])

            next_icon = cart_list[i][2]
            next_turn = cart_list[i][3]
            if track_dict[next_section] == "+":
                if cart_list[i][3] == 0:
                    if cart_list[i][2] == ">":
                        next_icon = "^"
                    elif cart_list[i][2] == "v":
                        next_icon = ">"
                    elif cart_list[i][2]== "<":
                        next_icon = "v"
                    else:
                        next_icon = "<"
                elif cart_list[i][3] == 2:
                    if cart_list[i][2] == ">":
                        next_icon = "v"
                    elif cart_list[i][2] == "v":
                        next_icon = "<"
                    elif cart_list[i][2]== "<":
                        next_icon = "^"
                    else:
                        next_icon = ">"
                next_turn = (cart_list[i][3] + 1) % 3
            elif track_dict[next_section] == "/":
                if cart_list[i][2] == ">":
                    next_icon = "^"
                elif cart_list[i][2] == "v":
                    next_icon = "<"
                elif cart_list[i][2]== "<":
                    next_icon = "v"
                else:
                    next_icon = ">"
            elif track_dict[next_section]== "\\":
                if cart_list[i][2] == ">":
                    next_icon = "v"
                elif cart_list[i][2] == "v":
                    next_icon = ">"
                elif cart_list[i][2]== "<":
                    next_icon = "^"
                else:
                    next_icon = "<"

            cart_list[i] = (cart_list[i][0] + move_dir[0], cart_list[i][1] + move_dir[1], next_icon, next_turn, cart_list[i][4])

            for c in cart_list:
                if c[4] != cart_list[i][4]:
                    if cart_list[i][0] == c[0] and cart_list[i][1] == c[1]:
                        return str(c[0]) + "," + str(c[1])

def part2(input_str):
    lines = input_str.splitlines()
    track_dict = {}
    cart_list = []
    height = len(lines)
    width = len(lines[0])
    carts = ">v<^"

    for y in range(height):
        for x in range(width):
            track_dict[x,y] = lines[y][x]
    
    cid = 0
    for y in range(height):
        for x in range(width):
            if track_dict[x,y] in carts:

                cart_list.append((x, y, track_dict[x,y], 0, cid, True))
                cid += 1

                if track_dict[x,y] == ">" or track_dict[x,y] == "<":
                    track_dict[x,y] = "-"
                elif track_dict[x,y] == "^" or track_dict[x,y] == "v":
                    track_dict[x,y] = "|"

    while True:
        cart_list.sort(key=lambda c: (c[1],c[0]))
        for i in range(len(cart_list)):
            if cart_list[i][5]:
                move_dir = None
                if cart_list[i][2] == ">":
                    move_dir = (1,0)
                elif cart_list[i][2] == "v":
                    move_dir = (0,1)
                elif cart_list[i][2] == "<":
                    move_dir = (-1,0)
                else:
                    move_dir = (0,-1)

                next_section = (cart_list[i][0]+move_dir[0],cart_list[i][1]+move_dir[1])

                next_icon = cart_list[i][2]
                next_turn = cart_list[i][3]
                if track_dict[next_section] == "+":
                    if cart_list[i][3] == 0:
                        if cart_list[i][2] == ">":
                            next_icon = "^"
                        elif cart_list[i][2] == "v":
                            next_icon = ">"
                        elif cart_list[i][2]== "<":
                            next_icon = "v"
                        else:
                            next_icon = "<"
                    elif cart_list[i][3] == 2:
                        if cart_list[i][2] == ">":
                            next_icon = "v"
                        elif cart_list[i][2] == "v":
                            next_icon = "<"
                        elif cart_list[i][2]== "<":
                            next_icon = "^"
                        else:
                            next_icon = ">"
                    next_turn = (cart_list[i][3] + 1) % 3
                elif track_dict[next_section] == "/":
                    if cart_list[i][2] == ">":
                        next_icon = "^"
                    elif cart_list[i][2] == "v":
                        next_icon = "<"
                    elif cart_list[i][2]== "<":
                        next_icon = "v"
                    else:
                        next_icon = ">"
                elif track_dict[next_section]== "\\":
                    if cart_list[i][2] == ">":
                        next_icon = "v"
                    elif cart_list[i][2] == "v":
                        next_icon = ">"
                    elif cart_list[i][2]== "<":
                        next_icon = "^"
                    else:
                        next_icon = "<"

                cart_list[i] = (cart_list[i][0] + move_dir[0], cart_list[i][1] + move_dir[1], next_icon, next_turn, cart_list[i][4], cart_list[i][5])

                remaining = [k for k in cart_list if k[5]]
                list_len = len(remaining)
                if list_len == 1:
                    return str(remaining[0][0]) + "," + str(remaining[0][1])

                for j in range(len(cart_list)):
                    if cart_list[j][5] and cart_list[j][4] != cart_list[i][4]:
                        if cart_list[i][0] == cart_list[j][0] and cart_list[i][1] == cart_list[j][1]:
                            cart_list[i] = (cart_list[i][0], cart_list[i][1], cart_list[i][2], cart_list[i][3], cart_list[i][4], False)
                            cart_list[j] = (cart_list[j][0], cart_list[j][1], cart_list[j][2], cart_list[j][3], cart_list[j][4], False)

def main():
    input_str = Path("input").read_text()
    print(part1(input_str))
    print(part2(input_str))

if __name__ == "__main__":
    main()
