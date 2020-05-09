from typing import List
from User import User
from Expense import Expense

class Group: 
    def __init__(self, inputList: List[str]): 
        """
        Constructor : defines the Group class and adds all the users in the group.

        Parameters:
            inputList (list(str)) : list of all words from command line

        Returns : 
            None
        """
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
        """
        Adds the expense from command line. Updates each user's balances.
        Adds the expense to each participating user's passbook.

        Parameters:
            inputList (list(str)) : list of all words from command line
        
        Returns:
            None

        """

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

        expenseType = inputList[4+num]

        # Update the transaction 
        def updateAmount(owedTo, usr, amt) :
            """
            Updates the balance of each user in `self.balances` attribute

            Parameters:
                owedTo (str) : id of the user who bore the expense.
                usr (str) : id of the user owing money to expense bearer.
                amt (int) : the amount `usr` owes to expense bearer

            Returns: 
                None
            """
            if owedTo == usr : return
            if (owedTo,usr) in self.balances:
                self.balances[(owedTo,usr)] += amt
            elif (usr,owedTo) in self.balances:
                self.balances[(usr,owedTo)] -= amt
            else:
                self.balances[(owedTo,usr)] = amt

        def handleType(expenseType, splitArgs, owedBy) :
            """
            Handles `EXACT` and `PERCENT` expenseTypes because of the `splitArgs`..

            Parameters:
                expenseType (str) : the type of expense.
                splitArgs (list(int)) : Arguments to split the amount among users.
                owedBy (list(str)) : list of user IDs of the users who owe money to expense bearer.
            
            Returns:
                None
            """
            splitArgs = list(map(int,inputList[5+num:]))
            amountList = []
            if expenseType == "EXACT":
                amountList = splitArgs
            if expenseType == "PERCENT":
                amountList = map(lambda x: roundNumber((x/100)*amount), splitArgs)
            for usr,amt in zip(owedBy, amountList):
                updateAmount(expenseBy, usr, amt)
                
            

        if "EQUAL" in inputList:
            amount = roundNumber(amount / num)
            for usr in owedBy:
                updateAmount(expenseBy,usr,amount)

        #Handle "EXACT" and "PERCENT"
        handleType(expenseType, splitArgs, owedBy)
        
        # Create Expense instance
        expense = Expense(self.users[expenseBy], amountToSplit, splitAmong, splitArgs, expenseType)

        # Add expense to each user's passbook
        for user in splitAmong:
            self.addExpenseToUsers(user, expense)
            
    def addExpenseToUsers(self, user, expense):
        """
        Adds expense to user's passbook

        Parameters:
            user (User): User object
            expense (Expense): Expense object to be added to user's passbook

        Returns:
            None
        """
        user.addExpense(expense)


    def show(self, inputList: List[str]):
        """
        Prints the balances responding to `SHOW` command.

        Parameters:
            inputList (list(str)): list of all words from command line.

        Returns:
            None
        """
    
        def printLine(pair):
            """
            Prints specific pair's balance from `self.balances`
            
            Paramters:
                pair (tuple): User pair from `self.balances`
            
            Returns:
                None
            """
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
    """
    Rounds the number to 2 decimal places if float. Or just gives the integer number.

    Parameter:
        number (int) or (float): Number to round
    
    Returns:
        (int) or (float)
    
    """
    if int(number) == number:
        return int(number)
    else:
        return round(number, 2)

