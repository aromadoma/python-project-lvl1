import prompt
from brain_games.games.brain_calc import main as brain_calc
from brain_games.games.brain_even import main as brain_even


def start_game(func):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    i = 0
    while i < 3:
        if func() == 0:
            i += 1
        else:
            print("Let's try again, {}!".format(name))
            return 0
    print('Congratulations, {}!'.format(name))


def start_calc():
    start_game(brain_calc)


def start_even():
    start_game(brain_even)