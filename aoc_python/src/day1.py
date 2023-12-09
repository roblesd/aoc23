
def day1_part1():
    lines_spec = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
            ]
    lines = []
    with open("./input/day1.input", 'r') as file:
        lines = file.readlines()

    sum = 0

    for line in lines:
        l = 0
        r = len(line)-1
        l_found = False
        r_found  = False
        for i in range(len(line)):
            if line[l].isnumeric() and not l_found:
                sum += int(line[l]) * 10
                l_found = True
            else:
                l += 1
            if line[r].isnumeric() and not r_found:
                sum += int(line[r])
                r_found = True
            else:
                r -= 1
            if l_found and r_found:
                break
    print(sum)

def day1_part2_old():
    lines_spec = [
                    "two1nine",
                    "eightwothree",
                    "abcone2threexyz",
                    "xtwone3four",
                    "4nineeightseven2",
                    "zoneight234",
                    "7pqrstsixteen"
    ]
    lines = []
    with open("./input/day1.input", 'r') as file:
        lines = file.readlines()
    sum = 0
    value_dict = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9
    }
    line_test = [
        "6tvxlgrsevenjvbxbfqrsk4seven"
    ]
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for line in line_test:
        # print(f"line: {line}")
        num_pos = {}
        # find the index of every number representation in the line
        for num in nums:
            idx = line.find(num)
            if idx != -1:
                num_pos[num] = idx
        # need to find the lowest index number and the highest index number
        l = len(line)
        lval = ""
        r = -1
        rval = ""
        for key, val in num_pos.items():
            print(f"key: {key}, val: {val}")
            if val < l:
                l = val
                lval = key
            if val > r:
                r = val
                rval = key
        #print(f"for line: {line}, the left index is: {l} and the right index is {r}")
        # add the number contributions to sum
        print(f"line: {line.strip()}, lval: {value_dict[lval]}, rval: {value_dict[rval]}")
        sum += (10*value_dict[lval] + value_dict[rval])
    print(sum)


def day1_part2():
    lines_spec = [
                    "two1nine",
                    "eightwothree",
                    "abcone2threexyz",
                    "xtwone3four",
                    "4nineeightseven2",
                    "zoneight234",
                    "7pqrstsixteen"
    ]
    lines = []
    with open("./input/day1.input", 'r') as file:
        lines = file.readlines()
    sum = 0
    value_dict = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9
    }
    line_test = [
        "6tvxlgrsevenjvbxbfqrsk4seven"
    ]
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    nums_rev = [num[::-1] for num in nums]
    print(nums_rev)
    for line in lines:
        # print(f"line: {line}")
        # find lowest index going forward
        l = len(line)
        lval = ""
        for num in nums:
            idx = line.find(num)
            if idx != -1 and idx < l:
                l = idx
                lval = num
        # find lowest index on reversed line
        r = len(line)
        rval = ""
        rev_line = line[::-1]
        for num in nums_rev:
            idx = rev_line.find(num)
            if idx != -1 and idx < r:
                r = idx
                rval = num[::-1]
        
        print(f"line: {line.strip()}, lval: {value_dict[lval]}, rval: {value_dict[rval]}")
        sum += (10*value_dict[lval] + value_dict[rval])
    
    print(sum)


#day1_part1()
day1_part2()