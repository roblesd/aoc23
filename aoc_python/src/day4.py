from collections import defaultdict
with open("./input/day4.input", 'r') as file:
    lines = file.readlines()
# lines = [
#     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
#     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
#     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
#     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
#     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
#     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
# ]
def day4part1():
    sum = 0
    for line in lines:
        numbers = line.split(": ")[1].split(" | ")
        #get the winning nums per card as a set
        winning_nums = numbers[0].split()
        winning_nums = [int(winning_num) for winning_num in winning_nums]
        winning_nums_set = set(winning_nums)

        #get your numbers as a list of ints
        nums = numbers[1].split()
        nums = [int(num) for num in nums]

        wins = 0
        #find the number of wins you have
        for num in nums:
            if num in winning_nums_set:
                if wins == 0:
                    wins += 1
                else:
                    wins *= 2
        sum += wins
    print(sum)

card_amts = defaultdict(lambda: 1)

def day4part2():
    sum = 0
    for i, line in enumerate(lines):
        # if the card is not in the dict, initialize it to 1
        if i not in card_amts:
            card_amts[i] = 1
        numbers = line.split(": ")[1].split(" | ")
        #get the winning nums per card as a set
        winning_nums = numbers[0].split()
        winning_nums = [int(winning_num) for winning_num in winning_nums]
        winning_nums_set = set(winning_nums)

        #get your numbers as a list of ints
        nums = numbers[1].split()
        nums = [int(num) for num in nums]
        wins = 0
        for num in nums:
            if num in winning_nums_set:
                wins+=1
        # for each copy of a card, add future cards
        for _ in range(card_amts[i]):
            # add a copy of future cards, for each winning number that you got in the current card
            for j in range(wins):
                card_amts[i+j+1] += 1
    for _, value in card_amts.items():
        sum += value
    print(sum)
day4part2()