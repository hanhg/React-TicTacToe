
def convert_hand_to_num(hand):
    total = 0
    num_of_aces = 0
    for i in hand:
        if i[0] == "A":
            num_of_aces += 1
            total += 11
        else:
            try:
                if len(i) == 3:
                    total += 10
                else:
                    total += int(i[0])
            except ValueError:
                total += 10

    while num_of_aces > 0 and total > 21:
        total -= 10
        num_of_aces -= 1
    return total
