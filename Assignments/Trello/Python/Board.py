import json

from CardList import CardList

class Board:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.privacy = "PUBLIC"
        self.url = ""
        self.members = {}
        self.lists = {}

    def addMember(self, id, user):
        if self.memberIdExists(id):
            print('Member ' + id + ' already Exists')
            return
        self.members[id] = user
        # Add board to user's instance
        user.boards.append(self.id)
    
    def removeMember(self,id):
        """
        Deletes a member from the board. Unassigns all the cards the user was a part of.

        Parameters:
            id(str): user ID of user to be removed from the board.
        """
        
        if not self.memberIdExists(id):
            print('Member' + id + ' doesn\'t exist')
            return

        usr = self.members[id]

        # Remove board from user's instance
        usr.boards.remove(self.id)

        # unassign all the cards the user was a part of from the current Board.
        for card in usr.cards:
            boardId, listId, cardId = card.split('/')
            listId = boardId+'/'+listId
            cardId = listId+'/'+cardId
            if boardId == self.id:
                cardList = self.lists[listId]
                cardInst = cardList[cardId]
                cardInst.unassign()

        del self.members[id]

    def updateName(self,name):
        """
        Updates the board name

        Parameters:
            name (str): New name of the board

        Returns:
            None
        """
        self.name = name

    def updatePrivacy(self,privacy):
        """
        Updates the board privacy

        Parameters:
            privacy (str): New privacy of the board

        Returns:
            None
        """
        self.privacy = privacy

        
    def createList(self, id, name):
        cardList = CardList(id,name)
        self.lists[id] = cardList
        print('Created List :' + id)
    
    def deleteList(self,id):
        if not self.listExists(id):
            print("List "+id+" doesn't exist")
            return
        del self.lists[id]

    def getList(self,id):
        if not self.listExists(id):
            return None
        return self.lists[id]
    

    def jsonify(self):
        jsonObject = {
            'id':self.id,
            'name':self.name,
            'privacy':self.privacy,
            'members': [self.members[user].jsonify() for user in self.members],
            'lists': [self.lists[lst].jsonify() for lst in self.lists]
        }

        return json.dumps(jsonObject)

    def memberIdExists(self, id):
        """
        Checks if the given member id is already present.

        Parameters:
            id (str): The ID that needs to checked, if exists already or not.

        Returns:
            (bool): True if ID exists, False if it doesn't
        """
        return id in self.members

    def listExists(self,id):
        """
        Checks if the given List id is already present.

        Parameters:
            id (str): The ID that needs to checked, if exists already or not.

        Returns:
            (bool): True if ID exists, False if it doesn't
        """
        return id in self.lists