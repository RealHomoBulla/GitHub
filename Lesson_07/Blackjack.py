import random
import time

card_deck = {
    "2 of hearts": [2], "3 of hearts": [3], "4 of hearts": [4], "5 of hearts": [5], "6 of hearts": [6],
    "7 of hearts": [7], "8 of hearts": [8], "9 of hearts": [9], "10 of hearts": [10], "Jack of hearts": [10],
    "Queen of hearts": [10], "King of hearts": [10], "Ace of hearts": [1, 10],
    "2 of spades": [2], "3 of spades": [3], "4 of spades": [4], "5 of spades": [5], "6 of spades": [6],
    "7 of spades": [7], "8 of spades": [8], "9 of spades": [9], "10 of spades": [10], "Jack of spades": [10],
    "Queen of spades": [10], "King of spades": [10], "Ace of spades": [1, 10],
    "2 of diamonds": [2], "3 of diamonds": [3], "4 of diamonds": [4], "5 of diamonds": [5], "6 of diamonds": [6],
    "7 of diamonds": [7], "8 of diamonds": [8], "9 of diamonds": [9], "10 of diamonds": [10], "Jack of diamonds": [10],
    "Queen of diamonds": [10], "King of diamonds": [10], "Ace of diamonds": [1, 10],
    "2 of clubs": [2], "3 of clubs": [3], "4 of clubs": [4], "5 of clubs": [5], "6 of clubs": [6], "7 of clubs": [7],
    "8 of clubs": [8], "9 of clubs": [9], "10 of clubs": [10], "Jack of clubs": [10], "Queen of clubs": [10],
    "King of clubs": [10], "Ace of clubs": [1, 10]
}
card_keys = [i for i in card_deck.keys()]


# print(card_keys[3])
def blackjack():
    print("--------------------------------------------------------")
    print("""
          \nWelcome to Lawless Casino! The game is blackjack. The goal is to get
          as close to 21 as possible without going over. If you hit blackjack,
          your bet pays out 3:2. We will let you play if you get in debt, but
          no more than $100 per bet: we don\'t encourage deadbeats."""
          )
    user_chips = 200
    bet = 25
    while True:  # deal + player's move
        user_chips = int(user_chips)
        drawn_cards = []
        if user_chips < 0:
            print("\nCurrent debt: -$" + str(abs(user_chips)) + ". Max bet in debt is $100.")
            bet = 25
        else:
            print("\nYou have: $" + str(user_chips) + " worth of chips.")
        if user_chips == 0:
            bet = 25
        if 0 < user_chips <= bet:
            bet = user_chips
        print("Current bet: $" + str(bet))
        while True:
            x = input("\nWhat do you want to bet? Press Enter to keep the same bet.")
            if x == "":
                break
            try:
                bet = int(x)
            except ValueError:
                print("\nYou have to enter a whole number!")
                continue
            if bet == 0:
                print("\nAnte up! You gotta bet something.")
                continue
            if bet < 0:
                bet = abs(bet)
            if bet > user_chips and user_chips > 0:
                print("\nNo betting more than you have!!")
                continue
            if bet > 100 and user_chips <= 0:
                print("\nYou\'re not betting more than $100 when you\'re in the hole!")
                continue
            break

        print("-------------------------------------------")
        print("\nDealing hand...")
        time.sleep(1)
        num_1 = random.randint(0, len(card_keys) - 1)
        num_2 = random.randint(0, len(card_keys) - 1)
        while num_1 == num_2:
            num_2 = random.randint(0, len(card_keys) - 1)
        dealer_hand = card_keys[num_1], card_keys[num_2]
        drawn_cards.append(card_keys[num_1])
        drawn_cards.append(card_keys[num_2])

        dealer_points = card_deck[card_keys[num_1]] + card_deck[card_keys[num_2]]
        # print(dealer_points)
        dealer_score = 0
        dealer_score_1 = 0
        if "Ace" in card_keys[num_1] or "Ace" in card_keys[num_2]:
            dealer_score_1 = card_deck[card_keys[num_1]][0]
            dealer_score_1 += card_deck[card_keys[num_2]][0]
        if "Ace" in card_keys[num_1] and "Ace" in card_keys[num_2]:
            dealer_score = 12
            dealer_score_1 = 2
        else:
            for i in dealer_points:
                dealer_score += i

        num_3 = random.randint(0, len(card_keys) - 1)
        num_4 = random.randint(0, len(card_keys) - 1)
        while card_keys[num_3] in drawn_cards:
            num_3 = random.randint(0, len(card_keys) - 1)
        drawn_cards.append(card_keys[num_3])
        while num_4 == num_3 or card_keys[num_4] in drawn_cards:
            num_4 = random.randint(0, len(card_keys) - 1)
        player_hand = card_keys[num_3], card_keys[num_4]
        drawn_cards.append(card_keys[num_4])
        player_points = card_deck[card_keys[num_3]] + card_deck[card_keys[num_4]]
        # print(player_points)

        player_score = 0
        player_score_1 = 0
        if "Ace" in card_keys[num_3] or "Ace" in card_keys[num_4]:
            player_score_1 = card_deck[card_keys[num_3]][0]
            player_score_1 += card_deck[card_keys[num_4]][0]
        if "Ace" in card_keys[num_3] and "Ace" in card_keys[num_4]:
            player_score = 12
            player_score_1 = 2
        else:
            for i in player_points:
                player_score += i
        print("\nDealer\'s hand: {0}".format(dealer_hand))
        if dealer_score_1 > 0:
            print("\nDealer\'s score: {0} or {1}".format(dealer_score_1, dealer_score))
        else:
            print("\nDealer\'s score: {0}".format(dealer_score))
        print("\nPlayer\'s hand: {0}".format(player_hand))
        if player_score_1 > 0:
            print("\nPlayer\'s score: {0} or {1}".format(player_score_1, player_score))
        else:
            print("\nPlayer\'s score: {0}".format(player_score))
        if dealer_score == 21 and player_score != 21:
            print("\nDealer wins. Shuffling for next hand...")
            print("\n-----------------------------------------")
            user_chips -= bet
            time.sleep(2)
            continue
        if player_score == 21 and dealer_score != 21:
            print("\nYou win! Shuffling for next hand...")
            print("\n-----------------------------------------")
            user_chips += (bet * 3 / 2)
            time.sleep(2)
            continue
        if dealer_score == 21 and player_score == 21:
            print("Push: bet returned. Shuffling for next hand...")
            print("\n-----------------------------------------")
            time.sleep(2)
            continue

        # ______________________________________________________________#
        valid_user_choices = ["1", "2", "3"]
        blackjack = False  # bet payout *3/2 if blackjack (so 10 wins 15)
        while True:  # card deal and player move
            temp = []
            num_aces = 0  # increments when ace on hit
            bust_variable = False
            double_bet = False
            blackjack = False
            print("\nDrawn cards so far: {0}".format(drawn_cards))
            if player_score_1 > 0:
                print("\nPlayer score: {0} or {1}.".format(player_score_1, player_score))
            else:
                print("\nPlayer score: {0}.".format(player_score))
            move = input("""
                \nWhat do you want to do? 1: Hit me! 2: Stay 3: double down!
                """)
            if move not in valid_user_choices:
                print("\nPlease enter a number 1-3.")
                continue

            if move == "1":
                draw_num = random.randint(0, len(card_keys) - 1)
                while card_keys[draw_num] in drawn_cards:
                    draw_num = random.randint(0, len(card_keys) - 1)
                drawn_cards.append(card_keys[draw_num])
                temp = card_deck[card_keys[draw_num]]
                print("--------------------------------------")
                print("\nDealing...")
                time.sleep(1)
                print("\nYou drew the {0}".format(card_keys[draw_num]))
                if "Ace" in card_keys[draw_num]:
                    if 11 + player_score <= 21:
                        temp = [11]
                        num_aces += 1
                    if 11 + player_score > 21 and player_score_1 == 0:
                        temp = [1]
                    if player_score + 11 > 21 and 0 < player_score_1 <= 10:
                        temp = [11]
                        num_aces += 1
                    else:
                        temp = [1]
                if player_score_1 > 0:
                    player_score_1 += temp[0]
                player_score += temp[0]
                if player_score == 21:
                    print("\nBlackjack!! Dealer\'s turn...")
                    final_player_score = player_score
                    blackjack = True
                    time.sleep(1)
                    break
                if player_score_1 == 21:
                    print("\nBlackjack!! Dealer\'s turn...")
                    final_player_score = player_score_1
                    blackjack = True
                    time.sleep(1)
                    break
                if player_score > 21 and player_score_1 == 0 and num_aces > 0:
                    player_score - 10
                    num_aces = 0
                    continue
                if player_score_1 > 21 and num_aces > 0:
                    player_score_1 - 10
                    player_score - 10
                    num_aces = 0
                    continue
                if player_score > 21 and player_score_1 == 0:
                    print("\n{0}:You bust. Too bad.".format(str(player_score)))
                    user_chips -= bet
                    bust_variable = True
                    break
                if player_score_1 > 21:
                    print("{0}:You bust. Too bad.".format(str(player_score_1)))
                    user_chips -= bet
                    bust_variable = True
                    break
                continue

            if move == "2":
                if player_score <= 21:
                    final_player_score = player_score
                    print("\nHolding at current score: {0}".format(player_score))
                if player_score > 21:
                    print("\nHolding at current score: {0}".format(player_score_1))
                    final_player_score = player_score_1
                print("\nDealer\'s turn...")
                time.sleep(1)
                break

            if move == "3":
                draw_num = random.randint(0, len(card_keys) - 1)
                while card_keys[draw_num] in drawn_cards:
                    draw_num = random.randint(0, len(card_keys) - 1)
                drawn_cards.append(card_keys[draw_num])
                print("\nDouble down! Dealing...")
                double_bet = True
                time.sleep(1)
                print("Your card: the {0}".format(card_keys[draw_num]))
                temp = card_deck[card_keys[draw_num]]

                if "Ace" in card_keys[draw_num]:
                    if 11 + player_score > 21 and player_score_1 == 0:
                        temp = [1]
                    if 11 + player_score <= 21:
                        temp = [11]
                    if player_score > 21 and 11 + player_score_1 <= 21:
                        temp = [11]
                    else:
                        temp = [1]

                print("Temp:{0}".format(temp))
                if player_score_1 > 0:
                    player_score_1 += temp[0]
                player_score += temp[0]
                if player_score > 21 and player_score_1 > 0 and player_score_1 < 21:
                    print("\nScore: {0}".format(player_score_1))
                    final_player_score = player_score_1
                else:
                    print("\nScore: {0}".format(player_score))
                    final_player_score = player_score
                if player_score > 21 and player_score_1 == 0:
                    print("\nYou bust. Too bad.")
                    user_chips -= (bet * 2)
                    bust_variable = True
                if player_score_1 > 21:
                    print("\nYou bust. Too bad.")
                    user_chips -= (bet * 2)
                    bust_variable = True
                if player_score == 21 or player_score_1 == 21:
                    final_player_score = 21
                    print("\nBlackjack! Dealer\'s turn...")
                    blackjack = True
                    time.sleep(1)
                break
        # __________________________dealer move__________________________#
        while bust_variable == False:
            num_aces = 0
            if 17 <= dealer_score <= 21:
                dealer_final_score = dealer_score
                print("\nDealer holds at {0}".format(dealer_score))
                break
            if dealer_score > 21 and dealer_score_1 == 0:
                print("\nDealer busts. You win!")
                if double_bet and blackjack:
                    user_chips += (bet * 3)
                elif double_bet:
                    user_chips += (bet * 2)
                elif blackjack:
                    user_chips += (bet * 3 / 2)
                else:
                    user_chips += bet
                bust_variable = True
                break
            if 17 <= dealer_score_1 <= 21:
                dealer_final_score = dealer_score_1
                print("\nDealer holds at {0}".format(dealer_score_1))
                break
            if dealer_score_1 > 21:
                print("\nDealer busts. You win!")
                if double_bet and blackjack:
                    user_chips += (bet * 3)
                elif double_bet:
                    user_chips += (bet * 2)
                elif blackjack:
                    user_chips += (bet * 3 / 2)
                else:
                    user_chips += bet
                bust_variable = True
                break
            print("\nDealer\'s score: {0}".format(dealer_score))
            if dealer_score_1 > 0:
                print("or {0}".format(dealer_score_1))
            print("----------------------------------")
            draw_num = random.randint(0, len(card_keys) - 1)
            while card_keys[draw_num] in drawn_cards:
                draw_num = random.randint(0, len(card_keys) - 1)
            drawn_cards.append(card_keys[draw_num])
            temp = card_deck[card_keys[draw_num]]
            print("\nDealing...")
            time.sleep(1)
            print("\nDealer draws the {0}".format(card_keys[draw_num]))
            if "Ace" in card_keys[draw_num]:
                if 11 + dealer_score <= 21:
                    temp = [11]
                    num_aces += 1
                if 11 + dealer_score > 21 and dealer_score_1 == 0:
                    temp = [1]
                if dealer_score + 11 > 21 and 0 < dealer_score_1 <= 10:
                    temp = [11]
                    num_aces += 1
                else:
                    temp = [1]
            if dealer_score_1 > 0:
                dealer_score_1 += temp[0]
            dealer_score += temp[0]
            continue

            # -----------final score if not a bust---------#
        if bust_variable == False:
            print("\nFinal score - You:{0}  Dealer:{1}".format(final_player_score, dealer_final_score))
            if dealer_final_score == final_player_score:
                print("\nPush. Bet returned.")

            if dealer_final_score > final_player_score:
                print("\nHouse wins.")
                if double_bet:
                    user_chips -= (bet * 2)
                if blackjack:
                    user_chips -= (bet * 3 / 2)
                else:
                    user_chips -= bet

            if dealer_final_score < final_player_score:
                print("\n You win!")
                if double_bet and blackjack:
                    user_chips += (bet * 3)
                elif double_bet:
                    user_chips += (bet * 2)
                elif blackjack:
                    user_chips += (bet * 3 / 2)
                else:
                    user_chips += bet

        # ________________final loop: play next hand or cash out________#
        continue_choice = ["Y", "y", "N", "n"]
        while True:
            cont = input("\nDeal again? Press Y to deal a new hand. Press N to cash out.")
            if cont not in continue_choice:
                print("Please choose Y or N.")
                continue
            if cont in continue_choice:
                break
        if cont == "Y" or cont == "y":
            continue
        if cont == "N" or cont == "n":
            if user_chips > 200:
                print("\nCongratulations, your winnings are $" + str(int(user_chips) - 200) + "! Thanks for playing.")
                break
            if user_chips < 200 and user_chips > 0:
                print("\nNot your lucky day. At least you still kept $" + str(
                    int(user_chips)) + ". Thank\'s for playing!")
                break
            if user_chips == 200:
                print("\nYou broke even. No loss, no gain. Thanks for playing!")
                break
            if user_chips == 0:
                print("\nThanks so much for losing all your money with us!")
                break
            else:
                print("\nBetter luck next time. You owe Lawless Casino $" + str(
                    abs(int(user_chips))) + ". Bruno will be by to collect within the next 24 hours.")
                break


blackjack()