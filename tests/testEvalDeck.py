import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from evalDeck import isFlush
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


    def test_full_house(self):
        # Community cards: Three, Four, Jack, Jack
        # Player's hand: Jack, Four
        # Full house: Three Jacks and two Fours
        state = PokerSharedState(
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
                Card(Rank.FOUR, Suit.HEARTS),
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.JACK, Suit.SPADES),
            ]
        )
        hand = [
            Card(Rank.JACK, Suit.DIAMONDS),
            Card(Rank.FOUR, Suit.CLUBS)
        ]
        self.assertTrue(isFullHouse(state, hand))

    def test_two_three_of_a_kind(self):
        # Community cards: Four, Four, Jack, Jack
        # Player's hand: Four, Jack
        # Two three-of-a-kinds: Three Fours and three Jacks
        state = PokerSharedState(
            dealer_position=0,
            small_blind=0,
            big_blind=0,
            pot=0,
            target_bet=0,
            players=[],
            round=PokerRound.RIVER,
            done=False,
            cards=[
                Card(Rank.FOUR, Suit.HEARTS),
                Card(Rank.FOUR, Suit.DIAMONDS),
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.JACK, Suit.SPADES),
            ]
        )
        hand = [
            Card(Rank.FOUR, Suit.CLUBS),
            Card(Rank.JACK, Suit.DIAMONDS)
        ]
        self.assertTrue(isFullHouse(state, hand))

    def test_no_full_house(self):
        # Community cards: Three, Four, Jack, Jack
        # Player's hand: Two, Three
        # No full house: Only two Jacks and no three-of-a-kind
        state = PokerSharedState(
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
                Card(Rank.FOUR, Suit.HEARTS),
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.JACK, Suit.SPADES),
            ]
        )
        hand = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.THREE, Suit.SPADES)
        ]
        self.assertFalse(isFullHouse(state, hand))

    def test_four_of_a_kind_and_pair(self):
        # Community cards: Jack, Jack, Jack, Four
        # Player's hand: Jack, Four
        # Four of a kind and a pair: Four Jacks and two Fours
        state = PokerSharedState(
            dealer_position=0,
            small_blind=0,
            big_blind=0,
            pot=0,
            target_bet=0,
            players=[],
            round=PokerRound.RIVER,
            done=False,
            cards=[
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.JACK, Suit.SPADES),
                Card(Rank.JACK, Suit.DIAMONDS),
                Card(Rank.FOUR, Suit.HEARTS),
            ]
        )
        hand = [
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.FOUR, Suit.SPADES)
        ]
        self.assertTrue(isFullHouse(state, hand))

    def test_three_pairs(self):
        # Community cards: Jack, Jack, Four, Four
        # Player's hand: Two, Two
        # Three pairs: No three-of-a-kind
        state = PokerSharedState(
            dealer_position=0,
            small_blind=0,
            big_blind=0,
            pot=0,
            target_bet=0,
            players=[],
            round=PokerRound.RIVER,
            done=False,
            cards=[
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.JACK, Suit.SPADES),
                Card(Rank.FOUR, Suit.HEARTS),
                Card(Rank.FOUR, Suit.DIAMONDS),
            ]
        )
        hand = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.SPADES)
        ]
        self.assertFalse(isFullHouse(state, hand))