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


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass


class Player:

    def __init__(self, is_player):
        self.hand = Hand()
        self.chips = Chips()
        self.is_player = is_player

    def take_bet(self):
        while True:
            try:
                n = int(input('Input an integer (max {total}): '.format(total=self.chips.total)))
            except TypeError:
                print('An error occurred! Please try again!')
                continue
            else:
                if n > self.chips.total:
                    continue
                self.chips.bet = n
                self.chips.total -= n
                break

    def hit(self, deck):
        if not self.is_player:
            if self.hand.value < 17:
                card = deck.pick_card()
                self.hand.add_card(card)
        else:
            card = deck.pick_card()
            self.hand.add_card(card)

    def hit_or_stand(self, deck):
        global playing
        pass
