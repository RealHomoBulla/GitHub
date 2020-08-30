'''
It is a BlackJack game created by me completely from scratch.
I have checked some StackOverflow projects in the process, but it is a product of days of hard work
and difficulties.
I would like to improve it in future and to add some features and to fix possible bugs.
Materials used:

https://www.blackjackapprenticeship.com/how-to-play-blackjack/
https://en.wikipedia.org/wiki/Blackjack
(for blackjack rules)

https://codereview.stackexchange.com/questions/149889/simple-blackjack-game-in-python
(this project has helped me with code structure, but I overhauled it completely.
'''

from random import *

p_chips = 0
print('\nWelcome to The Hateful Eight Casino!\nPlease cash in. Minimum - 25$.')

# Take an initial amount of chips.
while True:
    p_chips = input('How much money do you have? ')
    if p_chips.isdigit() ==  False:
        print('Please, give me some amount of money to receive chips! What have you got? ')
        continue
    elif int(p_chips) < 25:
        print('You don\'t have enough money to play. Sorry.')
        continue
    elif int(p_chips) >= 25:
        p_chips = int(p_chips)
        print(f'\nOkay, great. You have {p_chips} chips.')
        break

# Now we need to define functions.

# I decided to make a function to change bet settings every new game.
def set_the_bet():
    while True:
        bet = input('\nHow much do you Bet? ')
        if bet.isdigit() == False:
            print('Please, Bet something! ')
            continue
        elif int(bet) < 25:
            print('I remind you: Minimum Bet is 25$.')
            continue
        elif int(bet) >= 25:
            bet = int(bet)
            print(f'\nOkay, great. Your standard Bet is set to {bet} chips.')
            return bet
bet = set_the_bet()

# Deck is created.
def deck():
    deck = []
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K', 'A']
    types = ['Clubs','Diamonds','Hearts','Spades']
    for type in types:
        for value in values:
            deck.append(value + ' of ' + type)
    return deck

# Cards are randomly chosen from the deck.
def new_card(deck):
    return deck[randint(0,len(deck)-1)]

# Every chosen card is being removed from the deck.
def remove_card(deck, card):
    return deck.remove(card)

'''
p_variable will mean variable or name related to a Player,
d_variable is variable or name related to a Dealer.
This function evaluates any card to some amount of points.
If Player has an Ace, it can be chosen to be 1 or 11 points. 
'''
def p_card_value(card):
    if card[:1] in ('23456789'):
        return int(card[:1])
    elif card[:1] in ('1JQK'):
        return 10
    elif card[:1] == 'A':
        print(f'There is {card}.')
        num = input('Do you want it to be 1 or 11 points? [1/11]: ')
        while num != '1' or num != '11':
            if num == '1':
                print(f'{card} will be equal to 1 now.')
                return int(1)
            elif num == '11':
                print(f'{card} will be equal to 11 now.')
                return int(11)
            else:
                num = input('1 or 11? ')

# If it is dealer's card, there should be no option to choose 1 or 11. It is chosen automatically.
def d_card_value(card):
    if card[:1] in ('23456789'):
        return int(card[:1])
    elif card[:1] in ('1JQK'):
        return 10
    elif card[:1] == 'A':
        return int(11)

# Player's Hand creation:
def p_hand_creation(game_deck, p_chips, bet):
    p_card_1 = new_card(game_deck)
    remove_card(game_deck, p_card_1)
    # I remove cards from deck so that no duplicates are possible.
    p_card_2 = new_card(game_deck)
    remove_card(game_deck, p_card_2)
    print('\n','-'*100)
    print (f'You\'ve got {p_card_1} and {p_card_2}.')
    p_value_1 = p_card_value(p_card_1)
    p_value_2 = p_card_value(p_card_2)
    p_total = p_value_1 + p_value_2
    print(f'*** Player\'s Total: {p_total} ***\n')
    return p_total, p_card_1, p_card_2, p_value_1, p_value_2

# Dealer's Hand creation:
def d_hand_creation(game_deck):
    d_card_1 = new_card(game_deck)
    remove_card(game_deck, d_card_1)
    d_card_2 = new_card(game_deck)
    remove_card(game_deck, d_card_2)
    input('Press [Enter] to see Dealer\'s Hand.\n')
    print('Dealer draws two cards - one of them Face Up and one is a Hole Card (Face Down).')
    print(f'First Dealer\'s card is {d_card_1}.\n')
    # Soft-17 Rule. If Dealer has an Ace and '6', then Ace = 1 and he can continue to Hit.
    if d_card_1[:1] == 'A' and d_card_1[:1] == '6':
        d_value_1 = 1
        d_value_2 = 6
        d_total = 7
    # If it's not an Ace and '6', cards are calculated in normal way.
    else:
        d_value_1 = d_card_value(d_card_1)
        d_value_2 = d_card_value(d_card_2)
        d_total = d_value_1 + d_value_2
    return d_total, d_card_1, d_card_2, d_value_1, d_value_2

# If player has to pull one more card, it should be added to previous.
def p_hit(game_deck, p_total):
    p_card_extra = new_card(game_deck)
    remove_card(game_deck, p_card_extra)
    p_value_extra = p_card_value(p_card_extra)
    p_total += p_value_extra
    print(f'\nYou\'ve got {p_card_extra}.\n*** Player\'s Total: {p_total}. ***\n')
    return p_total

# If player stopped hitting, Dealer has to hit up to 17 points.
def p_stand(game_deck, d_total, d_card_1, d_card_2):
    print(f'Dealer discloses his Hole Card. It is {d_card_2}.')
    print(f'So he has: {d_card_1} and {d_card_2}.')
    print(f'### Dealer\'s Total: {d_total} ###\n')
    input('Press [Enter] to continue.\n')
    while d_total < 17:
        print('The Dealer hits again.')
        d_card_extra = new_card(game_deck)
        d_value_extra = d_card_value(d_card_extra)
        d_total += d_value_extra
        print(f'The card is {d_card_extra}.\n### Dealer\'s Total: {d_total} ### \n')
    return d_total

# Player should be asked to Hit or Stand until he has > 21 points.
def hit_or_stand(game_deck, p_total):
    decision = ''
    while p_total < 21 or decision.lower().replace(' ', '') not in 'hs':
        decision = input('Would you like to Hit or Stand? [h/s]: ')
        if decision.lower().replace(' ', '') == 'h':
            p_total = p_hit(game_deck, p_total)
        elif decision.lower().replace(' ', '') == 's':
            break
    return p_total

# Various win-lose-draw conditions, which change Chips amount.
def game_condition_p_blackjack(p_chips, bet):
    print('You have 21! You won! You gain 1.5 * Your Bet.')
    p_chips += (bet * 1.5)
    p_chips = round(p_chips)
    print(f'You currently have {p_chips} chips.')
    return p_chips

def game_condition_d_blackjack(p_chips, bet):
    p_chips -= bet
    print(f'Dealer has 21! You have lost your Bet of {bet}.')
    print(f'Your account is {p_chips} chips now.')
    return p_chips

def game_condition_push(p_chips):
    print('It\'s a Push! (draw) ')
    print(f'You still have {p_chips} chips.')
    return p_chips

def game_condition_loss(p_chips, bet):
    p_chips -= bet
    print(f'You have lost your Bet of {bet}.')
    print(f'Your account is {p_chips} chips now.')
    return p_chips

def game_condition_win(p_chips, bet):
    p_chips += bet
    print(f'You have won your Bet of {bet}.')
    print(f'Your account is {p_chips} chips now.')
    return p_chips

# Function to check Player's points agaings Dealer's points and to start win-lose-draw conditions.
def game_condition_check(p_total, d_total, p_chips, bet):
    print(f'-*-*- Player has {p_total} and Dealer has {d_total} -*-*-\n')
    if p_total == 21 and d_total != 21:
        p_chips = game_condition_p_blackjack(p_chips, bet)
    elif p_total != 21 and d_total == 21:
        p_chips = game_condition_d_blackjack(p_chips, bet)
    elif p_total == d_total:
        p_chips = game_condition_push(p_chips)
    elif p_total > 21:
        p_chips = game_condition_loss(p_chips, bet)
    elif 21 > d_total > p_total:
        p_chips = game_condition_loss(p_chips, bet)
    elif 21 > p_total > d_total:
        p_chips = game_condition_win(p_chips, bet)
    elif p_total < 21 and d_total > 21:
        p_chips = game_condition_win(p_chips, bet)
    # After checking the condition, Chips amount should be returned for a next game.
    return p_chips

# Game should be re-playable, but should check the chips amount, if it's possible to continue the game.
def play_again_request(p_chips, bet):
    request = ''
    while request.lower().replace(' ', '') != 'y' or request.lower().replace(' ', '') not in 'yn':
        request = input('\nWould you like to play again? [y/n]: ')
        if request.lower().replace(' ', '') == 'y':
            if p_chips >= 25:
                print(f'\nOkay, you are starting the New Game with {p_chips} chips. Good luck!')
                # New Bet can be set, and new Game Deck created.
                bet = set_the_bet()
                p_chips = game_body(p_chips, bet)
            else:
                print('Sorry, you run out of chips. See you next time!')
                quit()
            return p_chips
        elif request.lower().replace(' ', '') == 'n':
            print(f'\nYou cash out with {p_chips}$. See you next time!')
            quit()

# Deck, player's and dealer's cards should be generated again for every game.
def new_game_creation():
    game_deck = deck()
    p_total, p_card_1, p_card_2, p_value_1, p_value_2 = p_hand_creation(game_deck, p_chips, bet)
    d_total, d_card_1, d_card_2, d_value_1, d_value_2 = d_hand_creation(game_deck)
    return game_deck, p_total, p_card_1, p_card_2, p_value_1, p_value_2, d_total, d_card_1, d_card_2, d_value_1, d_value_2

# This is the Main body of the game. It creates the Deck, Hands, starts the game and checks the win-lose-draw state.
def game_body(p_chips, bet):
    game_deck, p_total, p_card_1, p_card_2, p_value_1, p_value_2, d_total, d_card_1, d_card_2, d_value_1, d_value_2 = new_game_creation()
    while p_chips > 0:
        p_total = hit_or_stand(game_deck, p_total)
        if p_total > 21 and d_total <= 17:
            p_chips = game_condition_loss(p_chips, bet)
        elif p_total >= 21 and d_total >= 17:
            p_chips = game_condition_check(p_total, d_total, p_chips, bet)
        else:
            print(f'\nPlayer decided to Stand with {p_total} points.\n')
            d_total = p_stand(game_deck, d_total, d_card_1, d_card_2)
            p_chips = game_condition_check(p_total, d_total, p_chips, bet)
        # When the game is finished, it suggests to play it again.
        p_chips = play_again_request(p_chips, bet)

# Initial start of the game.
p_chips = game_body(p_chips, bet)