import json

from Card import Card

class CardList:
    def __init__(self,id,name):
        """
        CardList constructor - creates a CardList instance

        Parameters:
            id (str): ID of the list
            name(str): Name of the list

        Returns:
            None
        """
        self.id = id
        self.name = name
        self.cards = {}

    def updateName(self,name):
        """
        Updates the name of the cardList

        Parameters:
            name(str): New name of the list

        Returns:
            None
        """
        self.name = name

    def createCard(self,id,name):
        card = Card(id,name)
        self.cards[id] = card
        print('Created Card:'+id)

    def deleteCard(self,id):
        if not self.cardExists(id):
            print("Card "+id+" doesn't exist")
            return
        del self.cards[id]


    def getCard(self,id):
        if not self.cardExists(id):
            return None
        return self.cards[id]

    

    def cardExists(self, id):
        """
        Checks if the given card id is already present.

        Parameters:
            id (str): The ID that needs to checked, if exists already or not.

        Returns:
            (bool): True if ID exists, False if it doesn't
        """
        return id in self.cards


    def jsonify(self):
        """
        return JSON format of the current object for representation.
        """
        jsonObject = self.getJsonObject()
        return json.dumps(jsonObject)

    def getJsonObject(self):
        jsonObject = {
            'id': self.id,
            'name': self.name,
            'cards': [self.cards[card].getJsonObject() for card in self.cards] if self.cards else [""]
        }
        return jsonObject