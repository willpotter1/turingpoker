from tg.types import PokerSharedState

def betStrength(state: PokerSharedState) -> int:
    """
    return a number that tells us how strong we think our opponent's hand
    is depending on their bet sizing. we should be comparing their bet sizing
    with our stack size, their stack size. We might want to think about how we
    can relate this betStrength funtction to the hand hiearchy to tell us which
    hand we want to call / fold depending on bet strenth.

    :param state: PokerSharedState
    :return: int
    
    """
    pot_size: int = state.pot
    opponent_bet: int = 0
    bot_name: str = open('BOT_NAME.txt', 'r').read()
    for playerID,player in enumerate(state.players):
        if player.id.lower() != bot_name.lower():
            opponent_index = playerID
            break
    state.players[opponent_index].current_bet 
    relative_bet_size: int = opponent_bet / pot_size

    print("relative " +  str(relative_bet_size))
    if relative_bet_size > 1.0:
        return 4    # Opponent likely has a strong hand.
    elif relative_bet_size > 0.6:
        return 3    # Consider folding weaker hands.
    elif relative_bet_size > 0.4:
        return 2    # Proceed cautiously.
    else:
        return 1    # Consider bluffing or raising.