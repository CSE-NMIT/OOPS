#include <bits/stdc++.h>
using namespace std;
class Users
{
public:
    map<string, map<string, float>> users;
    void addUsers(vector<string>);
    void getUser(string);
    void getUser();
    void addExpense(string, string, string, vector<string>);
    void addExpense(string, vector<string>, vector<string>);
    void addExpense(string, vector<string>, vector<string>, string);

private:
    int flag = 0; //This marks whether any payment hs been made or not.
    vector<string> user_list;
    vector<string> fullname;
};

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
void Users::getUser()
{
    if (this->flag == 0)
        cout << "No balances\n";
    else
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
}
void Users::getUser(string input)
{
    int mark;
    for (int i = 0; i < user_list.size(); i++)
    {
        if (user_list[i] == input)
        {
            mark = i;
            break;
        }
    }
    if (this->flag == 0)
        cout << "No balances\n";
    else
    {
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
void Users::addExpense(string paid_by, string money, string number, vector<string> receivers)
{
    this->flag = 1;
    float amount;
    int number_of_receivers;
    stringstream geek(money);
    stringstream geek1(number);
    geek >> amount;
    geek1 >> number_of_receivers;
    for (int i = 0; i < receivers.size(); i++)
    {
        if (receivers[i] != paid_by)
        {
            if (this->users[paid_by][receivers[i]] >= amount / number_of_receivers)
            {
                this->users[paid_by][receivers[i]] -= amount / number_of_receivers;
                continue;
            }
            this->users[receivers[i]][paid_by] += amount / number_of_receivers;
        }
    }
}
void Users::addExpense(string paid_by, vector<string> receivers, vector<string> received_amount)
{
    this->flag = 1;
    vector<float> balance;
    float temp;
    for (int i = 0; i < received_amount.size(); i++)
    {
        stringstream change(received_amount[i]);
        change >> temp;
        balance.push_back(temp);
    }
    for (int i = 0; i < receivers.size(); i++)
    {
        if (receivers[i] != paid_by)
        {
            if (this->users[paid_by][receivers[i]] <= balance[i])
            {
                balance[i] -= this->users[paid_by][receivers[i]];
                this->users[paid_by][receivers[i]] = 0;
                this->users[receivers[i]][paid_by] += balance[i];
            }
            else
                this->users[paid_by][receivers[i]] -= balance[i];
        }
    }
}
void Users::addExpense(string paid_by, vector<string> receivers, vector<string> received_percent, string money)
{
    this->flag = 1;
    float amount;
    stringstream geek(money);
    geek >> amount;
    vector<float> balance;
    float temp;
    for (int i = 0; i < received_percent.size(); i++)
    {
        stringstream change(received_percent[i]);
        change >> temp;
        balance.push_back(temp);
    }
    for (int i = 0; i < receivers.size(); i++)
    {
        if (receivers[i] != paid_by)
        {
            if (this->users[paid_by][receivers[i]] <= (balance[i] * amount) / 100)
            {
                balance[i] = (balance[i] * amount) / 100;
                balance[i] -= this->users[paid_by][receivers[i]];
                this->users[paid_by][receivers[i]] = 0;
                this->users[receivers[i]][paid_by] += balance[i];
            }
            else
                this->users[paid_by][receivers[i]] -= (balance[i] * amount) / 100;
        }
    }
}

int main()
{
    Users user;
    string get_input;
    while (get_input.length())
    {
        getline(cin, get_input);
        string initials = "";
        int i = 0;
        while (get_input[i] != ' ' && i != get_input.length())
            initials += get_input[i++];
        if (initials == "ADD")
        {
            vector<string> user_list;
            i++;
            while (get_input[i] != ' ')
                i++;
            i++;
            for (; i < get_input.length(); i++)
            {
                string str = "";
                while (get_input[i] != ' ' && i != get_input.length())
                    str += get_input[i++];
                user_list.push_back(str);
            }
            user.addUsers(user_list);
        }
        else if (initials == "SHOW")
        {
            if (get_input.length() == 4)
                user.getUser();
            else
            {
                string str = "";
                int i = 5;
                while (i < get_input.length())
                    str += get_input[i++];
                user.getUser(str);
            }
        }
        else if (initials == "EXPENSE")
        {
            i++;
            string paid_by = "";
            while (get_input[i] != ' ')
                paid_by += get_input[i++];
            i++;
            string amount = "";
            while (get_input[i] != ' ') //Amount paid
                amount += get_input[i++];
            i++;
            string number = "";
            while (get_input[i] != ' ') //Number of users
                number += get_input[i++];
            i++;
            vector<string> receivers;
            string user1 = "";
            while (get_input[i] != 'E' && get_input[i] != 'P')
            {
                if (get_input[i] == ' ')
                {
                    receivers.push_back(user1);
                    i++;
                    user1 = "";
                }
                else
                    user1 += get_input[i++];
            }
            string payment_type = "";
            while (get_input[i] != ' ' && i != get_input.length()) //Get payment type
                payment_type += get_input[i++];
            i++;
            if (payment_type == "EQUAL")
            {
                user.addExpense(paid_by, amount, number, receivers);
                continue;
            }

            vector<string> received_amount;
            user1 = "";
            while (i < get_input.size())
            {
                if (get_input[i] == ' ')
                {
                    received_amount.push_back(user1);
                    i++;
                    user1 = "";
                }
                else
                    user1 += get_input[i++];
            }
            received_amount.push_back(user1);
            if (payment_type == "EXACT")
                user.addExpense(paid_by, receivers, received_amount);
            else if (payment_type == "PERCENT")
                user.addExpense(paid_by, receivers, received_amount, amount);
        }
    }
    return 0;
}