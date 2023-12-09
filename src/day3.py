import re
from collections import defaultdict
lines = []
with open("./input/day3.input", 'r') as file:
    lines = file.readlines()

# lines = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
# ]

line_len = len(lines[0])
symbols = ['*', '+', '&', '%', '-', '=', '#', '/', '$', '@']

def is_symbol(str: str):
    #(not str.isalnum() and str != ".")
    return str in symbols
def is_gear(str: str):
    return str == "*"

def check_window(i, j, func) -> bool:
    #north (does it exist and is it a symbol)
    if i > 0 and func(lines[i-1][j]):
        return True
    #northeast
    if (i > 0 and j < line_len-1) and func(lines[i-1][j+1]):
        return True
    #east
    if j < line_len - 1 and func(lines[i][j+1]):
        return True
    #southeast
    if (i < len(lines) - 1 and j < line_len-1) and func(lines[i+1][j+1]):
        return True
    #south
    if i < len(lines) - 1 and func(lines[i+1][j]):
        return True
    #southwest
    if (i < len(lines) - 1 and j > 0) and func(lines[i+1][j-1]):
        return True
    #west
    if j > 0 and func(lines[i][j-1]):
        return True
    #northwest
    if (i > 0 and j > 0) and func(lines[i-1][j-1]):
        return True
    return False

def check_window2(i, j, func) -> tuple:
    #north (does it exist and is it a symbol)
    if i > 0 and func(lines[i-1][j]):
        return (i-1, j)
    #northeast
    if (i > 0 and j < line_len-1) and func(lines[i-1][j+1]):
        return (i-1, j+1)
    #east
    if j < line_len - 1 and func(lines[i][j+1]):
        return (i, j+1)
    #southeast
    if (i < len(lines) - 1 and j < line_len-1) and func(lines[i+1][j+1]):
        return (i+1, j+1)
    #south
    if i < len(lines) - 1 and func(lines[i+1][j]):
        return (i+1, j)
    #southwest
    if (i < len(lines) - 1 and j > 0) and func(lines[i+1][j-1]):
        return (i+1, j-1)
    #west
    if j > 0 and func(lines[i][j-1]):
        return (i, j-1)
    #northwest
    if (i > 0 and j > 0) and func(lines[i-1][j-1]):
        return (i-1, j-1)
    return (-1,-1)

def day3part1():
    pattern = r'\d+'
    sum = 0
    for i, line in enumerate(lines):
        print(f"The sum is currently: {sum}")
        numbers = re.finditer(pattern, line)
        number_idxs = [(match.group(), match.start()) for match in numbers]
        print(number_idxs)

        for idx_tuple in number_idxs:
            # print("idx__typle: ", idx_tuple)
            # iterate over the number
            for j in range(idx_tuple[1], idx_tuple[1]+len(idx_tuple[0])):
                print(f"j: {j}")
                #see if an adjacent square has a symbol - if it does, add number and break out of loop
                if check_window(i,j, is_symbol):
                    sum += int(idx_tuple[0])
                    break

    print(f"Total sum: {sum}")



# dictionary of gear location (i,j) -> numbers touching it
gear_info = defaultdict(list)

def day3part2():
    pattern = r'\d+'
    sum = 0
    for i, line in enumerate(lines):
        print(f"The sum is currently: {sum}")
        numbers = re.finditer(pattern, line)
        number_idxs = [(match.group(), match.start()) for match in numbers]
        print(number_idxs)

        for idx_tuple in number_idxs:
            # iterate over the number
            for j in range(idx_tuple[1], idx_tuple[1]+len(idx_tuple[0])):
                print(f"j: {j}")
                #see if an adjacent square has a gear - if it does, add number to dict and break out of loop
                val = check_window2(i,j, is_gear)
                if val != (-1,-1):
                    gear_info[val].append(int(idx_tuple[0]))
                    print("added: ", idx_tuple[0])
                    break
    # add gear ratios
    for key, value in gear_info.items():
        print(f"key: {key}, value: {value}")
        if len(value) == 2:
            sum+=value[0]*value[1]
    print(f"Total sum: {sum}")


#day3part1()
day3part2()