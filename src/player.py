from deck import *


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.aces > 0 and self.value > 21:
            self.value -= 10


class Player:

    def __init__(self, is_player):
        self.hand = Hand()
        self.is_player = is_player
        self.total_chips = 100
        self.bet = 0
        if is_player:
            self.name = 'Player'
        else:
            self.name = 'Dealer'

    def win_bet(self):
        self.total_chips += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total_chips -= self.bet
        self.bet = 0

    def take_bet(self):
        while True:
            try:
                n = int(input('Input an integer (max {total}): '.format(total=self.total_chips)))
            except TypeError:
                print('An error occurred! Please try again!')
                continue
            else:
                if n > self.total_chips:
                    continue
                self.bet = n
                self.total_chips -= n
                break

    def hit(self, deck):
        if not self.is_player:
            if self.hand.value < 17:
                card = deck.pick_card()
                self.hand.add_card(card)
        else:
            card = deck.pick_card()
            if type(card) is Card:
                self.hand.add_card(card)
            elif type(card) is str:
                print(card)

    def hit_or_stand(self, deck):
        while True:
            option = input('Do you want to hit (h) or stand (s)? ')
            if option == 'h' or option != 'H':
                self.hit(deck)
                break
            elif option == 's' or option == 'S':
                break

    def show_some(self):
        print('Dealer hand')
        for i in range(len(self.hand.cards)):
            print('Card {index}'.format(index=i+1))
            if i == 0:
                print('Hidden card')
                continue
            print(self.hand.cards[i])

    def show_all(self):
        print('Player hand')
        for i in range(len(self.hand.cards)):
            print('Card {index}'.format(index=i+1))
            print(self.hand.cards[i])

    def show(self):
        if not self.is_player:
            self.show_some()
        else:
            self.show_all()

    def bust(self):
        return self.hand.value > 21
