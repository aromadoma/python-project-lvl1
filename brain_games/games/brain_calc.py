import prompt
import random


def main():
    print('What is the result of the expression?')
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    action = random.choice(['-', '+', '*'])
    if action == '-':
        correct_answer = a - b
    elif action == '+':
        correct_answer = a + b
    else:
        correct_answer = a * b
    print(f'Question: {a} {action} {b}')
    answer = prompt.integer('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return 0
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
              "".format(answer, correct_answer))
        return 1


if __name__ == '__main__':
    main()
