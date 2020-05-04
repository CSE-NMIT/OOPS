#include <bits/stdc++.h>
#include "function_definitions.cpp"

using namespace std;

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
                user.getUser("");
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

            vector<string> argument;
            argument.push_back(paid_by);
            argument.push_back(amount);

            if (payment_type == "EQUAL")
            {
                argument.push_back("EQUAL");
                user.addExpense(argument, receivers);
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
            vector<string> arg(argument.size() + received_amount.size());
            vector<string>::iterator it;
            it = set_union(argument.begin(), argument.end(), received_amount.begin(), received_amount.end(), arg.begin());

            if (payment_type == "EXACT")
            {
                argument.push_back("EXACT");
                user.addExpense(arg, receivers);
            }

            else if (payment_type == "PERCENT")
            {
                argument.push_back("PERCENT");
                user.addExpense(arg, receivers);
            }
        }
    }
    return 0;
}