import json
import random
import string

from Board import Board
from User import User

class Trello:

    def __init__(self):

        self.boards = {}

        self.users = {
            'user1': User('user1', 'User 1'),
            'user2': User('user2', 'User 2'),
            'user3': User('user3', 'User 3'),
            'user4': User('user4', 'User 4'),
            'user5': User('user5', 'User 5')
        }

        # Define the length of the ID generated from `self.generateId(id)` method
        self.IDLENGTH = 5
    
    def handleBoard(self, inputList):
        """
        Handles BOARD Command from command Line

        Paramters:
            inputList (list(str)): List of space-separated words from command line.

        Returns:
            None
        """
        # Handle BOARD CREATE
        if inputList[1] == "CREATE":
            # The board can have names with whitespaces as well. 
            boardName = "".join(inputList[2:])

            # generate ID with prefix "" since board is the root of the path
            boardId = self.generateId("")

            # if the ID generated has already been generated. Generate a new one.
            while boardId in self.boards:
                boardId = self.generateId("")
            self.createBoard(boardId, boardName)

            return

        # Handle BOARD DELETE
        if inputList[1] == "DELETE":
            boardId = inputList[2]

            if not self.boardIdExists(boardId):
                print("Board "+boardId+" doesn't exist")
                return
            
            del self.boards[boardId]

            return

        # Handle ADD_MEMBER
        if inputList[2] == "ADD_MEMBER":

            usrId = inputList[3]

            # if the user doen't exist. Raise an alert.
            if not self.userExists(usrId):
                print('User '+usrId+' does not exist.')
                return
            
            usr = self.users[inputList[3]]
            boardId = inputList[1]
            board = self.boards[boardId]
            board.addMember(usrId,usr)

            return

        # Handle REMOVE_MEMBER
        if inputList[2] == "REMOVE_MEMBER":
            usrId = inputList[3]
            
            # if the user doesn't exist, raise an alert
            if not self.userExists(usrId):
                print('User '+usrId+' does not exist.')
                return
            
            board = self.boards[inputList[1]]
            board.removeMember(usrId)

            return

        # Handle update name
        if inputList[2] == "name":
            boardId = inputList[1]
            newName = "".join(inputList[3:])
            self.boards[boardId].updateName(newName)

            return

        # Handle update privacy
        if inputList[2] == "privacy":
            boardId = inputList[1]
            privacy = "".join(inputList[3])
            self.boards[boardId].updatePrivacy(privacy)

            return

    
    def handleList(self, inputList):
        """
        Handles LIST Command from command Line

        Paramters:
            inputList (list(str)): List of space-separated words from command line.

        Returns:
            None
        """

        # Handle LIST CREATE
        if inputList[1] == "CREATE":
            boardId = inputList[2]
            listName = inputList[3:]
            board = self.boards[boardId]
            listId = self.generateId(boardId)
            while board.listExists(listId):
                listId = self.generateId(boardId)
            board.createList(listId, listName)

            return
        
        # Handle LIST DELETE
        if inputList[1] == "DELETE":
            boardId, listId = inputList[2].split('/')
            listId = boardId+'/'+listId
            board = self.boards[board]
            board.deleteList(listId)

            return


        # Handle update name
        if "name" == inputList[2]:
            boardId, listId = inputList[1].split('/')
            listId = boardId+'/'+listId
            newName = "".join(inputList[3:])
            board = self.boards[boardId]

            cardList = board.getList(listId)

            if not cardList:
                print("List "+listId+" doesn't exist")
                return
            
            cardList.updateName(newName)

            return



    def handleCard(self, inputList):
        """
        Handles CARD Command from command Line

        Paramters:
            inputList (list(str)): List of space-separated words from command line.

        Returns:
            None
        """

        # Handle CARD CREATE
        if inputList[1] == "CREATE":
            boardId, listId = inputList[2].split('/')
            listId = boardId +'/'+ listId
            board = self.boards[boardId]
            cardName = "".join(inputList[3:])
            cardList = board.getList(listId)

            if not cardList:
                print('List '+listId+' does not exist')
                return
            
            cardId = self.generateId(listId)
            while cardId in cardList.cards:
                cardId = self.generateId(listId)
            
            cardList.createCard(cardId,cardName)

            return

        # Handle CARD DELETE
        if inputList[1] == "DELETE":
            boardId, listId, cardId = inputList[2].split('/')
            listId = boardId+'/'+listId
            cardId = listId+'/'+cardId
            board = self.boards[boardId]
            cardList = board.getList(listId)
            cardList.deleteCard(cardId)

            return

        # Handle update name
        if inputList[2] == "name":
            newName = "".join(inputList[3:])
            card = self.getCardfromCardId(inputList[1])
            if card == None:
                self.cardNotFound(inputList[1])
                return
            card.updateName(newName)

            return
            
        # Handle update description
        if inputList[2] == "description":
            newDesc = "".join(inputList[3:])
            card = self.getCardfromCardId(inputList[1])
            if card == None:
                self.cardNotFound(inputList[1])
                return
            card.updateDescription(newDesc)

            return

        # Handle ASSIGN
        if inputList[2] == "ASSIGN":
            userId = inputList[3]
            usr = self.users[userId]
            card = self.getCardfromCardId(inputList[1])
            if card == None:
                self.cardNotFound(inputList[1])
                return
            card.assign(userId,usr)

            return

        # Handle UNASSIGN
        if inputList[2] == 'UNASSIGN':
            card = self.getCardfromCardId(inputList[1])
            if card == None:
                self.cardNotFound(inputList[1])
                return
            card.unassighn()

            return
        
        # Handle MOVE

        if inputList[2] == 'MOVE':
            card = self.getCardfromCardId(inputList[1])

            if card == None:
                self.cardNotFound(inputList[1])
                return

            newListId = inputList[3]

            oldBoardId = inputList[1].split('/')[0]
            newBoardId = newListId.split('/')[0]

            if not newBoardId == oldBoardId:
                print('The new listId '+newListId+' is not in the same board as the card.')
                return

            # getting all data from oldCard 
            cardInstanceId = card.id.split('/')[2]
            cardName = card.name
            cardDescription = card.description
            cardIsAssigned = card.isAssigned
            cardAssignedTo = card.assignedTo
            cardUser = card.user

            # Delete the old card.
            oldListId = oldBoardId + '/' + inputList[1].split('/')[1]
            board = self.boards[oldBoardId]
            oldList = board.getList(oldListId)
            oldList.deleteCard(card.id)

            try:
                # Create new card in new list
                newCardId = newListId+'/'+cardInstanceId
                
                newList = board.getList(newListId)
                newList.createCard(newCardId,cardName)
                
                newCard = newList.getCard(newCardId)
                newCard.updateDescription(cardDescription)
                if cardIsAssigned:
                    newCard.assign(cardAssignedTo, cardUser)
            except:
                print('newCardId',newCardId)
                print(newList.cards)
            


    def cardNotFound(self,id):
        """
        Prints alert message if the card is not found.

        Parameters:
            id(str): Card ID
        Returns:
            None
        """
        print('Card '+id+' does not exist')


    def handleShow(self, inputList):
        """
        Handles SHOW Command from command Line

        Paramters:
            inputList (list(str)): List of space-separated words from command line.

        Returns:
            None
        """
        if len(inputList) == 1:
            if not self.boards:
                print('No boards')
                return
            print(self.jsonify())
            return
        if inputList[1] == 'BOARD':
            boardId = inputList[2]
            if not self.boardIdExists(boardId):
                print('Board '+boardId+' does not exist')
                return
            board = self.boards[boardId]
            print(board.jsonify())

            return
        
        if inputList[1] == "LIST":
            listId = inputList[2]
            boardId = listId.split('/')[0]
            board = self.boards[boardId]
            if not board.listExists(listId):
                print('List '+listId+' does not exist')
                return
            cardList = board.getList(listId)
            print(cardList.jsonify())

            return

        if inputList[1] == "CARD":
            card = self.getCardfromCardId(inputList[2])
            if card == None:
                self.cardNotFound(inputList[2])
            print(card.jsonify())

            return

    
    def createBoard(self, id, name):
        """
        Generates a Board and adds it to `self.boards`

        Parameters:
            id (str): board's ID
            name (str): board's Name
        
        Returns:
            None
        """
        board = Board(id, name)
        self.boards[id] = board
        print('Created Board: '+id)

    def getCardfromCardId(self,id):
        """
        Retrieves `Card` instance from given card ID
        
        Parameters:
            id(str): Card ID
        Returns:
            card (Card): the `Card` instance of the given ID.
        """
        boardId, listId, cardId = id.split('/')
        listId = boardId+'/'+listId
        cardId = listId+'/'+cardId
        board = self.boards[boardId]
        cardList = board.getList(listId)
        card = cardList.getCard(cardId)
        return card

    def generateId(self,prefix):
        """
        Generates random ID for boards, lists, cards and users

        Parameters:
            prefix (str): any prefix for the current object. 
                          e.g. "boardId/listId" will be a prefix for a Card
        
        Returns:
            ID (str): returns newly generated ID
        """
        generatedId = ''.join(random.choices(string.ascii_lowercase + string.digits,
                                         k = self.IDLENGTH))
        
        return prefix+'/'+generatedId if prefix != "" else generatedId

    
    def boardIdExists(self, id):
        """
        Checks if the given board id is already present.

        Parameters:
            id (str): The ID that needs to checked, if exists already or not.

        Returns:
            (bool): True if ID exists, False if it doesn't
        """
        return id in self.boards

    def userExists(self, id):
        """
        Checks if the given user id is already present.

        Parameters:
            id (str): The ID that needs to checked, if exists already or not.

        Returns:
            (bool): True if ID exists, False if it doesn't
        """
        return id in self.users


    def jsonify(self):
        """
        Retrieves JSON string of `Trello` instance.

        Parameters:
            None
        Returns:
            jsonString (str): JSON string of `Trello` instance.
        """
        jsonObject = [self.boards[board].getJsonObject() for board in self.boards]

        return json.dumps(jsonObject)



