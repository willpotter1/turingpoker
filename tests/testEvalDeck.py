import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from evalDeck import isFlush, isStraight, isFullHouse, isStraight
from tg import types

class TestEvalDeck(unittest.TestCase):
    def test_is_flush_true_using_all_cards(self):
        state = types.PokerSharedState(
            dealer_position=0, 
            small_blind=0, 
            big_blind=0, 
            pot=0, 
            target_bet=0, 
            players=[], 
            round=types.PokerRound.FLOP, 
            done=False, 
            cards=[
                types.Card(types.Rank.THREE, types.Suit.HEARTS), 
                types.Card(types.Rank.FOUR, types.Suit.HEARTS), 
                types.Card(types.Rank.FIVE, types.Suit.HEARTS)
            ]
        )
        hand = [
            types.Card(types.Rank.ACE, types.Suit.HEARTS), 
            types.Card(types.Rank.TWO, types.Suit.HEARTS)
        ]
        self.assertTrue(isFlush(state, hand))

    def test_is_flush_false_using_all_cards(self):
        state = types.PokerSharedState(
            dealer_position=0, 
            small_blind=0, 
            big_blind=0, 
            pot=0, 
            target_bet=0, 
            players=[], 
            round=types.PokerRound.FLOP, 
            done=False, 
            cards=[
                types.Card(types.Rank.THREE, types.Suit.HEARTS), 
                types.Card(types.Rank.FOUR, types.Suit.HEARTS), 
                types.Card(types.Rank.FIVE, types.Suit.HEARTS)
            ]
        )
        hand = [
            types.Card(types.Rank.ACE, types.Suit.HEARTS), 
            types.Card(types.Rank.TWO, types.Suit.CLUBS)
        ]
        self.assertFalse(isFlush(state, hand))

    def test_is_flush_false_have_spare_cards(self):
        state = types.PokerSharedState(
            dealer_position=0, 
            small_blind=0, 
            big_blind=0, 
            pot=0, 
            target_bet=0, 
            players=[], 
            round=types.PokerRound.RIVER, 
            done=False, 
            cards=[
                types.Card(types.Rank.THREE, types.Suit.HEARTS), 
                types.Card(types.Rank.FOUR, types.Suit.HEARTS), 
                types.Card(types.Rank.FIVE, types.Suit.HEARTS),
                types.Card(types.Rank.JACK, types.Suit.SPADES),
                types.Card(types.Rank.KING, types.Suit.CLUBS)
            ]
        )
        hand = [
            types.Card(types.Rank.ACE, types.Suit.HEARTS), 
            types.Card(types.Rank.TWO, types.Suit.CLUBS)
        ]
        self.assertFalse(isFlush(state, hand))

    def test_is_flush_true_have_spare_cards(self):
        state = types.PokerSharedState(
            dealer_position=0, 
            small_blind=0, 
            big_blind=0, 
            pot=0, 
            target_bet=0, 
            players=[], 
            round=types.PokerRound.RIVER, 
            done=False, 
            cards=[
                types.Card(types.Rank.THREE, types.Suit.HEARTS), 
                types.Card(types.Rank.FOUR, types.Suit.HEARTS),
                types.Card(types.Rank.JACK, types.Suit.HEARTS),
                types.Card(types.Rank.JACK, types.Suit.SPADES),
            ]
        )
        hand = [
            types.Card(types.Rank.ACE, types.Suit.HEARTS), 
            types.Card(types.Rank.TWO, types.Suit.HEARTS)
        ]
        self.assertTrue(isFlush(state, hand))

if __name__ == '__main__':
    unittest.main()