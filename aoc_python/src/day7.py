from enum import Enum

with open("./input/day7.input", 'r') as file:
    lines = file.readlines()
# lines = [
#         "32T3K 765",
#         "T55J5 684",
#         "KK677 28",
#         "KTJJT 220",
#         "QQQJA 483"
# ]

class Facecard(Enum):
    A = 13
    K = 12
    Q = 11
    # J = 11
    T = 10
    J = 1
class Handtype(Enum):
    HIGHCARD = 1
    ONEPAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    FULLHOUSE = 5
    FOUROFAKIND = 6
    FIVEOFAKIND = 7

class Hand():
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.type = self.get_handtype()

    def get_handtype(self):
        card_freq = [0] * 13
        # find what the card frequencies are in a hand
        for card in self.hand:
            if card.isnumeric():
                card_freq[int(card) - 1] += 1
            else:
                card_freq[Facecard[card].value - 1] += 1

        #handle jokers for p2
        jokers = card_freq[0]
        if jokers > 0:
            card_freq[0] -= jokers
            idx_max = card_freq.index(max(card_freq))
            card_freq[idx_max] += jokers

        print("Card frequency for hand ", self.hand,": ", card_freq)
        h_type = Handtype.HIGHCARD
        if 5 in card_freq:
            h_type = Handtype.FIVEOFAKIND
        elif 4 in card_freq:
            h_type = Handtype.FOUROFAKIND
        elif 3 in card_freq and 2 in card_freq:
            h_type = Handtype.FULLHOUSE
        elif 3 in card_freq:
            h_type = Handtype.THREEOFAKIND
        elif card_freq.count(2) == 2:
            h_type = Handtype.TWOPAIR
        elif 2 in card_freq:
            h_type = Handtype.ONEPAIR
        return h_type

    # ordering functions
    def __lt__(self, obj):
        # if their type is different, use that
        if self.type.value != obj.type.value:
            return self.type.value < obj.type.value
        #otherwise, damn
        else:
            for card, obj_card in zip(self.hand, obj.hand):
                if card.isnumeric() and obj_card.isnumeric():
                    if int(card) != int(obj_card):
                        return int(card) < int(obj_card)
                elif card.isnumeric():
                    if int(card) != Facecard[obj_card].value:
                        return int(card) < Facecard[obj_card].value
                elif obj_card.isnumeric():
                    if Facecard[card].value != int(obj_card):
                        return Facecard[card].value < int(obj_card)
                else:
                    if Facecard[card].value != Facecard[obj_card].value:
                        return Facecard[card].value < Facecard[obj_card].value
        # they are the exact same bruh
        return False
                

    def __repr__(self) -> str:
        return f"type: {self.type.name}, hand: {self.hand}, bid: {self.bid}" 

def day7p1():
    hands = []
    # (Type, hand, bid)
    for line in lines:
        #Get hand and bid from line
        hand, bid = line.strip().split()
        bid = int(bid)
        #add a new Hand (which has type, hand, and bid) to hands
        hands.append(Hand(hand, bid))
        # print("Hand ranking: ", hands)
    hands = sorted(hands)
    # print(hands)
    sum = 0
    for i, hand in enumerate(hands):
        print(f"hand {i}: {hand}")
        # print(f"ADDING bid({hand.bid}) * rank({i+1}) = {(i+1) * hand.bid} to sum!!!! ")
        sum += (i+1) * hand.bid
        # print("=======================================================================")
    print(f"Sum is: {sum}")



def day7p2():
    ...

day7p1()