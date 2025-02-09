from pokerHierarchy import PokerHierarchy
import sys
import os
sys.path.append(os.path.join(os.curdir, 'template-python-poker-bot-cloned','tg'))
from tg import types

def evalDeck(state: types.PokerSharedState, hand: types.Card):
    """
    Evaluate the combination of Shared State and the player's hand.
    Return an Integer from the PokerHierarchy of the best combination.

    :param state: PokerSharedState
    :param hand: list[Card, Card]
    :return: int
    """
    return

def isFlush(state: types.PokerSharedState, hand: types.Card):
    all_cards = state.cards + hand
    first_suit = all_cards[0].suit
    return all(card.suit == first_suit for card in all_cards)