#Status:Not Completed
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
            #d.Show(argument)
        elif(argument[0]=='EXPENSE'):
            #EXPENSE u1 1250 2 u2 u3 EXACT 370 880
            print('expense')
            payee=argument[1]
            total_amount=argument[2]
            total_users=int(argument[3])
            payers=argument[4:4+total_users]
            expense_type=argument[4+total_users]
            amounts = argument[5+total_users:]
            if(expense_type=='EQUAL'):
                print('EQUAL')
                #d.EqualExpense(payee,total_amount,total_users,payers)
            elif(expense_type=='EXACT'):
                print('EXACT')
                #d.ExactExpense(payee,total_amount,total_users,payers,amounts)
            elif(expense_type=='PERCENT'):
                print('PERCENT')
                #d.PercentExpense(payee,total_amount,total_users,payers,amounts)
            else:
                print('Invalid Expense Type\n Expense can be EQUAL,EXACt,PERCENT')   
        else:
            print('Invalid Operation \n Usecase ADD, SHOW, EXPENSE')
    
#userId, name, email, mobile number
class user:
    def __init__(self,id,name,email,mobile_number):
        self.userId = id
        self.name = name
        self.email = email
        self.mobile_number = mobile_number

class driver:
    def __init__(self):
        self.user = dict()

    def AddUsers(self,argument):
        users_pool=argument[2:]
        for user in users_pool:
            id = 'u'+user[-1]
            email = id+'@gmail.com'
            mobile_number=user[-1]+'number'
            self.user[id] = user(id,user,email,mobile_number)
    
    #def EqualExpense(self,payee,total_amount,total_users,payers):

    
    #def ExactExpense(self,payee,total_amount,total_users,payers,amounts):

    
    #def PercentExpense(self,payee,total_amount,total_users,payers,amounts):

    
    #def Show(self, argument):

if __name__ == '__main__':
    main()