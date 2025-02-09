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
    cards = [hand[0], hand[1]]

    if state.round == 'flop': 
        cards.append(state.cards[0])
        cards.append(state.cards[1])
        cards.append(state.cards[2])
    elif state.round == 'turn':
        cards.append(state.cards[0])
        cards.append(state.cards[1])
        cards.append(state.cards[2])
        cards.append(state.cards[3])
    elif state.round == 'river':
        cards.append(state.cards[0])
        cards.append(state.cards[1])
        cards.append(state.cards[2])
        cards.append(state.cards[3])
        cards.append(state.cards[4])
    return

def isFlush(state: types.PokerSharedState, hand: types.Card):
    all_cards = state.cards + hand
    suits = [card.suit for card in all_cards]
    return any(suits.count(suit) >= 5 for suit in suits)


def isFullHouse(state, hand):
    all_cards = state.cards + hand
    ranks = [0 for i in range(13)]
    for card in all_cards:
        ranks[card.rank - 1] += 1
    
    has_three_or_more = any(count >= 3 for count in ranks)
    if has_three_or_more:
        # Find the index of the first rank with 3 or more cards
        three_index = next(i for i, count in enumerate(ranks) if count >= 3)
        # Check if there's another rank with 2 or more cards (excluding the first three)
        has_pair = any(count >= 2 and i != three_index for i, count in enumerate(ranks))
        return has_pair

    return false
