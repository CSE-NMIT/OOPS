import json
class User:
    def __init__(self, userId, name):
        """
        Creates a `User` instance
        
        Parameters:
            userId(str): User ID
            name(str): User name
        """
        self.id = userId
        self.name = name
        self.__email = ""
        self.boards = []
        self.cards = []

    def getJsonObject(self):
        """
        Retrieves a Dictionary object of `User` instance which can be converted to JSON. 
        
        Parameters:
            None
        Returns:
            jsonObject (dict): `dict` object of the `User` instance.
        """
        jsonObject = {
            'id':self.id,
            'name':self.name,
            'email':self.__email
        }
        return jsonObject

    def jsonify(self):
        """
        Retrieves JSON string of the `User` instance.

        Parameters:
            None
        Returns:
            jsonString (str): JSON string of `User` instance.
        """
        jsonObject = self.getJsonObject()

        return json.dumps(jsonObject)