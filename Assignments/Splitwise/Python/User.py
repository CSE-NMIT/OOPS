
from typing import List

import Expense

class User: 
    def __init__(self,id,name):
        self.__age = int()
        self.__mobile = str()
        self.name = name
        self.userId = id
        self.__passbook = []
    
    def addExpense(self, expense) :
        self.__passbook.append(expense)
    
    def printPassbook(self) :
        for expense in self.__passbook:
            print(expense.toString())
