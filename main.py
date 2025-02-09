#!/usr/bin/env python3
import asyncio
import argparse

from tg.bot import Bot
from tg.types import *
import time
from evalDeck import evalDeck

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

        if (state.round == 'pre-flop'): 
            if (state.target_bet <= 50):
                return {'type' :'call'}
            elif (hand[0].rank == hand[1].rank and state.target_bet <= 250):
                return {'type' :'call'}
            elif (hand[0].rank == Rank.ACE and hand[0].rank == Rank.ACE):
                return {'type' : 'raise', 'amount' : 300}
            return {'type' : 'fold'} # default
        else:
            if strength <= 2:
                return {'type' : 'fold'}
            elif 3 <= strength <= 5:
                return {'type' : 'call'}
            else:
                amount: float = 100 * abs(strength - 6)
                return  {'type' :'raise', 'amount' : amount}
            
        

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
