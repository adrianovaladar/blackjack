import unittest
from deck import *


class MyTestCase(unittest.TestCase):
    def test_init_deck(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_repeated_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), len(set(deck.cards)))

    def test_pick_card(self):
        deck = Deck()
        deck.pick_card()
        self.assertEqual(len(deck.cards), 51)

    def test_empty_deck(self):
        deck = Deck()
        tmp = 0
        for i in range(len(deck.cards) + 1):
            tmp = deck.pick_card()
        self.assertEqual(type(tmp), type('test'))


if __name__ == '__main__':
    unittest.main()
