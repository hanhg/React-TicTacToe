from game import Game
import time

game = Game(users_money=100)
start = False

while True:
    answer = input("Would you like to play? (y/n) >>> ")
    if answer.upper() == "Y" or answer.upper() == "N":
        start = answer.upper() == "Y"
        break

while start:
    while True:
        game.display_users_money()
        answer = input("How much would you like to bet? >>> ")
        try:
            if int(answer) <= game.users_money:
                game.user_bet(int(answer))
            else:
                continue
            break
        except ValueError:
            print("Invalid Number input!")


    game.deal_cards()
    game.display_cards(reveal_dealer_cards=False)

    while game.get_user_hand_value() < 21:
        answer = input("Hit or Stand? (h/s) >>> ")
        if answer.upper() == "H":
            game.user_hit()
        elif answer.upper() == "S":
            break
        else:
            print('Invalid Input. Enter >>> "h" or "s"')
        game.display_cards(reveal_dealer_cards=False)


    time.sleep(1)
    game.display_cards(reveal_dealer_cards=True)
    while game.get_dealer_hand_value() < 18 and game.get_user_hand_value() <= 21 and game.get_user_hand_value() >= game.get_dealer_hand_value():
        time.sleep(2)
        game.dealer_hit()
        game.display_cards(reveal_dealer_cards=True)
        if game.get_user_hand_value() < game.get_dealer_hand_value() or game.get_dealer_hand_value() == 21:
            break


    if (game.get_user_hand_value() > 21
            or (game.get_user_hand_value() < game.get_dealer_hand_value()
                and game.get_dealer_hand_value() <= 21)):
        print("You Lost! :(")
        game.reset_pot()
    elif (game.get_user_hand_value() > game.get_dealer_hand_value()
          or game.get_dealer_hand_value() > 21):
        print("You Won! :)")
        game.user_win()
    else:
        print("Tie!")
        game.reset_pot()
    game.display_users_money()
    game.reset_game()
    time.sleep(2)
    while True:
        answer = input("Would you like to play again? (y/n) >>> ")
        if answer.upper() == "Y" or answer.upper() == "N":
            start = answer.upper() == "Y"
            break

