import prompt
import random


def main():
    first_element = random.randint(0, 100)
    progression_length = random.randint(5, 10)
    # print(f'LENGTH = {progression_length}')
    hidden_elem_index = random.randint(0, progression_length - 1)
    # print(f'HIDDEN INDEX = {hidden_elem_index}')
    increment = random.randint(1, 10)
    # print(f'INCREMENT = {increment}')
    progression = [first_element]
    for i in range(1, progression_length):
        progression.append(first_element + increment * i)
    print('What number is missing in the progression?')
    print('Question: ', end='')
    # print(f'PROGRESSION = {progression}')
    for element in progression:
        # print(f'--element {element}')
        if progression.index(element) != hidden_elem_index:
            # print(f'--element index {progression.index(element)} != {hidden_elem_index}')
            print(element, end=' ')
        else:
            # print(f'--element index {progression.index(element)} == {hidden_elem_index}')
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
