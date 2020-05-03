#include <bits/stdc++.h>
using namespace std;

class User
{
public:
    string userId;
    User(){};
    User(string userId);
    User(string userId, string email, long long phoneNumber, string name);

protected:
    string email;
    long long phoneNumber;

private:
    string name;
};

User::User(string userId)
{
    this->userId = userId;
}

User::User(string userId, string email, long long phoneNumber, string name)
{
    this->userId = userId;
    this->email = email;
    this->phoneNumber = phoneNumber;
    this->name = name;
}