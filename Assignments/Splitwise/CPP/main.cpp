//Basic testing

#include <bits/stdc++.h>
#include "user.cpp"

using namespace std;

class Account : public User
{
public:
    User user;
    float amount;
    Account(string user);
    void setAmount(float amount);
};

Account::Account(string user)
{
    this->user = user;
};

int main()
{
    return 0;
}
