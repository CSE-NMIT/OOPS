import User

class Card:

    def __init__(self,id):
        self.name=name
        self.id=id
        self.user=None

    def isAssUser(self) -> bool:
        if self.user is None:
            return False  
        return True

    def assUser(self,userId):
        self.user = User(userId)

    def unAssUser(self):
        self.user = None


    def displayCards(self):
        print("Card ID:",self.id,"/nNAME",self.name,"/n")
        if isAssUser:
            user.displayUser()


            