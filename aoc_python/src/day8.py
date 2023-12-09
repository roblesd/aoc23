with open("./input/day8.input", 'r') as file:
    lines = file.readlines()
# with open("./day8spec.txt", 'r') as file:
#     lines = file.readlines()
import math
def day8p1():
    lines_new = [line.strip() for line in lines if line.strip()!=""]
    directions = lines_new[0]
    path = {}
    for line in lines_new[1:]:
        loc, l_r = line.split(" = ")
        l,r = l_r.strip("()").split(",")
        r = r.strip()
        l = l.strip()
        print(f"{l}|{r}")
        path[loc] = (l,r)

    i = 0
    next_loc = "AAA"
    print(f"directions: {directions}")
    while True:
        #Get direction (L/R)
        dir = directions[i%len(directions)]
        #Get next location
        if dir == "L":
            next_loc = path[next_loc][0]
        else:
            next_loc = path[next_loc][1]

        if next_loc == "ZZZ":
            i += 1
            break
        i += 1
    print(f"final i: {i}")

def day8p2():
    lines_new = [line.strip() for line in lines if line.strip()!=""]
    directions = lines_new[0]
    next_locs = []
    path = {}
    for line in lines_new[1:]:
        loc, l_r = line.split(" = ")
        # add starting locs to a list
        if loc[-1] == "A":
            next_locs.append(loc)

        l,r = l_r.strip("()").split(",")
        r = r.strip()
        l = l.strip()
        print(f"{l}|{r}")
        path[loc] = (l,r)
    print(f"NEXT LOCS: {next_locs}")

    cycles = []
    for next_loc in next_locs:
        i = 0
        print(f"directions: {directions}")
        while True:
            #Get direction (L/R)
            dir = directions[i%len(directions)]
            #Get next location
            if dir == "L":
                next_loc = path[next_loc][0]
            else:
                next_loc = path[next_loc][1]
            if next_loc[-1] == "Z":
                i += 1
                cycles.append(i)
                break
            i += 1
    print(cycles)
    print(math.lcm(*cycles))

    # i = 0
    # found_zs = 0
    # print(f"directions: {directions}")
    # while found_zs != len(next_locs):
    #     # print(f"i is {i}")
    #     found_zs = 0
    #     #Get direction (L/R)
    #     dir = directions[i%len(directions)]
    #     #Get next location
    #     for j in range(len(next_locs)):
    #         # print(f"j: {j}, before next_locs[j]: {next_locs[j]}")
    #         if dir == "L":
    #             next_locs[j] = path[next_locs[j]][0]
    #         else:
    #             next_locs[j] = path[next_locs[j]][1]
    #         # print(f"j: {j}, after next_locs[j]: {next_locs[j]}")
    #         if next_locs[j][-1] == "Z":
    #             found_zs += 1
    #     i += 1
    # print(f"final i: {i}")
day8p2()