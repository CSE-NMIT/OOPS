# Detailed Approach - Explain the approach how Problem was solved

 - `class user` stores the information of each user like `userId`, `name`, `age`(private) and `mobile`(private)


In `main.py`  -

 - `class ProcessInput` defines all the methods that are specified in the instruction set i.e. `ADD`, `EXPENSE` and `SHOW`
 
 - `class ProcessInput` also has two attributes namely `users` and `owes`

 - Attribute `users` is a dictionary that stores instances of `user` class as values and their respective `user.userId` as the corresponding key.

 - Attribute `owes` stores the EXPENSE details as the amount owed as the value and the tuple of 2 users as the corresponding key. This helps in saving some memory and computation time compared to saving an instance of each user mapped to another user.

E.g.
 ```
    owes = {
        ('u1','u2') : 240,   # This means that u2 owes u1 a sum of 240
        ('u1','u3') : -120   # This means that u1 owes u3 a sum of 120
    }
 ```

 - The method `processADD(self, inputList: List[str]` takes in the whole input line containing the keyword ADD as list of separated words. The method then reads all the user names and creates instancs of `user` class giving them a `userId` marked in numbers in the order they appear. It then stores the users in the `ProcessInput.users` data structore.

 - The method `processExpense(self, inputList : List[str])` takes in the whole input line containing the keyword EXPENSE as list of separated words. The method then reads the user the money is owed to and the users money is owedBy, and then updates the `ProcessInput.owes` data structure.

 - The method `processShow(self, inputList: List[str])` takes in the whole input line containing the keyword SHOW as list of separated words. the method then checks for any additional arguments, if none just prints out the user names and the money owed by them. If there is another argument, it shows all the expenses related to that user only.

## Update 1 

- class `Group` will be formed for each group. (As an extension to requirements, there can be multiple groups of people to handle).
  - `users` attribute will store all the users in the group.
  - `expenses` attribute will store all the EXPENSE class instances, this will help in tracking all  the transactions. (This is not ideal for memory, probably storing each expense into a file or database would be better, and instead of tracking a bunch of expenses, each addExpense function call would store the expense into a file/DB. But then this applies to all the attributes in general.)
  - `balances` attribute (previously `owes`) stays the same tracking the current balances among the users. (This is probably a bit expensive in terms memory but will be faster in execution.)
  - `processAdd` method can now be the constructor of the `class Group` this will create a group of users. This also provides the flexibility of adding users to the group later.
  - `processExpense` method can now be `addExpense` with the same parameters.
  - `processShow` method can now be `show` with the same parameters.

- `class Expense` will be tracking each transaction.
  - `expenseType` attribute will store the type of expense (i.e. EQUAL/PERCENT/EXACT/SHARE). I can use an enum for the same.
  - `expenseBy` attribute will track all the user who made the payment initially.
  - `amount` attribute will store the information on the amount paid.
  - `splitAmong` (list) attribute will store all the users among which the expense is to be split.
  - `splitArgs` this attribute stores the PERCENT/EXACT split arguments.
  - `toString()` method returns a human readable string format of the expense object.

- `class User` has a new attribute named `passbook` (Private) which stores the expenses the user was a part of.



**No using PIP install**
