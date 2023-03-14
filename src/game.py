from player import *


def print_bust(player):
    print('{p} busts'.format(p=player.name))
    player.lose_bet()


def print_win(player):
    print('{p} wins'.format(p=player.name))
    player.win_bet()


def push():
    print('It is a push')


def main():
    player = Player(True)
    dealer = Player(False)
    deck = Deck()
    deck.shuffle()
    print('Blackjack game')
    for i in range(2):
        player.hand.add_card(deck.pick_card())
    for i in range(2):
        dealer.hand.add_card(deck.pick_card())
    player.take_bet()
    playing = True
    player.show()
    print('')
    dealer.show()
    while playing:
        player.hit_or_stand(deck)
        player.show()
        dealer.show()
        if player.hand.value > 21:
            print_bust(player)
            break
        elif player.hand.value <= 21:
            while dealer.hand.cards.value < 17:
                dealer.hit(deck)

main()
