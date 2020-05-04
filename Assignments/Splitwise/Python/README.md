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



**No using PIP install**
