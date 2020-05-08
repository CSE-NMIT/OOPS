from typing import List
from User import User
from Expense import Expense

class Group: 
    def __init__(self, inputList: List[str]): 
        self.users = {}
        self.balances = {}
        self.expenses = []

        usersString = inputList[2:]
        count = 1
        for usr in usersString:
            id = 'u'+str(count)
            self.users[id] = User(id,usr)
            count += 1

    def addExpense(self, inputList: List[str]):

        expenseBy = inputList[1]
        amountToSplit = int(inputList[2])
        splitAmong = []
        splitArgs = []
        expenseType = ""

        amount = amountToSplit
        num = int(inputList[3])
        owedBy = inputList[4:4+num]

        for user in owedBy:
            splitAmong.append(self.users[user])

        splitAmong.append(self.users[expenseBy])
        splitAmong = set(splitAmong)

        # Update the transaction 
        def updateAmount(owedTo, usr, amt) :
            if owedTo == usr : return
            if (owedTo,usr) in self.balances:
                self.balances[(owedTo,usr)] += amt
            elif (usr,owedTo) in self.balances:
                self.balances[(usr,owedTo)] -= amt
            else:
                self.balances[(owedTo,usr)] = amt


        if "EQUAL" in inputList:
            expenseType = "EQUAL"
            amount = roundNumber(amount / num)
            for usr in owedBy:
                updateAmount(expenseBy,usr,amount)


        if "EXACT" in inputList:
            expenseType = "EXACT"
            amountList = list(map(int,inputList[5+num:]))
            splitArgs = amountList
            for usr,amt in zip(owedBy,amountList):
                updateAmount(expenseBy, usr, amt)

        if "PERCENT" in inputList:
            expenseType = "PERCENT"
            splitArgs = list(map(int,inputList[5+num:]))
            amountList = map(lambda x: roundNumber((x/100)*amount), splitArgs)
            for usr,amt in zip(owedBy, amountList):
                updateAmount(expenseBy, usr, amt)
        
        # Create Expense instance
        expense = Expense(self.users[expenseBy], amountToSplit, splitAmong, splitArgs, expenseType)


        # Add expense to each user's passbook
        for user in splitAmong:
            self.addExpenseToUsers(user, expense)
            
    def addExpenseToUsers(self, user, expense):
        user.addExpense(expense)


    def show(self, inputList: List[str]):
    
        def printLine(pair):
            if self.balances[pair] < 0:
                print(self.users[pair[0]].name+" owes "+ self.users[pair[1]].name+": "+ str(-(self.balances[pair])))
            if self.balances[pair] > 0:
                print(self.users[pair[1]].name+" owes "+ self.users[pair[0]].name+ ": "+ str(self.balances[pair]))

        if not self.balances :
            print("No balances")
            return
        if len(inputList) == 1:
            for pair in self.balances:
                printLine(pair)
        else :
            count = 0
            for pair in self.balances:
                if inputList[1] in pair:
                    count += 1
                    printLine(pair)
            if count ==0: print("No balances")



def roundNumber(number):
    if int(number) == number:
        return int(number)
    else:
        return round(number, 2)

