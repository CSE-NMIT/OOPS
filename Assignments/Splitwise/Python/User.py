
from typing import List

import Expense

class User: 
    def __init__(self,id,name):
        """
        Creates user instance of the user

        Parameters:
            id (str): user ID
            name (str): User's name
        
        Returns:
            None
        """
        self.__age = int()
        self.__mobile = str()
        self.name = name
        self.userId = id
        self.__passbook = []
    
    def addExpense(self, expense) :
        """
        Adds expense object to User's `self.__passbook` attribute

        Parameters:
            expense (Expense): Expense object to be added to passbook

        Returns:
            None
        """
        self.__passbook.append(expense)
    
    def printPassbook(self) :
        """
        Prints the `self.__passbook` in human readable format

        Parameters:
            None
        Returns:
            None
        """
        for expense in self.__passbook:
            print(expense.toString())
