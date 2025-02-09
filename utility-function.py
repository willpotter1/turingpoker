def poker_utility(currBet: float, action: str):
    match (action):
        case "fold":
            return -currBet;
        case _:
            return currBet;