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
    suits = [card.suit for card in all_cards]
    return any(suits.count(suit) >= 5 for suit in suits)