#!/usr/bin/env python3
import asyncio
import argparse

from tg.bot import Bot
from tg.types import *
import time
from evalDeck import evalDeck
from preflop import preflop_action2
from betStrength import betStrenth

import sys
import os
sys.path.append(os.path.join(os.curdir, "tg"));


parser = argparse.ArgumentParser(
    prog='Template bot',
    description='A Turing Games poker bot that always checks or calls, no matter what the target bet is (it never folds and it never raises)')

parser.add_argument('--port', type=int, default=80,
                    help='The port to connect to the server on')
parser.add_argument('--host', type=str, default='ws.turingpoker.com',
                    help='The host to connect to the server on')
parser.add_argument('--room', type=str, default='room4',
                    help='The room to connect to')
parser.add_argument('--username', type=str, default='magnus poker',
                    help='The username for this bot (make sure it\'s unique)')

args = parser.parse_args()

cnt = 0
# Always call
class TemplateBot(Bot):
    def act(self, state, hand):
        print('asked to act')
        print('acting', state, hand, self.my_id)

        strength: int = evalDeck(state, hand)
        print('strength:', strength)

        bet_strength: int = betStrenth(state)
        print('bet strength:', bet_strength)

        if (state.round == 'pre-flop'): 
            preflop_val = preflop_action2(state=state, hand=hand)
            if (type(preflop_val) == tuple):
                return {'type': 'raise', 'amount': preflop_val[1]}
            else:
                return {'type': preflop_val}
        else:
            if strength <= 2:
                return {'type' :'call'}
            elif (hand[0].rank == hand[1].rank and state.target_bet <= 250):
                return {'type' :'call'}
            elif (hand[0].rank == Rank.ACE and hand[0].rank == Rank.ACE):
                return {'type' : 'raise', 'amount' : 350}
            elif ((hand[0].rank == Rank.KING and hand[0].rank == Rank.KING) or
            (hand[0].rank == Rank.QUEEN and hand[0].rank == Rank.QUEEN)):
                return {'type' : 'raise', 'amount' : 250}
            elif (hand[0].rank == Rank.ACE or hand[0].rank == Rank.ACE and state.target_bet <= 100):
                return {'type' : 'call'}
            elif ((hand[0].rank == Rank.ACE and hand[1].rank == Rank.KING) or (hand[0].rank == Rank.KING and hand[1].rank == Rank.ACE)):
                return {'type' : 'raise' , 'amount' : 100}
            elif ((hand[0].rank == Rank.ACE and hand[1].rank == Rank.QUEEN) or (hand[0].rank == Rank.QUEEN and hand[1].rank == Rank.ACE)):
                return {'type' : 'raise' , 'amount' : 70}
            elif ((hand[0].rank == Rank.KING and hand[1].rank == Rank.QUEEN) or (hand[0].rank == Rank.QUEEN and hand[1].rank == Rank.KING)):
                return {'type' : 'raise' , 'amount' : 70}
            return {'type' : 'fold'}
            
        

    def opponent_action(self, action, player):
        #print('opponent action?', action, player)
        pass

    def game_over(self, payouts):
        global cnt
        #print('game over', payouts)
        cnt += 1
        print(cnt)

    def start_game(self, my_id):
        self.my_id = my_id
        pass

if __name__ == "__main__":
    bot = TemplateBot(args.host, args.port, args.room, args.username)
    asyncio.run(bot.start())
