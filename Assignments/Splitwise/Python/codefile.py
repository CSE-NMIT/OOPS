import constant
import math
import array
from pprint import pprint as pp

class Splitwise(object):

    def __init__(self):

        self.user_list = []
        self.user_details = {}

        input("Create a user group. Add name: ")
        self.total_users = int(input("Enter the number of users: "))
        print("Automated users' details are as follows: ")

        for i in range(self.total_users):
            self.user_details["user_id"] = "00" + str(i)
            self.user_details["name"] = "User_" + str(i)
            self.user_details["email"] = "User" + str(i) + "@gmail.com"
            self.user_details["mob_no"] = "903456782" + str(i)
            self.user_details["due_amt"] = 0
            self.user_list.append(self.user_details)
            self.user_details = {}
        pp(self.user_list)

    def equal_distribution(self):
        exp_name = input("Add the name of expense: ")
        amt_spent = int(input("The amount spent is: "))
        eq_payable_amt = int(amt_spent/self.total_users)
        print("Each of the users of this group owes: ", eq_payable_amt)

    def unequal_distribution(self):


a = Splitwise()
a.equal_distribution()

