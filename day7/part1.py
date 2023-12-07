from collections import Counter
import functools

card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}
hand_ranks = {
    "five": 7,
    "four": 6,
    "full": 5,
    "three": 4,
    "two": 3,
    "one": 2,
    "high": 1,
}


def hand_type(hand):
    card_counts = Counter(hand)
    if any(count == 5 for count in card_counts.values()):
        return "five"
    if any(count == 4 for count in card_counts.values()):
        return "four"
    if any(count == 3 for count in card_counts.values()) and any(
        count == 2 for count in card_counts.values()
    ):
        return "full"
    if any(count == 3 for count in card_counts.values()):
        return "three"
    if sum(count == 2 for count in card_counts.values()) == 2:
        return "two"
    if sum(count == 2 for count in card_counts.values()) == 1:
        return "one"
    return "high"


def hand_cmp(hand1, hand2):
    type1 = hand_type(hand1)
    type2 = hand_type(hand2)
    if type1 != type2:
        return hand_ranks[type1] - hand_ranks[type2]
    for i in range(len(hand1)):
        if hand1[i] == hand2[i]:
            continue
        return card_ranks[hand1[i]] - card_ranks[hand2[i]]
    return 0


hands = []
hand_bid = {}
f = open("input", "r")
while True:
    line = f.readline()
    if not line:
        break
    hand, bid = line.rstrip().split()
    bid = int(bid)
    hands.append(hand)
    hand_bid[hand] = bid
f.close()
hands.sort(key=functools.cmp_to_key(hand_cmp))
ans = 0
for idx, hand in enumerate(hands):
    ans += (idx + 1) * hand_bid[hand]
print(ans)

