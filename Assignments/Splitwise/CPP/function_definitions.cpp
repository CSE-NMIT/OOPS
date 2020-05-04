#include <bits/stdc++.h>
#include "class.cpp"
using namespace std;

void Users::addUsers(vector<string> user)
{
    fullname = user;
    for (int i = 1; i <= user.size(); i++)
    {
        string temp = "u";
        ostringstream oss;
        oss << i;
        temp += oss.str();
        this->user_list.push_back(temp);
    }
    for (int i = 0; i < user.size(); i++)
    {
        for (int j = 0; j < user.size(); j++)
        {
            if (user_list[i] != user_list[j])
                this->users[user_list[i]].emplace(user_list[j], 0);
        }
    }
}

void Users::getUser(string input)
{
    if (this->flag == 0)
        cout << "No balances\n";
    else
    {
        if (input.length() == 0)
        {
            for (int i = 0; i < this->user_list.size(); i++)
            {
                for (int j = 0; j < this->user_list.size(); j++)
                {
                    if (this->user_list[i] != this->user_list[j])
                    {
                        if (this->users[this->user_list[i]][this->user_list[j]] != 0)
                            cout << this->fullname[i] << " owes " << this->fullname[j] << ": " << this->users[this->user_list[i]][this->user_list[j]] << endl;
                    }
                }
            }
        }
        else
        {
            int mark;
            for (int i = 0; i < user_list.size(); i++)
            {
                if (user_list[i] == input)
                {
                    mark = i;
                    break;
                }
                for (int i = 0; i < this->user_list.size(); i++)
                {
                    if (this->user_list[i] != input)
                    {
                        if (this->users[input][this->user_list[i]] != 0)
                            cout << fullname[mark] << " owes " << this->fullname[i] << ": " << this->users[input][this->user_list[i]] << endl;
                        else if (this->users[this->user_list[i]][input] != 0)
                            cout << this->fullname[i] << " owes " << fullname[mark] << ": " << this->users[this->user_list[i]][input] << endl;
                    }
                }
            }
        }
    }
}

void Users::addExpense(vector<string> a, vector<string> receivers)
{
    this->flag = 1;
    float amount;
    stringstream geek(a[1]);
    geek >> amount;
    if (a[a.size() - 1] == "EQUAL")
    {
        for (int i = 0; i < receivers.size(); i++)
        {
            if (receivers[i] != a[0])
            {
                if (this->users[a[0]][receivers[i]] >= amount / receivers.size())
                {
                    this->users[a[0]][receivers[i]] -= amount / receivers.size();
                    continue;
                }
                this->users[receivers[i]][a[0]] += amount / receivers.size();
            }
        }
    }
    else
    {
        vector<float> balance;
        float temp;
        for (int i = 2; i < a.size() - 1; i++)
        {
            stringstream change(a[i]);
            change >> temp;
            balance.push_back(temp);
        }
        if (a[a.size() - 1] == "EXACT")
        {
            for (int i = 0; i < receivers.size(); i++)
            {
                if (receivers[i] != a[0])
                {
                    if (this->users[a[0]][receivers[i]] <= balance[i])
                    {
                        balance[i] -= this->users[a[0]][receivers[i]];
                        this->users[a[0]][receivers[i]] = 0;
                        this->users[receivers[i]][a[0]] += balance[i];
                    }
                    else
                        this->users[a[0]][receivers[i]] -= balance[i];
                }
            }
        }
        else if (a[a.size() - 1] == "PERCENT")
        {
            for (int i = 0; i < receivers.size(); i++)
            {
                if (receivers[i] != a[0])
                {
                    if (this->users[a[0]][receivers[i]] <= (balance[i] * amount) / 100)
                    {
                        balance[i] = (balance[i] * amount) / 100;
                        balance[i] -= this->users[a[0]][receivers[i]];
                        this->users[a[0]][receivers[i]] = 0;
                        this->users[receivers[i]][a[0]] += balance[i];
                    }
                    else
                        this->users[a[0]][receivers[i]] -= (balance[i] * amount) / 100;
                }
            }
        }
    }
}