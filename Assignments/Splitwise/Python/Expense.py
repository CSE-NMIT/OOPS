from typing import List
import User

class Expense : 
    def __init__(self, 
            expenseBy, 
            amount,
            splitAmong, 
            splitArgs, 
            expenseType):
        self.expenseBy = expenseBy
        self.amount = amount
        self.splitAmong = splitAmong
        self.splitArgs = splitArgs
        self.expenseType = expenseType


    def toString(self):

        splitAmongString = ""
        
        for user in self.splitAmong:
            splitAmongString += user.name + " "
        splitArgsString = ""
        
        for arg in self.splitArgs:
            splitArgsString += str(arg) + " "
        
        string  = self.expenseBy.name + "paid " + str(self.amount) + " split among " + splitAmongString + " as " + self.expenseType + " " + splitArgsString

        return string