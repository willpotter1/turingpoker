import numpy as np
from tg.types import ActionType, Card, Rank, Suit, PokerSharedState
from typing import List

#Playing in Big Blind
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
    
    for playerId, player in enumerate(state.players):
        if player.id == 'magnus poker':
            index = playerId
            break

    if state.dealer_position == index:
        action_matrix = button_matrix
    elif state.dealer_position != index:
        action_matrix = bb_matrix
    else:
        action_matrix = button_3bet_matrix
    
    action_value = get_hand_index(hand, action_matrix)
    #Fold
    if action_value ==0:
        return ActionType.FOLD.value
   #Call
    elif action_value == 1:
        current_bet = state.players[index].current_bet
        target_bet = state.target_bet
        if current_bet >= target_bet:
            return ActionType.CALL.value
        else:
            return ActionType.FOLD.value
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