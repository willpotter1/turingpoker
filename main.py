#!/usr/bin/env python3
import asyncio
import argparse
from betStrength import betStrength
from tg.bot import Bot
from tg.types import *
import time
from evalDeck import evalDeck
from preflop import preflop_action2
from betStrength import betStrength
from time import sleep

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
        sleep(0.1)
        print('asked to act')

        strength = evalDeck(state, hand)
        opponent_strength = betStrength(state)
        print('our hand ' + str(hand[0].rank) + str(hand[1].rank))
        print('opponent strength' + str(opponent_strength))
        print('our strength ' +  str(strength))


        index = 0 
        op_id = 0
        for playerId, player in enumerate(state.players):
            bot_name: str = open('BOT_NAME.txt', 'r').read()
            if player.id.lower() == bot_name.lower():
                index = playerId
            else: 
                op_index =  playerId
        print('our stack' + str(state.players[index].stack))
        print('round : ' + state.round)
        if (state.players[op_id].stack == 0 and state.players[op_id].current_bet <= 60 ): 
            return {'type' : 'call'}
        if (state.round == 'pre-flop'): 
            preflop_val = preflop_action2(state=state, hand=hand)
            if (type(preflop_val) == tuple):
                return {'type': 'raise', 'amount': preflop_val[1]}
            else:
                return {'type': preflop_val}
        else:
            if (state.players[index].stack <= 50):
                return {'type' : 'call'}
            if (state.round == 'flop'):
                if (strength == 1):
                    if opponent_strength == 1:
                       return {'type' : 'call'}
                    elif opponent_strength >= 2:
                        return {'type' : 'fold'}
                if (strength == 2):
                    if opponent_strength == 2:
                       return {'type' : 'call'}
                    elif opponent_strength == 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                    elif opponent_strength >= 3:
                        return {'type' : 'fold'}
                if (strength == 3):
                    if opponent_strength == 2 or opponent_strength == 3:
                       return {'type' : 'call'}
                    elif opponent_strength == 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                    elif opponent_strength >= 4:
                        return {'type' : 'fold'}
                if (strength == 4):
                    if 3 <= opponent_strength <= 4:
                       return {'type' : 'call'}
                    elif opponent_strength >= 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                if (strength == 5):
                    if  opponent_strength == 4:
                       return {'type' : 'call'}
                    else:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                if (strength >= 6):
                    return {'type' : 'raise', 'amount' : state.target_bet * 6}
            elif (state.round == 'turn'):
                if (strength == 1):
                    if opponent_strength == 1:
                       return {'type' : 'call'}
                    elif opponent_strength >= 2:
                        return {'type' : 'fold'}
                if (strength == 2):
                    if opponent_strength == 2:
                       return {'type' : 'call'}
                    elif opponent_strength == 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                    elif opponent_strength >= 3:
                        return {'type' : 'fold'}
                if (strength == 3):
                    if opponent_strength == 2 or opponent_strength == 3:
                       return {'type' : 'call'}
                    elif opponent_strength == 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                    elif opponent_strength >= 4:
                        return {'type' : 'fold'}
                if (strength == 4):
                    if 3 <= opponent_strength <= 4:
                       return {'type' : 'call'}
                    elif opponent_strength >= 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                if (strength == 5):
                    if  opponent_strength == 4:
                       return {'type' : 'call'}
                    else:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                if (strength >= 6):
                    return {'type' : 'raise', 'amount' : state.target_bet * 5}
            elif (state.round == 'river'):
                if (strength == 1):
                    if opponent_strength == 1:
                       return {'type' : 'call'}
                    elif opponent_strength >= 2:
                        return {'type' : 'fold'}
                if (strength == 2):
                    if opponent_strength == 2:
                       return {'type' : 'call'}
                    elif opponent_strength == 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                    elif opponent_strength >= 3:
                        return {'type' : 'fold'}
                if (strength == 3):
                    if opponent_strength == 2 or opponent_strength == 3:
                       return {'type' : 'call'}
                    elif opponent_strength == 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                    elif opponent_strength >= 4:
                        return {'type' : 'fold'}
                if (strength == 4):
                    if 3 <= opponent_strength <= 4:
                       return {'type' : 'call'}
                    elif opponent_strength >= 1:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                if (strength == 5):
                    if  opponent_strength == 4:
                       return {'type' : 'call'}
                    else:
                       return { 'type' : 'raise', 'amount' : state.target_bet * 3}
                if (strength >= 6):
                    return {'type' : 'raise', 'amount' : state.target_bet * 6}
        

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
