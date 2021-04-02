import prompt
import random


def main():
    first_element = random.randint(0, 100)
    hidden_elem_index = random.randint(0, 9)
    print(hidden_elem_index)
    increment = random.randint(0, 10)
    progression = [first_element]
    for i in range(1, 10):
        progression.append(first_element + increment * i)
    print(progression)
    print('What number is missing in the progression?')
    print('Question: ', end='')
    for element in progression:
        if progression.index(element) != hidden_elem_index:
            print(element, end=' ')
        else:
            print('..', end=' ')
    answer = prompt.integer('\nYour answer: ')
    if answer == progression[hidden_elem_index]:
        print('Correct!')
        return 0
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
              "".format(answer, progression[hidden_elem_index]))
        return 1


if __name__ == '__main__':
    main()
