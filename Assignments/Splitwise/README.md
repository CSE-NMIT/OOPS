# Assignment - Split Wisely

## Problem Statement
Well, a lot have used splitwise (Atleast sharing people). havent we!. So why don't we go ahead and design this ??
Create an expense sharing application.
An expense sharing application is where you can add your expenses and split it among different people. 
The app keeps balances between people as in who owes how much to whom.

## Example
```
You live with 3 other friends.
You: User1 (id: u1)
Flatmates: User2 (u2), User3 (u3), User4 (u4)

This month's electricity bill was Rs. 1000.
Now you can just go to the app and add that you paid 1000,
select all the 4 people and then select split equally.
Input: u1 1000 4 u1 u2 u3 u4 EQUAL

For this transaction, everyone owes 250 to User1.
The app should update the balances in each of the profiles accordingly.

User2 owes User1: 250 (0+250)
User3 owes User1: 250 (0+250)
User4 owes User1: 250 (0+250)
---


Now, It is the BBD sale on Flipkart and there is an offer on your card.
You buy a few stuffs for User2 and User3 as they asked you to.
The total amount for each person is different.
Input: u1 1250 2 u2 u3 EXACT 370 880

For this transaction, User2 owes 370 to User1 and User3 owes 880 to User1.

The app should update the balances in each of the profiles accordingly.
User2 owes User1: 620 (250+370)
User3 owes User1: 1130 (250+880)
User4 owes User1: 250 (250+0)

---

Now, you go out with your flatmates and take your brother/sister along with you.
User4 pays and everyone splits equally. You owe for 2 people.
Input: u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20

For this transaction, User1 owes 480 to User4, User2 owes 240 to User4 and User3 owes 240 to User4.

The app should update the balances in each of the profiles accordingly.
User1 owes User4: 230 (250-480)
User2 owes User1: 620 (620+0)
User2 owes User4: 240 (0+240)
User3 owes User1: 1130 (1130+0)
User3 owes User4: 240 (0+240)
    
```
## Requirements

1. User: Each user should have a userId, name, email, mobile number.
2. Expense: Could either be EQUAL, EXACT or PERCENT
3. Users can add any amount, select any type of expense and split with any of the available users.
4. The percent and amount provided could have decimals upto two decimal places.
5. In case of percent, you need to verify if the total sum of percentage shares is 100 or not.
6. In case of exact, you need to verify if the total sum of shares is equal to the total amount or not.
7. The application should have a capability to show expenses for a single user as well as balances for everyone.
8. When asked to show balances, the application should show balances of a user with all the users where there is a non-zero balance.
9. The amount should be rounded off to two decimal places. Say if User1 paid 100 and amount is split equally among 3 people. Assign 33.34 to first person and 33.33 to others.

## Input
1. All inputs will be taken from STDIN. You will follow the same ** CODING RULES ** as followed in Hackerrank or other platforms
2. There will be 3 types of input:

1. New Users Addion: ``` ADD <no-of-users> <space-separated-list-of-user-names>```. The ID will be incremental in the form of ``` u1, u2, u3, u4... ```
2. Expense in the format: ``` EXPENSE <user-id-of-person-who-paid> <no-of-users> <space-separated-list-of-user-ids> <EQUAL/EXACT/PERCENT> <space-separated-values-in-case-of-non-equal> ```
3. Show balances for all: ``` SHOW ```
4. Show balances for a single user: ``` SHOW <user-id> ```

## Output
1. When asked to show balance for a single user. Show all the balances that user is part of:
2. Format: ``` <user-id-of-x> owes <user-id-of-y>: <amount> ```
3. If there are no balances for the input, print ``` No balances ```
4. In cases where the user for which balance was asked for, owes money, they’ll be x. They’ll be y otherwise.

## Sample Input
```
ADD 4 User1 User2 User3 User4
SHOW
SHOW u1
EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
SHOW u4
SHOW u1
EXPENSE u1 1250 2 u2 u3 EXACT 370 880
SHOW
EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
SHOW u1
SHOW
```

## Sample Output
```
No balances
No balances
User4 owes User1: 250
User2 owes User1: 250
User3 owes User1: 250
User4 owes User1: 250
User2 owes User1: 620
User3 owes User1: 1130
User4 owes User1: 250
User1 owes User4: 230
User2 owes User1: 620
User3 owes User1: 1130
User1 owes User4: 230
User2 owes User1: 620
User2 owes User4: 240
User3 owes User1: 1130
User3 owes User4: 240
```

## Expectations
1. Make sure that you have a working and demonstrable code
2. Make sure that the code is functionally correct
3. Code should be modular and readable
4. Separation of concern should be addressed
5. Please do not write everything in a single file
6. Code should easily accommodate new requirements and minimal changes
7. There should be a main method from where the code could be easily testable
8. [Optional] Write unit tests, if possible
9. No need to create a GUI

## Optional Requirements
Please do these only if you’ve time left. You can write your code such that these could be accommodated without changing your code much.

1. A way to add an expense name while adding the expense. Can also add notes, images, etc.
2. Option to split by share. Ex: ‘User4 pays and everyone splits equally. You pay for 2 people.’ could be added as: ``` u4 1200 4 u1 u2 u3 u4 SHARE 2 1 1 1 ```
3. A way to show the passbook for a user. The entries should show all the transactions a user was part of. You can print in any format you like.
4. There can be an option to simplify expenses. When simplify expenses is turned on (is true), the balances should get simplified. Ex: ‘User1 owes 250 to User2 and User2 owes 200 to User3’ should simplify to ‘User1 owes 50 to User2 and 200 to User3’.

## Your output here 
### Commandline Screenshot

![ ](test-sh.png)

### test.sh output

The test.sh execution is not reaching inside the first if statement after creating final file.


```
avinash@lenovo-budgie:~/Documents/OOPS$ ./test.sh Python Splitwise
Code Compile and Test
================PYTHON====================
==================Testing==================
```

out from program - 

```
No balances
No balances
User4 owes User1: 250
User2 owes User1: 250
User3 owes User1: 250
User4 owes User1: 250
User2 owes User1: 620
User3 owes User1: 1130
User4 owes User1: 250
User2 owes User1: 620
User3 owes User1: 1130
User1 owes User4: 230
User2 owes User1: 620
User3 owes User1: 1130
User1 owes User4: 230
User2 owes User4: 240
User3 owes User4: 240

```
