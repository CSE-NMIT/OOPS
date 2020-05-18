class User :
    
    
    def __init__(self,name,userID) :
       
        self.userID = userID
        self.name=name
        #self.email=email
        #self.mobile_number=mobile_number
        
        

def Add_User(line) :
    global expenses
    user_count=1
    no_of_users = len(line)
    for each_user in line:
        user_id = 'u{}'.format(user_count)
        user_dict[user_id]=User(each_user,user_id)
        user_count+=1

    for u_users in user_dict.keys() :
        for v_users in user_dict.keys() :
            expenses[u_users + v_users] = 0
    
    


def Add_expense(line) :
    global expenses
    who_paid = line.pop(0)
    how_much_paid=int(line.pop(0))
    number_of_participant= int(line.pop(0))
    participant_list=[]
    for _ in range(number_of_participant):
        participant_list.append(line.pop(0))
    type_of_expense =line.copy()
    if type_of_expense[0] == "EQUAL" :
        
        #print(expenses)

        add_amount = how_much_paid/number_of_participant
        for participants in participant_list :
            if participants != who_paid :
                expenses[participants + who_paid]+=add_amount

    elif type_of_expense[0] == "EXACT" :
        count=1
        
        check_total = map(int,type_of_expense[1:])
        if sum(check_total) != how_much_paid :
            print("Invalid Expence")
            return
        
        
        for participants in participant_list :
            if participants != who_paid :
                expenses[participants + who_paid] += int(type_of_expense[count])
            count+=1    
            
    elif type_of_expense[0] == "PERCENT" :
        count=1
        for participants in participant_list :
            if participants != who_paid :
                expenses[participants + who_paid] +=how_much_paid*(int(type_of_expense[count])/100.0)
            count+=1
    
       

def Show_Exp(line) :
    global expenses
    flag =0
    for uid in expenses.keys():
        if expenses[uid] == 0 :
            continue
        uid1 = uid[:2]
        uid2 = uid[2:]
        
        if expenses[uid1 + uid2] >= expenses[uid2 + uid1] :
            expenses[uid1 + uid2] -= expenses[uid2 + uid1]
            expenses[uid2 + uid1] =0

    

    if len(line) == 1 :
        for uid in expenses.keys():
            if expenses[uid] == 0 :
                continue
            uid1 = uid[:2]
            uid2 = uid[2:]
            flag =1
            print(user_dict[uid1].name,"owes",str(user_dict[uid2].name) + ":",expenses[uid])
            
    else :
        temp_user_id=line[1]
        for uid in expenses.keys():
            if temp_user_id in uid :    
                if expenses[uid] == 0 :
                    continue
                uid1 = uid[:2]
                uid2 = uid[2:]
                flag =1
                print(user_dict[uid1].name,"owes",str(user_dict[uid2].name) + ":",expenses[uid])
        
    if flag == 0:
        print("No balances")

def main():
    f=open(".\\Assignments\\Splitwise\\input.txt","r")
    for line in f:
        
        #line = input().strip().split()
        line =line.strip().split()
        
        if line[0]=="ADD" :
            Add_User(line[2:])
            num_of_users=line[1]
        elif line[0]== "EXPENSE" :
            Add_expense(line[1:])
        elif line[0]=="SHOW" :
            Show_Exp(line)
    

user_dict={}
expenses={}

if __name__ == '__main__':
    main()    