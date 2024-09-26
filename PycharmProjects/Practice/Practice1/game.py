from deck import Deck
from  converter import convert_hand_to_num

class Game:
    deck = Deck(shuffle=True)

    users_money = 0
    pot = 0

    dealer_cards = []
    user_cards = []

    def __init__(self, users_money=10):
        self.users_money = users_money

    def deal_cards(self):
        self.dealer_cards.append(self.deck.cards.pop())
        self.user_cards.append(self.deck.cards.pop())
        self.dealer_cards.append(self.deck.cards.pop())
        self.user_cards.append(self.deck.cards.pop())

    def dealer_hit(self):
        self.dealer_cards.append(self.deck.cards.pop())

    def user_hit(self):
        self.user_cards.append(self.deck.cards.pop())

    def clear_board(self):
        for i in self.dealer_cards:
            self.deck.cards.append(i)
        for i in self.user_cards:
                self.deck.cards.append(i)
        self.dealer_cards = []
        self.user_cards = []

    def reset_game(self):
        self.clear_board()
        self.deck.shuffle_deck()

    def get_hand_value(self, cards):
        return convert_hand_to_num(cards)

    def get_user_hand_value(self):
        return self.get_hand_value(self.user_cards)

    def get_dealer_hand_value(self):
        return self.get_hand_value(self.dealer_cards)

    def display_cards(self, reveal_dealer_cards):
        if reveal_dealer_cards:
            print("-------------------")
            string_dealer_cards = "Dealer: "
            for card in self.dealer_cards:
                string_dealer_cards += card + " "
            print(string_dealer_cards)
            string_user_cards = "User: "
            for card in self.user_cards:
                string_user_cards += card + " "
            print(string_user_cards)
            print("-------------------")
        else:
            print("-------------------")
            string_dealer_cards = f"Dealer: {self.dealer_cards[0]} ?"
            print(string_dealer_cards)
            string_user_cards = "User: "
            for card in self.user_cards:
                string_user_cards += card + " "
            print(string_user_cards)
            print("-------------------")

    def display_users_money(self):
        print("User's Money: " + str(self.users_money))

    def user_bet(self, bet_amount):
        self.users_money -= bet_amount
        self.pot += bet_amount * 2

    def reset_pot(self):
        self.pot = 0

    def user_win(self):
        self.users_money += self.pot
        self.reset_pot()
