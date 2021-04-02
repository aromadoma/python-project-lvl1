import prompt
from brain_games.games.brain_calc import main as brain_calc
from brain_games.games.brain_even import main as brain_even
from brain_games.games.brain_gcd import main as brain_gcd
from brain_games.games.brain_progression import main as brain_progression
from brain_games.games.brain_prime import main as brain_prime
from brain_games.games.brain_games import main as brain_games


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
    print('What is the result of the expression?')
    start_game(brain_calc)


def start_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(brain_even)


def start_gcd():
    print('Find the greatest common divisor of given numbers.')
    start_game(brain_gcd)


def start_progression():
    print('What number is missing in the progression?')
    start_game(brain_progression)


def start_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start_game(brain_prime)


def start_games():
    start_game(brain_games)
