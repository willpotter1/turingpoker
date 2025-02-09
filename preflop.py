import numpy as np
from tg.types import ActionType, Card, Rank, Suit, PokerSharedState
from typing import List

# Playing in Big Blind
# 2: Raise, 1: Call, 0: Fold
button_matrix = np.array([
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,0,2,2,2,2,2,2,2,2],
    [2,2,2,2,0,0,0,0,2,2,2,2,2],
    [2,2,2,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,2]
])

bb_matrix = np.array([
    [2,2,2,2,2,2,1,1,1,2,2,2,1],
    [2,2,2,2,2,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,1,1,1,1,1,1,1,1],
    [2,1,1,2,2,2,1,1,1,1,1,1,1],
    [1,1,1,1,2,2,1,1,1,1,1,1,1],
    [1,1,1,1,1,2,2,2,2,1,1,1,1],
    [1,1,1,1,1,1,2,2,2,1,1,1,1],
    [1,1,1,1,1,1,1,2,2,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,2,1,1,1],
    [1,1,1,0,0,0,0,1,1,1,2,1,1],
    [1,1,1,0,0,0,0,0,0,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1]
])
button_3bet_matrix = np.array([
    [2,2,2,1,1,1,1,1,1,1,1,1,1],
    [2,2,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,2,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,2,1,1,1,1,1,1,0,0,0],
    [1,1,1,1,2,1,1,1,1,0,0,0,0],
    [1,0,0,0,0,1,1,1,1,0,0,0,0],
    [1,0,0,0,0,0,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1]
])

# function that inputs the current position, hand, 
# Poisitions: big_blind, dealer_position


def preflop_action2(state : PokerSharedState, hand: List[Card]):
    
    index = 0
    op_index = 0
    for playerId, player in enumerate(state.players):
        bot_name: str = open('BOT_NAME.txt', 'r').read()
        if player.id.lower() == bot_name.lower():
            index = playerId
        else: 
            op_index =  playerId

    # bb calc
    op_bb = state.players[op_index].current_bet / state.big_blind

    if (op_bb <= 5): 
        #use loosest chart
        action_matrix = button_matrix
        print("using loose chart")
    elif (5 < op_bb <= 15): 
        # use medium chart
        action_matrix = bb_matrix
        print("using mid chart")
    else: 
        #using tighest chart
        action_matrix = button_3bet_matrix
        print("using tight chart")
    
    action_value = get_hand_index(hand, action_matrix)
    
    print("opponent big blind bet " + str(op_bb))
    if action_value == 0:
        if (op_bb <= 1):
            return ActionType.CALL.value
        else:
            return ActionType.FOLD.value

    elif action_value == 1:
        return ActionType.CALL.value
    #Raise
    elif action_value == 2:
        if np.array_equal(action_matrix, button_matrix) == True:
            raise_amount = state.target_bet * 2
        elif np.array_equal(action_matrix, bb_matrix) == True:
            raise_amount = state.target_bet * 9
        elif np.array_equal(action_matrix, button_3bet_matrix) == True:
            raise_amount = state.target_bet * 20
        
        stack_size = state.players[index].stack
        if stack_size >= raise_amount:
            return ActionType.RAISE.value, raise_amount
        else:
            return ActionType.CALL.value

def get_hand_index(hand: List[Card], action_matrix: np.array):
    # index for the matrix
    rank_to_index = {
    Rank.ACE: 0,
    Rank.KING: 1,
    Rank.QUEEN: 2,
    Rank.JACK: 3,
    Rank.TEN: 4,
    Rank.NINE: 5,
    Rank.EIGHT: 6,
    Rank.SEVEN: 7,
    Rank.SIX: 8,
    Rank.FIVE: 9,
    Rank.FOUR: 10,
    Rank.THREE: 11,
    Rank.TWO: 12,
    }

    rev = False
    if hand[0].suit == hand[1].suit:
        rev = True
    
    r1= hand[0].rank
    r2 = hand[1].rank
    if rev:
        if r1 > r2:
            return action_matrix [rank_to_index[r2]][rank_to_index[r1]]
        else:
            return action_matrix [rank_to_index[r1]][rank_to_index[r2]]
    return action_matrix [rank_to_index[r1]][rank_to_index[r2]]
