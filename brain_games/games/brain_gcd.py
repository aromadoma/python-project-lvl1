import prompt
import random


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def main():
    print('Find the greatest common divisor of given numbers.')
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    print(f'Question: {a} {b}')
    answer = prompt.integer('Your answer: ')
    gcd = find_gcd(a, b)
    if answer == gcd:
        print('Correct!')
        return 0
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
              "".format(answer, gcd))
        return 1


if __name__ == '__main__':
    main()
