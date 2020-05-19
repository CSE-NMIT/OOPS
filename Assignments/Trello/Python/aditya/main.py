#from Assignments.Trello.Python.aditya.all_clsses import Board , User , lists , cards



import json


class User :
    def __init__(self,name,userID):
        self.name =name
        self.email = name + "@gmail.com"
        self.userID = userID
    
    def toJSON(self) :
        temp = {'id' : self.userID , 'name' : self.name  , 'email':self.email}
        return json.dumps(temp)
        
class cards :
    def __init__(self,name,cardID) :
        self.name =name
        self.cardID = cardID
        self.assigned = "UNASSIGN"
        self.assignedto = ""
        self.description = ""
    def Assign_card(self,emailID) :
        self.assignedto = emailID
    
    def toJSON(self) :
        temp = {'id' : self.cardID , 'name' : self.name  , 'assignedto' : self.assignedto , 'description' : self.description}
        temp = {k: v for k, v in temp.items() if v != ""  }
        return json.dumps(temp)
    







class lists :
    def __init__(self,name,listID):
        #super().__init__(name)
        self.name =name
        self.listID = listID
        self.cards_members = {}

    def add_card(self,name,cardID) :
        self.cards_members[cardID] = cards(name,cardID)

    def delete_card(self,cardID) :
        del self.cards_members[cardID]

    def change_card_attribute(self,cardID,attribute,new_value) :
            if attribute == 'name':
                self.cards_members[cardID].name=new_value
            else :
                self.cards_members[cardID].description = new_value
    


    def toJSON(self) :
        temp2=[]
        for x in self.cards_members.values() :
            temp2.append(x.toJSON())

        temp = {'id' : self.listID , 'name' : self.name , 'cards' : temp2}
        temp = {k:v for k, v in temp.items() if v != [] and v != {}  }
        return json.dumps(temp)




class Board :
    
    def __init__(self,name,id):
        
        self.lists_members = {}
        self.name = name
        self.id = id
        self.privacy  = "PUBLIC"
        self.url = "www.trello.com/"+name +"/"+str(id)
        self.members ={}

    def add_member(self,name) :
        temp = User_dict[name].userID
        self.members[temp] = User_dict[name]

    def remove_member(self,name) :
        temp = User_dict[name].userID
        del self.members[temp]

    def create_list(self,name,listID) :
        self.lists_members[listID] = lists(name,listID)

    def delete_list(self,listID) :
        del self.lists_members[listID]

    def change_name_list(self,listID,new_name) :
        self.lists_members[listID].name  = new_name
        
    
    def toJSON(self) :
        temp2 = []
        temp3 = []
        for x in self.lists_members.values() :
            temp2.append(x.toJSON())
        for x in self.members.values() :
            temp3.append(x.toJSON())
        temp = {'id':self.id,'name':self.name,'privacy':self.privacy,'lists':temp2,'users': temp3}
        temp = {k: v for k, v in temp.items() if v != [] and v != {}  }
        return json.dumps(temp)

    
    

def dosomething_board(parse_me):
    global board_dict , id_genrator 
    
    
    if "CREATE" in parse_me:
        id_genrator +=1
        
        new_board_name = parse_me[-1]
        
        board_dict[str(id_genrator)] = Board(new_board_name,str(id_genrator)) 
        
        print("Created board:", id_genrator)
        return

    elif "DELETE" in parse_me :

        board_id = parse_me[-1]
        del board_dict[board_id]
    
    elif "name" in parse_me :
        board_id = parse_me[0]
        board_dict[board_id].name = parse_me[-1]
    
    elif "privacy" in parse_me :
        board_id = parse_me[0]
        board_dict[board_id].privacy = parse_me[-1]

    else :
        board_name = parse_me[0]
        if parse_me[1] == "ADD_MEMBER" :
            board_dict[board_name].add_member(parse_me[-1])

        elif parse_me[1] == "REMOVE_MEMBER" :
            board_dict[board_name].remove_member(parse_me[-1])


def dosomething_list(parse_me):
    global board_dict , list_id_genrator , list_dict
    
    if "CREATE" in parse_me:
        list_id_genrator +=1
        board_id = parse_me[1]
        list_name = " ".join(parse_me[1:])
        board_dict[board_id].create_list(list_name,str(list_id_genrator))
        list_dict[str(list_id_genrator)] = board_id
        print("Created List:", list_id_genrator)
        return

    elif "DELETE" in parse_me :
        board_id = list_dict[parse_me[-1]]

        board_dict[board_id].delete_list(parse_me[-1])


    else :
        board_id = list_dict[parse_me[0]]
        board_dict[board_id].change_name_list(parse_me[0],parse_me[-1])


def dosomething_card(parse_me):
    global board_dict , list_id_genrator , id_genrator , card_id_genrator,list_dict,card_dict

    if "CREATE" in parse_me :
        board_id = list_dict[parse_me[1]]
        card_id_genrator +=1
        board_dict[board_id].lists_members[parse_me[1]].add_card(parse_me[-1],str(card_id_genrator))
        card_dict[str(card_id_genrator)] = (parse_me[1],board_id)
        print("Created card:", card_id_genrator)
        

    elif "DELETE" in parse_me :
        list_id,board_id = card_dict[parse_me[-1]]
        board_dict[board_id].lists_members[list_id].delete_card(parse_me[-1])
        
    elif "ASSIGN" in parse_me :
        list_id,board_id = card_dict[parse_me[0]]
        board_dict[board_id].lists_members[list_id].cards_members[parse_me[0]].assignedto = parse_me[-1]
        
    
    elif "UNASSIGN" in parse_me :
        list_id,board_id = card_dict[parse_me[0]]
        board_dict[board_id].lists_members[list_id].cards_members[parse_me[0]].assignedto = ""
        board_dict[board_id].lists_members[list_id].cards_members[parse_me[0]].assigned = "UNASSIGN"
        

    elif "MOVE" in parse_me :
        list_id,board_id = card_dict[parse_me[0]]
        temp_card = board_dict[board_id].lists_members[list_id].cards_members[parse_me[0]]
        del board_dict[board_id].lists_members[list_id].cards_members[parse_me[0]]
        new_board_id = list_dict[parse_me[-1]]

        board_dict[new_board_id].lists_members[parse_me[-1]].add_card(temp_card.name,temp_card.cardID)
        card_dict[temp_card.cardID] = (parse_me[-1],new_board_id)

    elif 'name' in parse_me or 'description' in parse_me :
        list_id,board_id = card_dict[parse_me[0]]
        new_value = " ".join(parse_me[2:])
        board_dict[board_id].lists_members[list_id].change_card_attribute(parse_me[0],parse_me[1],new_value)


def dosomething_show(parse_me):
    global board_dict , list_dict , card_dict
    if len(parse_me) == 1 :
        if str(not board_dict) == "True" :
            print("No boards")
            return
        JsonEverything = []
        for boards in board_dict.values() :
            JsonEverything.append(boards.toJSON())
        print(JsonEverything)

    if "BOARD" in parse_me :
        if str(not board_dict) == "True" :
            print("No boards")
            return
        elif parse_me[-1] not in board_dict.keys() :
            print("Board {} does not exist".format(parse_me[-1]))
            return
        else :
            print(board_dict[parse_me[-1]].toJSON())

    elif "LIST" in parse_me :
        board_id = list_dict[parse_me[-1]]
        print(board_dict[board_id].lists_members[parse_me[-1]].toJSON())
        
    elif "CARD" in parse_me :
        list_id,board_id = card_dict[parse_me[-1]]
        board_dict[board_id].lists_members[list_id].cards_members[parse_me[-1]].toJSON()

        
card_dict ={}
list_dict ={}
board_dict ={}


User_dict = {"user1":User('user1','abc@gmail.com'),"user2":User('user2','ramesh@gmail.com'),"user3":User('user3','gopal@gmail.com')}

id_genrator =100
list_id_genrator  = 10
card_id_genrator = 1000
f=open(".\\Assignments\\Trello\\input_adi.txt","r")
for line in f:

    #line = input()
    line = line.strip().split()

    if line[0] == "BOARD" :
        dosomething_board(line[1:])
    elif line[0] == "LIST" :
        dosomething_list(line[1:])
    elif line[0] == "CARD" :
        dosomething_card(line[1:])
    elif line[0] == "SHOW" :
        dosomething_show(line)

    else :
        print('Wrong Input !! ')
