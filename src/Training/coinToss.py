# coinToss.py - simple coin toss game

import random  # generate random 0 ,1
import logging  # for debugging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)
logging.debug('Start of code')


def get_guess():
    logging.debug('Start of get_guess()')
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
        logging.debug('User input guess = (%s)' % (guess))
        if guess == 'heads':
            int_guess = 1
        elif guess == 'tails':
            int_guess = 0
    logging.debug('int_guess = (%d)' % (int_guess))
    logging.debug('End of get_guest()')
    return int_guess


int_guess = get_guess()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
logging.debug('toss = (%d)' % (toss))
assert type(toss) == type(int_guess), 'variable have to be same type'
if toss == int_guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    int_guess = get_guess()
    if toss == int_guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
