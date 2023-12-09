with open("./input/day6.input", 'r') as file:
    data = file.readlines()

# data = [
#     "Time:      7  15   30",
#     "Distance:  9  40  200"
# ]

def day6part1():
    times = [int(time) for time in data[0].split()[1:]]
    print(times)
    distances = [int(distance) for distance in data[1].split()[1:]]
    print(distances)

    wins = [0] * len(times)
    for j, (time, distance) in enumerate(zip(times,distances)):
        for i in range(time):
            d = i * (time-i)
            if d > distance:
                wins[j] += 1
    product = 1
    for win in wins:
        product *= win
    print(product)

def day6part2():
    times = [int("".join(data[0].split()[1:]))]
    print(times)
    distances = [int("".join(data[1].split()[1:]))]
    print(distances)

    wins = [0] * len(times)
    for j, (time, distance) in enumerate(zip(times,distances)):
        for i in range(time):
            d = i * (time-i)
            if d > distance:
                wins[j] += 1
    product = 1
    for win in wins:
        product *= win
    print(product)

def oh_of_1():
    time = int("".join(data[0].split()[1:]))
    print(time)
    distance = int("".join(data[1].split()[1:]))
    print(distance)

    print(int((time**2-4*distance)**(1/2)))

oh_of_1()