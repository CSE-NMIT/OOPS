from typing import List

import User
from Group import Group

def main():
    g = None
    while True:
        #process each line in input
        try:
            inputList = input().strip().split(' ')
            if inputList[0] == 'ADD':
                g = Group(inputList)
            if inputList[0] == 'EXPENSE':
                g.addExpense(inputList)
            if inputList[0] == 'SHOW':
                g.show(inputList)
            if inputList[0] == '':
                exit(0)
        except (EOFError):
            exit(0)


if __name__ == '__main__':
    main()