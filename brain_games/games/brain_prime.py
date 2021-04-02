import prompt
import random


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number


def main():
    number = random.randint(0, 100)
    print('Question: {}'.format(number))
    answer = prompt.string('Your answer: ')
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    if answer == correct_answer:
        print('Correct!')
        return 0
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
              "".format(answer, correct_answer))
        return 1


if __name__ == '__main__':
    main()
