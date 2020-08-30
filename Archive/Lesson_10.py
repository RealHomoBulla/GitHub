# class Barbershop:
#     shampoo = 'H&S'
#     def __init__(self, cut  = 'Undercut'):
#         self.cut = cut
#
#     def sing(self):
#         print(f'How beautiful my haircut "{self.cut}" and what nice smell my shampoo "{self.shampoo}" has!')
#
#     def new_shampoo(self, s=''):
#         self.shampoo = s
#
# pasha = Barbershop('Zero')
# drus = Barbershop('Top Knot')
# mike = Barbershop('Short Cut')
#
# print(drus.cut)
# print(drus.shampoo)
# print(drus.sing())
# print(pasha.new_shampo('Palmolive'))
# print(pasha.sing())


class Player:

    def __init__(self, name='', money=0):
        self.name = name
        self.__money = money
        self.__cards = []
        self.__can_start_game = True
        self.__bet = 0

    def count_cards(self):
        v = 0
        for c in self.cards:
            v += c
        return v

    def get_money(self):
        return self.__money

    def __change_sum(self, delta=0):
        if self.__money + delta >= 0:
            self.__money += delta
        else:
            raise
    def add_card(self, card):
        if self.__bet > 0:
            self.__cards.append(card)

    def start_game(self, bet=0):
        if self.__can_start_game:
            if bet >=  self.__money:
                raise ValueError("You don't have enough money.")
            self.__bet = bet
            self.__can_start_game = False

    def win(self):
        self.__can_start_game = True
        self.__change_sum(bet)
        self.__bet = 0
        self.__cards = []

    def lose(self):
        self.__can_start_game = True
        self.__money -= self.__bet
        self.__bet = 0
        self.__cards = []

    def __repr__(self):
        return f"I am {self.name}. Hello)"
    def __str__(self):
        return f"I am {self.name}. Hello)"

cube = Player('Cube', 100)
cube.add_card(4)
print(cube.cards)
igor = Player('Igor', 150)
igor.add_card(10)
print(igor.cards)
igor.add_card(11)
print(igor.cards)
print(igor.count_cards())
