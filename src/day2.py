lines_spec = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ]

def day2part1():

    lines = []
    with open("./input/day2.input", 'r') as file:
        lines = file.readlines()
    possible = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    sum = 0
    for line in lines:
        print()
        print(line)
        split_line = line.split(":")
        game_id = int(split_line[0].split()[1])
        sets = split_line[1].split(";")
        valid_line = True
        for set in sets:
            set_split = set.split(",")
            print("Set split: ", set_split)
            for color in set_split:
                color_list = color.strip().split()
                print("color: ", color_list[1], ", amount: ", color_list[0])
                if possible[color_list[1]] < int(color_list[0]):
                    valid_line = False
        print("line is valid? ", valid_line)
        if valid_line:
            print(game_id)
            sum += game_id
    print("sum: ", sum)

def day2part2():

    lines = []
    with open("./input/day2.input", 'r') as file:
        lines = file.readlines()
    possible = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    sum = 0
    for line in lines:
        print()
        print(line)
        split_line = line.split(":")
        sets = split_line[1].split(";")
        red = 0
        blue = 0
        green = 0
        #loop over the sets within a game
        for set in sets:
            set_split = set.split(",")
            print("Set split: ", set_split)
            #loop over the cube colors within a set
            for color in set_split:
                color_list = color.strip().split()
                print ("color list", color_list)
                if color_list[1] == "red" and int(color_list[0]) > red:
                    red = int(color_list[0])
                elif color_list[1] == "blue" and int(color_list[0]) > blue:
                    blue = int(color_list[0])
                elif color_list[1] == "green" and int(color_list[0]) > green:
                    green = int(color_list[0])
                print("WITHIN A SET+++", "red: ", red, " blue: ", blue, " green", green)
        print("WITHIN A GAMEE+++++++++", "red: ", red, " blue: ", blue, " green", green)
        temp = red*blue*green
        sum += temp
    print("sum: ", sum)

day2part2()
#day2part1()