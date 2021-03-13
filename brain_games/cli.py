"""CLI module."""
import prompt


def welcome_user():
    """Input and greeting name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
