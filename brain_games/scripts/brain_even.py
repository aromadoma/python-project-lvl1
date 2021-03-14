import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = random.randint(0, 100)
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                  "Let's try again, {}!".format(answer, correct_answer, name))
            exit()
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
