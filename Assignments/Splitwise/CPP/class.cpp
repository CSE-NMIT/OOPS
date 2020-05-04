#include <bits/stdc++.h>
using namespace std;

class Users
{
public:
    map<string, map<string, float>> users;
    void addUsers(vector<string>);
    void getUser(string);
    void addExpense(vector<string>, vector<string>);

private:
    int flag = 0; //This marks whether any payment has been made or not.
    vector<string> user_list;
    vector<string> fullname;
};
