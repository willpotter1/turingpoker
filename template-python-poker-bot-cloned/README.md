# Template Python Poker Bot
This repo is a template for a Turing Poker bot written in Python. Two sample bots are included.
The first, `main.py`, is a simple bot that always checks or calls. 
The second, `kellycriterion.py`, simulates potential game outcomes to estimate the probability
of winning the current hand, and uses the [Kelly Criterion](https://en.wikipedia.org/wiki/Kelly_criterion) to determine the optimal bet size.
# How to connect your bot
1. Run `git clone https://github.com/Turing-Games/template-python-poker-bot.git`
2. Run `git checkout mcgill-tournament`
3. Run `pip install -r requirements.txt`
4. Run `python3 main.py --host ws.turingpoker.com --port 80 --room 123456 --username your_username`