import unittest
from unittest.mock import patch
from player import *
from deck import *

class MyTestCase(unittest.TestCase):
    def test_hit(self):
        with self.subTest():
            player = Player(True)
            deck = Deck()
            number_cards_before = len(player.hand.cards)
            player.hit(deck)
            self.assertEqual(number_cards_before + 1, len(player.hand.cards))
        with self.subTest():
            player = Player(False)
            deck = Deck()
            number_cards_before = len(player.hand.cards)
            player.hit(deck)
            self.assertEqual(number_cards_before + 1, len(player.hand.cards))
        with self.subTest():
            player = Player(False)
            deck = Deck()
            player.hand.value = 17
            number_cards_before = len(player.hand.cards)
            player.hit(deck)
            self.assertEqual(number_cards_before, len(player.hand.cards))
        with self.subTest():
            player = Player(False)
            deck = Deck()
            player.hand.value = 0
            number_cards_before = len(player.hand.cards)
            player.hit(deck)
            self.assertEqual(number_cards_before + 1, len(player.hand.cards))


if __name__ == '__main__':
    unittest.main()
