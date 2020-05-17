
class cards :
    def __init__(self,name) :
        self.name =name


class lists :
    def __init__(self,name):
        self.name =name
    




class Board :
    Board_count =100
    def __init__(self,name):
        self.name = name
        self.id = Board_count
        Board_count +=1

        self.url = "www.trello.com/"+name +"/"+str(id)

