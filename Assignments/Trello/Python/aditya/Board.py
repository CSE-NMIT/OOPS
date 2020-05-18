
class User :
    user_id_genrator = 1
    def __init__(self,name):
        self.name =name
        self.email = name + "@gmail.com"
        self.userID = User.user_id_genrator
        User.user_id_genrator +=1

class cards :
    def __init__(self,name) :
        self.name =name


class lists(cards) :
    def __init__(self,name,name_card):
        super().__init__(name)
        self.name =name
    




class Board(lists) :
    
    def __init__(self,name,id):
        self.name = name
        self.id = id

        self.url = "www.trello.com/"+name +"/"+str(id)
        self.members ={}

    def add_member(self,name) :
        self.members[name] = User_dict[name]
    def remove_member(self,name) :
        del self.members[name]
def dosomething_board(parse_me):
    global board_dict , id_genrator
    
    
    if "CREATE" in parse_me:
        id_genrator +=1
        board_dict[str(id_genrator)] = Board(parse_me[-1],str(id_genrator)) 
        print("Created board:", id_genrator)
        return

    elif "DELETE" in parse_me :
        del board_dict[parse_me[-1]]
    
    elif "name" in parse_me :
        board_dict[parse_me[0]].name = parse_me[-1]
    elif "privacy" in parse_me :
        board_dict[parse_me[0]].privacy = parse_me[-1]

    else :
        if parse_me[1] == "ADD_MEMBER" :
            board_dict[parse_me[0]].add_member(parse_me[-1])

        elif parse_me[1] == "REMOVE_MEMBER" :
            board_dict[parse_me[0]].remove_member(parse_me[-1])

def dosomething_list(parse_me):
    pass
def dosomething_card(parse_me):
    pass
def dosomething_show(parse_me):
    pass



board_dict ={}
User_dict = {"user1":User('user1'),"user2":User('user2'),"user3":User('user3')}
id_genrator =100
f=open(".\\Assignments\\Trello\\input.txt","r")
for line in f:
    line = line.strip().split()

    if line[0] == "BOARD" :
        dosomething_board(line[1:])
    elif line[0] == "LIST" :
        dosomething_list(line[1:])
    elif line[0] == "CARD" :
        dosomething_card(line[1:])
    elif line[0] == "SHOW" :
        dosomething_show(line[1:])
    
    else :
        print('Wrong Input !! ')
