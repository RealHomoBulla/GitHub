from random import *

p_chips = 1000
bet = 25
variables = tuple()

def deck():
    deck = []
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K', 'A']
    types = ['Clubs','Diamonds','Hearts','Spades']
    for type in types:
        for value in values:
            deck.append(value + ' of ' + type)
    return deck

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

def p_hand_creation(game_deck):
# Player's Hand creation:
    global p_hand
    p_card_1 = new_card(game_deck)
    remove_card(game_deck, p_card_1)
    p_card_2 = new_card(game_deck)
    remove_card(game_deck, p_card_2)
    print (f'\nYou\'ve got {p_card_1} and {p_card_2}.')
    p_value_1 = card_value(p_card_1)
    p_value_2 = card_value(p_card_2)
    p_total = p_value_1 + p_value_2
    print(f'Total is: {p_total}\n')
    p_hand = p_card_1, p_card_2, p_value_1, p_value_2, p_total
    return p_hand

def d_hand_creation(game_deck):
# Dealer's Hand creation:
    global d_hand
    d_card_1 = new_card(game_deck)
    remove_card(game_deck, d_card_1)
    d_card_2 = new_card(game_deck)
    remove_card(game_deck, d_card_2)
    print('Dealer draws two cards - one of them face up and one is a hole card (face down).')
    print(f'First card is {d_card_1}.\n')
    d_value_1 = card_value(d_card_1)
    d_value_2 = card_value(d_card_2)
    d_total = d_value_1 + d_value_2
    d_hand = d_card_1, d_card_2, d_value_1, d_value_2, d_total
    return d_hand

def p_hit(new_game, game_deck):
    p_card_extra = new_card(game_deck)
    remove_card(game_deck, p_card_extra)
    p_value_extra = card_value(p_card_extra)
    p_total += p_value_extra
    print(f'You\'ve got {p_card_extra}, and your current Total is {p_total}.')
    game_condition_check(p_total, d_total)
    return p_total

def p_stand(new_game):
    print(f'\nThe dealer discloses his hole card. It is {d_card_2}.')
    print(f'So he has {d_card_1} and {d_card_2} with a Total of {d_total}.\n')
    while d_total < 17:
        print('The Dealer hits again.')
        d_card_extra = new_card(game_deck)
        d_value_extra = card_value(d_card_extra)
        d_total += d_value_extra
        print(f'The card is {d_card_extra} and new Total is {d_total}\n')
        game_condition_check(p_total, d_total)
        return d_total

def game_condition_p_blackjack(p_chips, bet):
    print('Blackjack! You won! You gain 1.5 * Your Bet.')
    p_chips += (bet * 1.5)
    p_chips = round(p_chips)
    print(f'You currently have {p_chips} chips.')
    play_again_request()

def game_condition_d_blackjack(p_chips, bet):
    p_chips -= bet
    print(f'Dealer has Blackjack! You have lost your Bet of {bet}')
    print(f'Your account is {p_chips} chips now.')
    play_again_request()

def game_condition_push(p_chips):
    print('It\'s a Push! (draw) ')
    print(f'You still have {p_chips} chips.')
    play_again_request()

def game_condition_loss(new_game, p_chips, bet):
    p_chips -= bet
    print(f'You have {p_total} points. You have lost your Bet of {bet}')
    print(f'Your account is {p_chips} chips now.')
    play_again_request()

def game_condition_check(new_game):
    if p_total == 21 and d_total != 21:
        game_condition_p_blackjack(p_chips, bet)
    if p_total != 21 and d_total == 21:
        game_condition_d_blackjack(p_chips, bet)
    if p_total == 21 and d_total == 21:
        game_condition_push(p_chips)
    if p_total > 21:
        game_condition_loss(new_game, p_chips, bet)

def play_again_request():
    request = input('Would you like to play again? [y/n]: ')
    while request.lower().replace(' ', '') != 'y' or request.lower().replace(' ', '') not in 'yn':
        request = input('Would you like to play again? [y/n]: ')
        if request.lower().replace(' ', '') == 'y':
            another_game = new_game_creation()
        elif request.lower().replace(' ', '') == 'n':
            quit()
        else:
            continue

def new_game_creation():
    global game_deck
    game_deck = deck()
    global p_hand
    global d_hand
    p_hand = p_hand_creation(game_deck)
    d_hand = d_hand_creation(game_deck)
    new_game = p_hand, d_hand, game_deck
    return new_game
global new_game
new_game = new_game_creation()

print(new_game)


def game_body(new_game, p_chips, bet):

    while True:
        decision = input('Would you like to Hit or Stand? [h/s]: ')
        if decision.lower().replace(' ', '') == 'h':
            p_hit(new_game, game_deck)
            game_condition_check(new_game)
        if decision.lower().replace(' ', '') == 's':
            p_stand(new_game)
            game_condition_check(new_game)

game_body(new_game, p_chips, bet)