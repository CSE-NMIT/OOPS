import json 

class Card:
    def __init__(self, id, name):
        """
        Creates a `Card` instance
        
        Parameters:
            id(str): Card ID
            name(str): Card name
        """
        self.id = id
        self.name = name
        self.description =""
        self.assignedTo = ""
        self.isAssigned = False
        self.user = None
    
    def updateDescription(self, descr):
        """
        Updates the `self.description` attribute.
        
        Parameters:
            descr(str): New description of the card.
        Returns:
            None

        """
        self.description = descr

    def updateName(self, name):
        """
        Updates the `self.name` attribute.
        
        Parameters:
            name(str): New name of the card.
        Returns:
            None
            
        """
        self.name = name

    def assign(self,id, user):
        """
        Assigns a user to the card. lso adds the crdId to the `User.cards` attribute.

        Parameters:
            id(str): User ID
            user(User): `User` instance of the user assigned to the card.

        Returns:
            None
        
        """
        if self.isAssigned:
            self.unassign()
        self.isAssigned = True
        self.assignedTo = id
        self.user = user
        self.user.cards.append(self.id)
    
    def unassign(self):
        """
        If any user is assigned to the card, unassigns the user. 
        Also removes the cardId from the `User.cards` attribute.

        Parameters:
            None
        Returns:
            None
        
        """
        if self.isAssigned:
            self.isAssigned = False
            self.assignedTo = ""
            self.user.cards.remove(self.id)
            self.user = None
        else:
            print('Card '+self.id+' is already unassigned.')

    def getJsonObject(self):
        """
        Retrieves a Dictionary object of `Card` instance which can be converted to JSON. 
        
        Parameters:
            None
        Returns:
            jsonObject (dict): `dict` object of the `Card` instance.
        """
        jsonObject = {
            'id': self.id,
            'isAssigned': self.isAssigned,
            'name': self.name,
            'description': self.description,
            'assignedTo': self.assignedTo,
        }
        return jsonObject

    def jsonify(self):
        """
        Retrieves JSON string of the `Card` instance.

        Parameters:
            None
        Returns:
            jsonString (str): JSON string of `Card` instance.
        """
        jsonObject = self.getJsonObject()

        return json.dumps(jsonObject)