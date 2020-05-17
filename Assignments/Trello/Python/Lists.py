from Card import Card

class Lists:

    def __init__(self,id):
        self.id=id
        self.name
        self.description
        self.cards={}



    def createCard(self,cardName):
        cardId = None   #generate cardId
        c = Card(cardId)
        c.name = cardName
        cards[cardId] = c
        return cardId


    def deleteCard(self,cardId):
        del cards[cardId]



    def setName(self,name):
        self.name = name


    def setDescription(self,desc):
        self.description = desc


    def issCard(self,cardId) -> bool:       #return true for a card
        if cardId in cards: return True
        return False




    def displayList(self):
        print("List ID:",self.id,"/nNAME",self.name,"/nCARDS:")
        for i in cards:
            print("/n",i,"/n")
            i.displayCards()