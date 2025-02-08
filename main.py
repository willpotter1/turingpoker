#!/usr/bin/env python3
import asyncio
import argparse

from tg.bot import Bot
import time

from tg.types import PokerRound, ActionType, Action

parser = argparse.ArgumentParser(
    prog='Template bot',
    description='A Turing Games poker bot that always checks or calls, no matter what the target bet is (it never folds and it never raises)')

parser.add_argument('--port', type=int,
                    help='The port to connect to the server on')
parser.add_argument('--host', type=str, default='localhost',
                    help='The host to connect to the server on')
parser.add_argument('--room', type=str, default='my-new-room',
                    help='The room to connect to')
parser.add_argument('--party', type=str, default='poker',
                    help='The party to connect to')
parser.add_argument('--key', type=str, default='',
                    help='The key for authentication')

args = parser.parse_args()

# Always call
class TemplateBot(Bot):
    def act(self, state, hand):
        """Decide how to act based on round and a naive post-flop strategy."""

        print('asked to act')
        print('acting', state, hand, self.my_id)

        # 1. If we're still pre-flop, let's do something simple:
        if state.round == PokerRound.PRE_FLOP:
            print("Pre-flop: always call.")
            return {'type': ActionType.CALL.value}

        # 2. Once we have community cards (FLOP, TURN, RIVER),
        #    compute a naive hand strength:
        strength = naive_hand_strength(hand, state.cards)
        pot_size = state.pot
        target_bet = state.target_bet

        print(f"Post-flop round: {state.round}")
        print(f"Hand strength: {strength:.2f}, Pot: {pot_size}, Target bet: {target_bet}")

        # Decide action based on naive threshold
        if strength < 0.3:
            print("Folding due to weak hand.")
            return {'type': ActionType.FOLD.value}

        elif strength < 0.6:
            print("Calling with mediocre hand.")
            return {'type': ActionType.CALL.value}

        else:
            # Attempt a raise
            # Let's raise approximately half of the current pot
            raise_amount = pot_size // 2

            # Make sure we're actually raising above the call
            if raise_amount <= target_bet:
                raise_amount = target_bet + 10  # e.g. 10 chips on top

            print(f"Raising to {raise_amount}")
            return {'type': ActionType.RAISE.value, 'amount': raise_amount}


    def opponent_action(self, action, player):
        print('opponent action?', action, player)

    def game_over(self, payouts):
        print('game over', payouts)

    def start_game(self, my_id):
        self.my_id = my_id
        print('start game', my_id)

if __name__ == "__main__":
    bot = TemplateBot(args.host, args.port, args.room, args.party, args.key)
    asyncio.run(bot.start())

def naive_hand_strength(hole_cards, community_cards):
    """
    Return a naive measure of hand strength from 0.0 to 1.0
    based on how many cards of the same rank you have.
    This ignores straights, flushes, etc.
    """

    # Combine hole + community
    all_cards = list(hole_cards) + list(community_cards)

    # Tally ranks
    rank_count = {}
    for card in all_cards:
        rank_count[card.rank] = rank_count.get(card.rank, 0) + 1

    # Find the max "of a kind"
    max_of_a_kind = max(rank_count.values()) if rank_count else 1

    # Count how many pairs, trips, quads
    pairs = sum(1 for count in rank_count.values() if count == 2)
    triples = sum(1 for count in rank_count.values() if count == 3)
    quads = sum(1 for count in rank_count.values() if count == 4)

    # Super-naive approach
    if quads >= 1:
        return 0.95
    elif triples >= 1 and pairs >= 1:
        # full house
        return 0.90
    elif triples >= 1:
        return 0.80
    elif pairs >= 2:
        # two pair
        return 0.60
    elif pairs == 1:
        # one pair
        return 0.40
    else:
        # no pair
        return 0.20