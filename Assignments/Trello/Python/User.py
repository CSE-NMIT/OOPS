import json
class User:
    def __init__(self, userId, name):
        self.id = userId
        self.name = name
        self.__email = ""
        self.boards = []
        self.cards = []

    def jsonify(self):
        """
        return JSON format of the current object for representation.
        """
        jsonObject = {
            'id':self.id,
            'name':self.name,
            'email':self.__email
        }

        return json.dumps(jsonObject)