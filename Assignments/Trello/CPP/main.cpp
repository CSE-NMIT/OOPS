#include <bits/stdc++.h>
#include "functions.cpp"
using namespace std;

int main()
{
    Board b;
    while (1)
    {
        string input;
        getline(cin, input);
        int i = 0;
        if (input[0] == 'B')
        {
            string board_parameter;
            int mark;
            while (input[i] != ' ')
                i++;
            mark = ++i;
            if (input[mark] == 'C' || input[mark] == 'D')
            {
                while (input[i] != ' ')
                    i++;
                i++;
                while (i < input.length())
                    board_parameter += input[i++];
                if (input[mark] == 'C')
                    b.createBoard(board_parameter);
                else if (input[mark] == 'D')
                    b.deleteBoard(board_parameter);
            }
            else
            {
                while (input[i] != ' ')
                    board_parameter += input[i++];
                i++;
                string command, value;
                while (input[i] != ' ')
                    command += input[i++];
                i++;
                while (i < input.length())
                    value += input[i++];
                b.modify(board_parameter, command, value);
            }
        }
        else if (input[0] == 'S')
        {
            vector<string> params;
            string value;
            if (input.length() == 4)
            {
                b.show(params);
                continue;
            }
            if (input[5] == 'C')
            {
                i = 10;
                while (i < input.size())
                    value += input[i++];
                params.push_back("CARD");
                params.push_back(value);
                b.show(params);
            }
            else if (input[5] == 'L')
            {
                i = 10;
                while (i < input.size())
                    value += input[i++];
                params.push_back("LIST");
                params.push_back(value);
                b.show(params);
            }
            else if (input[5] == 'B')
            {
                i = 11;
                while (i < input.size())
                    value += input[i++];
                params.push_back("BOARD");
                params.push_back(value);
                b.show(params);
            }
        }
        else if (input[0] == 'L')
        {
            vector<string> params;
            string board_id;
            if (input[5] == 'C' || input[5] == 'D')
            {
                i = 12;
                while (input[i] != ' ' && i < input.length())
                    board_id += input[i++];
                if (input[5] == 'C')
                {
                    i++;
                    string l_name;
                    while (i < input.length())
                        l_name += input[i++];
                    params.push_back(board_id);
                    params.push_back(l_name);
                    b.createList(params);
                }
                else if (input[5] == 'D')
                    b.deleteList(board_id);
            }
            else
            {
                i = 5;
                string value;
                while (input[i] != ' ')
                    board_id += input[i++];
                i++;
                while (input[i] != ' ')
                    i++;
                i++;
                while (i < input.length())
                    value += input[i++];
                b.modify("List", board_id, value);
            }
        }
        else if (input[0] == 'C')
        {
            if (input[5] == 'C' || input[5] == 'D')
            {
                string id;
                i = 12;
                while (input[i] != ' ' && i < input.length())
                    id += input[i++];
                if (input[5] == 'C')
                {
                    vector<string> params;
                    params.push_back(id);
                    i++;
                    string name;
                    while (i < input.length())
                        name += input[i++];
                    params.push_back(name);
                    b.createCard(params);
                }
                else
                    b.deleteCard(id);
            }
            else
            {
                i = 5;
                string card_id;
                while (input[i] != ' ')
                    card_id += input[i++];
                string command;
                i++;
                while (input[i] != ' ' && i < input.length())
                    command += input[i++];
                string value;
                if (command[0] != 'U')
                {
                    i++;
                    while (i < input.length())
                        value += input[i++];
                }
                else
                    value = "";
                b.cardModify(card_id, command, value);
            }
        }
        else if (input[0] == 'U')
        {
            string name;
            string email;
            i = 12;
            while (input[i] != ' ')
                name += input[i++];
            i++;
            while (i < input.length())
                email += input[i++];
            b.createUser(name, email);
        }
    }
    return 0;
}