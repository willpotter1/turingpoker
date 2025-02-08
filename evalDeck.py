from pokerHierarchy import PokerHierarchy
import tg.types as types

def evalDeck(state: types.PokerSharedState, hand: types.Card):
    """
    Evaluate the combination of Shared State and the player's hand.
    Return an Integer from the PokerHierarchy of the best combination.

    :param state: PokerSharedState
    :param hand: list[Card, Card]
    :return: int
    """
    return