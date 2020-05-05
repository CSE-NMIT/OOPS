from user import user
from ProcessInput import ProcessInput
from typing import List
def main():
    p = ProcessInput()
    while True:
        #process each line in input
        try:
            inputList = input().strip().split(' ')
            if inputList[0] == 'ADD':
                p.processAdd(inputList)
            if inputList[0] == 'EXPENSE':
                p.processExpense(inputList)
            if inputList[0] == 'SHOW':
                p.processShow(inputList)
            if inputList[0] == '':
                exit(0)
        except (EOFError):
            exit(0)


if __name__ == '__main__':
    main()