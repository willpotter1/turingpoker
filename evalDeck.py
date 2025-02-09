from pokerHierarchy import PokerHierarchy
from tg import types

def evalDeck(state: types.PokerSharedState, hand: types.Card):
    """
    Evaluate the combination of Shared State and the player's hand.
    Return an Integer from the PokerHierarchy of the best combination.

    :param state: PokerSharedState
    :param hand: list[Card, Card]
    :return: int
    """    
    if isFullHouse(state, hand):
        return 7
    elif isFlush(state, hand):
        return 6
    elif isStraight(state, hand):
        return 5
    elif isTriple(state, hand):
        return 4
    elif isTwoPair(state, hand):
        return 3
    elif isPair(state, hand):
        return 2
    else: 
        return 1



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
    return False

def isPair(state, hand):
    all_cards = state.cards + hand
    ranks = [0 for i in range(13)]
    for card in all_cards:
        ranks[card.rank - 1] += 1
    has_pair = any(count >= 2 for count in ranks)
    return has_pair


def isTwoPair(state, hand):
    all_cards = state.cards + hand
    ranks = [0 for i in range(13)]
    for card in all_cards:
        ranks[card.rank - 1] += 1
    has_pair = any(count >= 2 for count in ranks)
    if has_pair:
        pair_index = next(i for i, count in enumerate(ranks) if count >=2)
        has_second_pair = any(count >= 2 and i!= pair_index for i, count in enumerate(ranks))
        return has_second_pair
    return False

def isTriple(state, hand):
    all_cards = state.cards + hand
    ranks = [0 for i in range(13)]
    for card in all_cards:
        ranks[card.rank - 1] += 1
    has_pair = any(count >= 3 for count in ranks)
    return has_pair

def isStraight(state: types.PokerSharedState, hand: list[types.Card]):
    all_cards = state.cards + hand;
    # Extract and Preprocess Ranks
    ranks: set[types.Rank] = set(); # Use a set to avoid duplicates
    for card in all_cards:
        match (card.rank):
            case types.Rank.JACK:
                ranks.add(11);
                continue;
            case types.Rank.QUEEN:
                ranks.add(12);
                continue;
            case types.Rank.KING:
                ranks.add(13);
                continue;
            case types.Rank.ACE:
                ranks.add(1);
                continue;
            case _:
                ranks.add(card.rank);
    ranks_list:list[types.Card] = sorted(ranks); # Sort the ranks
    # Check for a Straight
    for i in range(len(ranks_list) - 4):
        if ranks_list[i] == ranks_list[i + 1] - 1 == ranks_list[i + 2] - 2 == ranks_list[i + 3] - 3 == ranks_list[i + 4] - 4:
            return True;
    return False;