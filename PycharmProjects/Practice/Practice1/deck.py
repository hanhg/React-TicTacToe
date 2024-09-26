import random

class Deck:
    cards = ["A♠", "A♣", "A♦", "A♥",
            "2♠", "2♣", "2♦", "2♥",
            "3♠", "3♣", "3♦", "3♥",
            "4♠", "4♣", "4♦", "4♥",
            "5♠", "5♣", "5♦", "5♥",
            "6♠", "6♣", "6♦", "6♥",
            "7♠", "7♣", "7♦", "7♥",
            "8♠", "8♣", "8♦", "8♥",
            "9♠", "9♣", "9♦", "9♥",
            "10♠", "10♣", "10♦", "10♥",
            "J♠", "J♣", "J♦", "J♥",
            "Q♠", "Q♣", "Q♦", "Q♥",
            "K♠", "K♣", "K♦", "K♥"]

    def __init__(self, shuffle):
        if(shuffle):
            self.shuffle_deck()

    def shuffle_deck(self):
        new_deck = []
        indexes = []
        for j in range(len(self.cards)):
            indexes.append(j)
        while len(indexes) > 0:
            choice = random.choice(indexes)
            choice_index = indexes.index(choice)
            del(indexes[choice_index])
            new_deck.append(self.cards[choice])
        self.cards = new_deck

