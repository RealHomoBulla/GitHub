from random import *

global p_chips
global bet
# global p_total
# global d_total
# global p_card_1
# global p_card_2
# global d_card_1
# global d_card_2
# global p_value_1
# global p_value_2
# global d_value_2
# global d_value_2

p_chips = 1000
bet = 25
# p_total = 0
# d_total = 0
# p_card_1 = 0
# p_card_2 = 0
# d_card_1 = 0
# d_card_2 = 0
# p_value_1 = 0
# p_value_2 = 0
# d_value_2 = 0
# d_value_2 = 0

def play_again_request():
    request = input('Would you like to play again? [y/n]: ')
    while request.lower().replace(' ', '') != 'y' or request.lower().replace(' ', '') != 'n':
        continue
        if request.lower().replace(' ', '') == 'y':
            blackjjack_game()
        elif request.lower().replace(' ', '') == 'n':
            quit()

def deck():
    deck = []
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K', 'A']
    types = ['Clubs','Diamonds','Hearts','Spades']
    for type in types:
        for value in values:
            deck.append(value + ' of ' + type)
    return deck
game_deck = deck()

def new_card(deck):
    return deck[randint(0,len(deck)-1)]

def remove_card(deck, card):
    return deck.remove(card)

def card_value(card):
    if card[:1] in ('23456789'):
        return int(card[:1])
    elif card[:1] in ('1JQK'):
        return 10
    elif card[:1] == 'A':
        # need to make it not callable when it is dealer's card, so that dealer choose automatically
        print(f'One of your cards is {card}.')
        num = input('Do you want this to be 1 or 11 points? [1/11]: ')
        while num != '1' or num != '11':
            if num == '1':
                print(f'{card} will be equal to 1 now.\n')
                return int(1)
            elif num == '11':
                print(f'{card} will be equal to 11 now.\n')
                return int(11)
            else:
                num = input('1 or 11? ')

def p_hand_creation():
# Player's Hand creation:
    p_card_1 = new_card(game_deck)
    remove_card(game_deck, p_card_1)
    p_card_2 = new_card(game_deck)
    remove_card(game_deck, p_card_2)
    print (f'\nYou\'ve got {p_card_1} and {p_card_2}.')
    p_value_1 = card_value(p_card_1)
    p_value_2 = card_value(p_card_2)
    p_total = p_value_1 + p_value_2
    print(f'Total is: {p_total}\n')
    return p_card_1, p_card_2, p_value_1, p_value_2, p_total

def d_hand_creation():
# Dealer's Hand creation:
    d_card_1 = new_card(game_deck)
    remove_card(game_deck, d_card_1)
    d_card_2 = new_card(game_deck)
    remove_card(game_deck, d_card_2)
    print('Dealer draws two cards - one of them face up and one is a hole card (face down).')
    print(f'First card is {d_card_1}.\n')
    d_value_1 = card_value(d_card_1)
    d_value_2 = card_value(d_card_2)
    d_total = d_value_1 + d_value_2
    return d_card_1, d_card_2, d_value_1, d_value_2, d_total

def p_hit():
    p_card_extra = new_card(game_deck)
    remove_card(game_deck, p_card_extra)
    p_value_extra = card_value(p_card_extra)
    p_total += p_value_extra
    print(f'You\'ve got {p_card_extra}, and your current Total is {p_total}.')
    game_condition_check()
    return p_total

def p_stand():
    print(f'\nThe dealer discloses his hole card. It is {d_card_2}.')
    print(f'So he has {d_card_1} and {d_card_2} with a Total of {d_total}.\n')
    while d_total < 17:
        print('The Dealer hits again.')
        d_card_extra = new_card(game_deck)
        d_value_extra = card_value(d_card_extra)
        d_total += d_value_extra
        print(f'The card is {d_card_extra} and new Total is {d_total}\n')
        game_condition_check()

def game_condition_p_blackjack():
    print('Blackjack! You won! You gain 1.5 * Your Bet.')
    p_chips += (bet * 1.5)
    p_chips = round(p_chips)
    print(f'You currently have {p_chips} chips.')
    play_again_request()

def game_condition_d_blackjack():
    p_chips -= bet
    print(f'Dealer has Blackjack! You have lost your Bet of {bet}')
    print(f'Your account is {p_chips} chips now.')
    play_again_request()

def game_condition_push():
    print('It\'s a Push! (draw) ')
    print(f'You still have {p_chips} chips.')
    play_again_request()

def game_condition_loss():
    p_chips -= bet
    print(f'You have {p_total} points. You have lost your Bet of {bet}')
    print(f'Your account is {p_chips} chips now.')
    play_again_request()

def game_condition_check():
    if p_total == 21 and d_total != 21:
        game_condition_p_blackjack()
    if p_total != 21 and d_total == 21:
        game_condition_d_blackjack()
    if p_total == 21 and d_total == 21:
        game_condition_push()
    if p_total > 21:
        game_condition_loss()

def game_body():
    while True:
        p_card_1, p_card_2, p_value_1, p_value_2, p_total = p_hand_creation()
        d_card_1, d_card_2, d_value_1, d_value_2, d_total = d_hand_creation()
        decision = input('Would you like to Hit or Stand? [h/s]: ')
        if decision.lower().replace(' ', '') == 'h':
            p_hit()
            game_condition_check()
        if decision.lower().replace(' ', '') == 's':
            p_stand()
            game_condition_check()

game_body()