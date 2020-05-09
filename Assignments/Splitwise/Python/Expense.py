from typing import List
import User

class Expense : 
    def __init__(self, 
            expenseBy, 
            amount,
            splitAmong, 
            splitArgs, 
            expenseType):
        """
        Constructor for Expense class. creates the complete expense instance.

        Parameters:
            expenseBy (User): User object of the expense bearer.
            amount (int) or (float): Amount that needs to be split
            splitAmong (list(User)) : List of user objects of users among whom
                                      the expense needs to be split
            expenseType (str): The type of expense (EXACT/EQUAL/PERCENT)
        
        Returns:
            None
        """
        self.expenseBy = expenseBy
        self.amount = amount
        self.splitAmong = splitAmong
        self.splitArgs = splitArgs
        self.expenseType = expenseType


    def toString(self):
        """
        Converts Expense object to human readable format.

        Parameters:
            None

        Returns:
            (str) : Human readable string of Expense object
        """
        splitAmongString = ""
        
        for user in self.splitAmong:
            splitAmongString += user.name + " "
        splitArgsString = ""
        
        for arg in self.splitArgs:
            splitArgsString += str(arg) + " "
        
        string  = self.expenseBy.name + "paid " + str(self.amount) + " split among " + splitAmongString + " as " + self.expenseType + " " + splitArgsString

        return string