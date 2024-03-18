import numpy as np

card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
# A dictionary with card value
card_dict = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

# Open the file and read the lines
with open('Day7/input.txt') as f:
    lines = f.readlines()

hands = []
bids = []
for line in lines:
    hands.append(line.strip().split(' ')[0])
    bids.append(int(line.strip().split(' ')[1].strip().split('\n')[0]))


nhands = len(hands)

# Get the type of each hand
# Five of a kind = 7
# Four of a kind = 6
# Full house = 5
# Three of a kind = 4
# Two pair = 3
# One pair = 2
# High card = 1

def get_hand_type(hand):
    hand_type = 1
    hand_dict = {}
    for card in hand:
        if card in hand_dict:
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1

    if 5 in hand_dict.values():
        hand_type = 7
    elif 4 in hand_dict.values():
        hand_type = 6
    elif 3 in hand_dict.values() and 2 in hand_dict.values():
        hand_type = 5
    elif 3 in hand_dict.values():
        hand_type = 4
    elif list(hand_dict.values()).count(2) == 2:
        hand_type = 3
    elif 2 in hand_dict.values():
        hand_type = 2

    return hand_type

def get_hand_strength(hand):
    hand_strength = 0
    for k, card in enumerate(hand):
        hand_strength += 14**(5-k-1) * card_dict[card]
    return hand_strength

# Get the type of each hand
hand_types = []
hand_strs = []
for i in range(nhands):
    hand = hands[i]
    hand_types.append(get_hand_type(hand))
    hand_strs.append(get_hand_strength(hand))


hand_types = np.array(hand_types)
hands = np.array(hands)
bids = np.array(bids)
# Sort the hands and its bid by type

hands = hands[np.argsort(hand_types)]
bids = bids[np.argsort(hand_types)]
hand_strs = np.array(hand_strs)[np.argsort(hand_types)]
hand_types = hand_types[np.argsort(hand_types)]

output = open('Day7/output_prev.txt', 'w')
for element in zip(hands, hand_types, bids, hand_strs):
    output.write(str(element)+'\n')
output.close()


rank = 1
rank_list = []
for i in range(nhands-1):
    if hand_types[i] == rank:
        rank_list.append(i)
    elif hand_types[i] != rank:
        # We have gone to the next rank
        # Order the list of hands of the same type
        for j in range(len(rank_list)-1):
            for k in range(j+1, len(rank_list)):
                if hand_strs[rank_list[j]] > hand_strs[rank_list[k]]:
                    hands[rank_list[j]], hands[rank_list[k]] = hands[rank_list[k]], hands[rank_list[j]]
                    bids[rank_list[j]], bids[rank_list[k]] = bids[rank_list[k]], bids[rank_list[j]]
                    hand_types[rank_list[j]], hand_types[rank_list[k]] = hand_types[rank_list[k]], hand_types[rank_list[j]]
                    hand_strs[rank_list[j]], hand_strs[rank_list[k]] = hand_strs[rank_list[k]], hand_strs[rank_list[j]]
        rank += 1
        rank_list = []
        rank_list.append(i)



output = open('Day7/output.txt', 'w')
for k, element in enumerate(zip(hands, hand_types, bids, hand_strs)):
    output.write(str(element)+' '+str((k+1)*bids[k])+'\n')
    #print(element)
output.close()

# Get the points adding the bid by its rank
points = 0
for rank in range(1, len(hands)+1):
    points += rank * bids[rank-1]

print(points)


