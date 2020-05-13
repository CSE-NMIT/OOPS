import json 

class Card:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.description =""
        self.assignedTo = ""
        self.isAssigned = False
        self.user = None
    
    def updateDescription(self, descr):
        self.description = descr

    def updateName(self, name):
        self.name = name

    def assign(self,id, user):
        if self.isAssigned:
            self.unassign()
        self.isAssigned = True
        self.assignedTo = id
        self.user = user
        self.user.cards.append(self.id)
    
    def unassign(self):
        if self.isAssigned:
            self.isAssigned = False
            self.assignedTo = ""
            self.user.cards.remove(self.id)
            self.user = None
        else:
            print('Card '+self.id+' is already unassigned.')

    def jsonify(self):
        """
        return JSON format of the current object for representation.
        """
        jsonObject = {
            'id': self.id,
            'isAssigned': self.isAssigned,
            'name': self.name,
            'description': self.description,
            'assignedTo': self.assignedTo,
        }

        return json.dumps(jsonObject)