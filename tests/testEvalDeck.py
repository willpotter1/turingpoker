import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from evalDeck import isFlush, isStraight, isFullHouse, isStraight, isStraight, isTwoPair
from tg import types
from tg.types import *

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

    def test_is_straight_using_all_cards(self):
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
                types.Card(types.Rank.ACE, types.Suit.HEARTS),
                types.Card(types.Rank.TWO, types.Suit.SPADES), 
                types.Card(types.Rank.THREE, types.Suit.HEARTS), 
                types.Card(types.Rank.FOUR, types.Suit.CLUBS)
            ]
        )
        hand = [
            types.Card(types.Rank.FIVE, types.Suit.DIAMONDS)
        ]
        self.assertTrue(isStraight(state, hand))
    def test_two_pair(self):
            # Community cards: Three, Four, Jack, Jack
            # Player's hand: Four, Two
            # Two pairs: Jacks and Fours
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
                    Card(Rank.THREE, Suit.HEARTS),
                    Card(Rank.FOUR, Suit.HEARTS),
                    Card(Rank.JACK, Suit.HEARTS),
                    Card(Rank.JACK, Suit.SPADES),
                ]
            )
            hand = [
                Card(Rank.FOUR, Suit.CLUBS),
                Card(Rank.TWO, Suit.HEARTS)
            ]
            self.assertTrue(isTwoPair(state, hand))

    def test_three_pair(self):
        # Community cards: Three, Four, Jack, Jack
        # Player's hand: Four, Three
        # Three pairs: Jacks, Fours, and Threes
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
                Card(Rank.THREE, Suit.HEARTS),
                Card(Rank.FOUR, Suit.HEARTS),
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.JACK, Suit.SPADES),
            ]
        )
        hand = [
            Card(Rank.FOUR, Suit.CLUBS),
            Card(Rank.THREE, Suit.SPADES)
        ]
        self.assertTrue(isTwoPair(state, hand))

    def test_one_pair(self):
        # Community cards: Three, Four, Jack, Jack
        # Player's hand: Two, Five
        # Only one pair: Jacks
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
                Card(Rank.THREE, Suit.HEARTS),
                Card(Rank.FOUR, Suit.HEARTS),
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.JACK, Suit.SPADES),
            ]
        )
        hand = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.FIVE, Suit.SPADES)
        ]
        self.assertFalse(isTwoPair(state, hand))

    def test_no_pair(self):
        # Community cards: Three, Four, Five, Six
        # Player's hand: Two, Seven
        # No pairs
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
                Card(Rank.THREE, Suit.HEARTS),
                Card(Rank.FOUR, Suit.HEARTS),
                Card(Rank.FIVE, Suit.HEARTS),
                Card(Rank.SIX, Suit.HEARTS),
            ]
        )
        hand = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.SPADES)
        ]
        self.assertFalse(isTwoPair(state, hand))

    def test_full_house(self):
        # Community cards: Three, Three, Jack, Jack
        # Player's hand: Jack, Four
        # Full house: Three Jacks and two Threes (not a two-pair)
        state = types.PokerSharedState(
            dealer_position=0,
            small_blind=0,
            big_blind=0,
            pot=0,
            target_bet=0,
            players=[],
            round=PokerRound.RIVER,
            done=False,
            cards=[
                Card(Rank.THREE, Suit.HEARTS),
                Card(Rank.THREE, Suit.DIAMONDS),
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.JACK, Suit.SPADES),
            ]
        )
        hand = [
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.FOUR, Suit.HEARTS)
        ]
        self.assertTrue(isTwoPair(state, hand))

if __name__ == '__main__':
    unittest.main()