def main():
    print('Starting')
    # u=user('1','Gribesh','email','mobile')
    # print(u.name)
    d=driver()
    while 1:
        argument=input('Enter\n').split(' ')
        if(argument[0]=='ADD'):
            print('Adding Users')
            d.AddUsers(argument)
            print('Users Added')
        elif(argument[0]=='SHOW'):
            print('Show')
            d.Show(argument)
        elif(argument[0]=='EXPENSE'):
            #EXPENSE u1 1250 2 u2 u3 EXACT 370 880
            print('expense')
            payee=argument[1]
            total_amount=int(argument[2])
            total_users=int(argument[3])
            payers=argument[4:4+total_users]
            expense_type=argument[4+total_users]
            amounts = argument[5+total_users:]
            if(expense_type=='EQUAL'):
                print('EQUAL')
                d.EqualExpense(payee,total_amount,total_users,payers)
            elif(expense_type=='EXACT'):
                print('EXACT')
                d.ExactExpense(payee,total_amount,total_users,payers,amounts)
            elif(expense_type=='PERCENT'):
                print('PERCENT')
                d.PercentExpense(payee,total_amount,total_users,payers,amounts)
            else:
                print('Invalid Expense Type\n Expense can be EQUAL,EXACt,PERCENT')   
        else:
            print('Invalid Operation \n Usecase ADD, SHOW, EXPENSE')
    
#userId, name, email, mobile number
class user:
    def __init__(self,id,name):
        self.userId = id
        self.name = name
        #self.email = email
        #self.mobile_number = mobile_number

class driver:
    def __init__(self):
        self.user = dict()
        self.balanceSheet = dict()

    def AddUsers(self,argument):
        users_pool=argument[2:]
        for users in users_pool:
            num=str(users[-1])
            id = 'u'+num
            #email = id+'@gmail.com'
            #mobile_number=user[-1]+'number'
            self.user[id] = user(id,users)
    
    def EqualExpense(self,payee,total_amount,total_users,payers):
        amount=total_amount/total_users
        for user in payers:
            if (payee,user) in self.balanceSheet:
                self.balanceSheet[(payee,user)] += amount
            elif (user,payee) in self.balanceSheet:
                self.balanceSheet[(user,payee)] -= amount
            else:
                self.balanceSheet[(payee,user)] = amount
    
    def ExactExpense(self,payee,total_amount,total_users,payers,amounts):
        amounts = map(int,amounts)
        for user,amount in zip(payers,amounts):
            if (payee,user) in self.balanceSheet:
                self.balanceSheet[(payee,user)] += amount
            elif (user,payee) in self.balanceSheet:
                self.balanceSheet[(user,payee)] -= amount
            else:
                self.balanceSheet[(payee,user)] = amount
    
    def PercentExpense(self,payee,total_amount,total_users,payers,amounts):
        amounts = map(lambda x: (x/100)*total_amount, amounts)
        for user,amount in zip(payers,amounts):
            if (payee,user) in self.balanceSheet:
                self.balanceSheet[(payee,user)] += amount
            elif (user,payee) in self.balanceSheet:
                self.balanceSheet[(user,payee)] -= amount
            else:
                self.balanceSheet[(payee,user)] = amount
    
    def Show(self, argument):

        def printLine(pair):
            if self.balanceSheet[pair] < 0:
                print(self.user[pair[0]].name+" owes "+ self.user[pair[1]].name+": "+ str(-(self.balanceSheet[pair])))
            if self.balanceSheet[pair] > 0:
                print(self.user[pair[1]].name+" owes "+ self.user[pair[0]].name+ ": "+ str(self.balanceSheet[pair]))

        if len(self.balanceSheet.keys()) == 0:
            print("No balances")
            return
        if len(argument) == 1:
            for pair in self.balanceSheet:
                printLine(pair)
        else :
            count = 0
            for pair in self.balanceSheet:
                if argument[1] in pair:
                    count += 1
                    printLine(pair)
            if count ==0: print("No balances")

if __name__ == '__main__':
    main()
