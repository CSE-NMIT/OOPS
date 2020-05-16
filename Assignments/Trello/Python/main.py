from Trello import Trello

def main():
    t = Trello()
    while True:
        try:
            inputList = input().strip().split(' ')
            if inputList[0] == "BOARD":
                t.handleBoard(inputList)
            if inputList[0] == "LIST":
                t.handleList(inputList)
            if inputList[0] == "CARD":
                t.handleCard(inputList)
            if inputList[0] == "SHOW":
                t.handleShow(inputList)
            if inputList[0] == '':
                exit(0)
        except(EOFError):
            exit(0)

if __name__ == '__main__':
    main()