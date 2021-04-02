import prompt
import random


def main():
    number = random.randint(0, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print('Question: {}'.format(number))
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return 0
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}"
              "'.\n".format(answer, correct_answer))
        return 1


if __name__ == '__main__':
    main()
