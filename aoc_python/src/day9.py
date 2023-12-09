
with open("./input/day9.input", 'r') as file:
    lines = file.readlines()

# lines = ["0 3 6 9 12 15",
#         "1 3 6 10 15 21",
#         "10 13 16 21 30 45"
# ]
def find_pattern(l: list):
        diff = [l[i] - l[i-1] for i in range(1,len(l))]
        # print(diff)
        new_diff = diff
        pattern = [l, diff]

        while any(new_diff):
            diff = new_diff
            # print(f"Old diff: {diff}")
            new_diff = [diff[i]-diff[i-1] for i in range(1, len(diff))]
            pattern.append(new_diff)
            # print(f"New diff: {new_diff}")
        # print(f"In the end: {diff}")
        return (len(pattern), list(reversed(pattern)))

def day9p1():
    sum = 0
    for line in lines:
        line = line.strip().split()
        line = [int(elt) for elt in line]
        p_len, pattern = find_pattern(line)
        
        for i in range(1,p_len):
            pattern[i].append(pattern[i][-1] + pattern[i-1][-1])
        
        print(f"Addding {pattern[-1][-1]} to the sum")
        sum += pattern[-1][-1]

    print(sum)

def day9p2():
    sum = 0
    for line in lines:
        line = line.strip().split()
        line = [int(elt) for elt in line]
        p_len, pattern = find_pattern(line)
        
        for i in range(1,p_len):
            pattern[i].insert(0, pattern[i][0] - pattern[i-1][0])
        
        print(f"Addding {pattern[-1][0]} to the sum")
        sum += pattern[-1][0]

    print(sum)    
    
day9p2()