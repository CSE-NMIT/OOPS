#include <bits/stdc++.h>
#include "classes.cpp"
using namespace std;

hash<string> hashing;
map<Board_id, Board> board;
map<List_id, List> list1;
map<User_id, User> users;
map<Card_id, Card> card1;

void User::createUser(string name, string email)
{
    User u;
    u.user_name = name;
    u.email = email;
    User_id us = {to_string(hashing(name))};
    users[us] = u;
    cout << "Created user: " << us.user_id << endl;
}

void Board::createBoard(string b_name)
{
    Board temp;
    Board_id b = {to_string(hashing(b_name))};
    temp.board_name = b_name;
    board[b] = temp;
    cout << "Created board: " << b.board_id << endl;
}

void Board::deleteBoard(string b_id)
{
    map<Board_id, Board>::iterator i;
    for (i = board.begin(); i != board.end(); i++)
    {
        if (i->first.board_id == b_id)
        {
            board.erase(i);
            break;
        }
    }
}

void List::createList(vector<string> params)
{
    List temp;
    temp.list_name = params[1];
    temp.board__id = params[0];
    List_id l = {to_string(hashing(params[1]))};
    list1[l] = temp;
    Board_id b = {params[0]};
    board[b].lists.push_back(l.list_id);
    cout << "Created list: " << l.list_id << endl;
}

void List::deleteList(string id)
{
    List_id l = {id};
    Board_id b = {list1[l].board__id};
    vector<string>::iterator i;
    for (i = board[b].lists.begin(); i != board[b].lists.end(); i++)
    {
        if (*i == id)
        {
            board[b].lists.erase(i);
            break;
        }
    }
    for (auto j = list1.begin(); j != list1.end(); j++)
    {
        if (j->first.list_id == id)
        {
            list1.erase(j);
            break;
        }
    }
}

void Card::createCard(vector<string> params)
{
    Card c;
    c.card_name = params[1];
    c.list__id = params[0];
    Card_id car = {to_string(hashing(params[1]))};
    card1[car] = c;
    List_id l = {params[0]};
    list1[l].cards.push_back(car.card_id);
    cout << "Created card: " << car.card_id << endl;
}

void Card::deleteCard(string id)
{
    Card_id c = {id};
    List_id l = {card1[c].list__id};
    for (auto i = card1.begin(); i != card1.end(); i++)
    {
        if (i->first.card_id == id)
        {
            card1.erase(i);
            break;
        }
    }
    vector<string>::iterator i;
    for (i = list1[l].cards.begin(); i != list1[l].cards.end(); i++)
    {
        if (*i == id)
        {
            list1[l].cards.erase(i);
            break;
        }
    }
}

void Board::modify(string id, string command, string value)
{
    if (id[0] == 'L')
    {
        for (auto j = list1.begin(); j != list1.end(); j++)
        {
            if (j->first.list_id == command)
            {
                j->second.list_name = value;
                break;
            }
        }
        return;
    }
    Board_id b = {id};
    if (command[0] == 'n')
        board[b].board_name = value;
    else if (command[0] == 'p')
        board[b].privacy = value;
    else if (command[0] == 'A')
        board[b].members.push_back(value);
    else if (command[0] == 'R')
    {
        vector<string>::iterator i;
        for (i = board[b].members.begin(); i < board[b].members.end(); i++)
        {
            if (*i == value)
            {
                board[b].members.erase(i);
                break;
            }
        }
    }
}

void Card::cardModify(string id, string command, string value)
{
    Card_id c = {id};
    if (command[0] == 'n')
        card1[c].card_name = value;
    else if (command[0] == 'd')
        card1[c].description = value;
    else if (command[0] == 'A')
        card1[c].assigned_user.push_back(value);
    else if (command[0] == 'U')
        card1[c].assigned_user.clear();
    else if (command[0] == 'M')
    {
        List_id l = {card1[c].list__id};
        vector<string>::iterator i;
        for (i = list1[l].cards.begin(); i != list1[l].cards.end(); i++)
        {
            if (*i == id)
            {
                list1[l].cards.erase(i);
                break;
            }
        }
        l = {value};
        list1[l].cards.push_back(id);
    }
}

void Board::show(vector<string> params)
{
    if (board.size() == 0 && params.size() == 0)
    {
        cout << "No boards" << endl;
        return;
    }
    if (params.size() == 0)
    {
        int count = board.size(), flag = 0;
        if (count > 0)
        {
            cout << "[";
            flag = 1;
        }
        map<Board_id, Board>::iterator i;
        for (i = board.begin(); i != board.end(); i++)
        {
            display_board(i);
            if (--count)
                cout << ", ";
        }
        if (flag)
            cout << "]" << endl;
        else
            cout << endl;
    }
    else
    {
        if (params[0][0] == 'B')
        {
            map<Board_id, Board>::iterator i;
            int marker = 1;
            for (i = board.begin(); i != board.end(); i++)
            {
                if (i->first.board_id == params[1])
                {
                    display_board(i);
                    marker = 0;
                    break;
                }
            }
            if (marker)
                cout << "Board " << params[1] << " does not exist";
            cout << endl;
        }
        else if (params[0][0] == 'C')
        {
            display_card(params[1]);
            cout << endl;
        }
        else if (params[0][0] == 'L')
        {
            display_list(params[1]);
            cout << endl;
        }
    }
}

void Board::display_board(map<Board_id, Board>::iterator i)
{
    cout << "{\"id\": \"" << i->first.board_id << "\", \"name\": \"" << i->second.board_name << "\", \"privacy\": \"" << i->second.privacy << "\"}";
    if (i->second.lists.size() > 0)
    {
        vector<string>::iterator j;
        int count = i->second.lists.size(), flag = 0;
        if (count > 0)
        {
            cout << ", \"lists\": ";
            cout << "[";
            flag = 1;
        }
        for (j = i->second.lists.begin(); j != i->second.lists.end(); j++)
        {
            display_list(*j);
            if (--count)
                cout << ", ";
        }
        if (flag)
            cout << "]";
    }
    if (i->second.members.size() > 0)
    {
        vector<string>::iterator j;
        int count = i->second.members.size(), flag = 0;
        if (count > 0)
        {
            cout << ", \"members\": ";
            cout << "[";
            flag = 1;
        }
        for (j = i->second.members.begin(); j != i->second.members.end(); j++)
        {
            display_member(*j);
            if (--count)
                cout << ", ";
        }
        if (flag)
            cout << "]";
    }
}

void User::display_member(string user_id)
{
    User_id u = {user_id};
    cout << "{\"id\": \"" << user_id << "\", \"name\": \"" << users[u].user_name << "\", \"email\": \"" << users[u].email << "\"}";
}

void Card::display_card(string card_id)
{
    Card_id c = {card_id};
    if (card1.find(c) == card1.end())
    {
        cout << "Card " << card_id << " does not exist";
        return;
    }
    cout << "{\"id\": \"" << card_id << "\", \"name\": \"" << card1[c].card_name << "\", \"description\": \"" << card1[c].description << "\"";
    if (card1[c].assigned_user.size() > 0)
    {
        vector<string>::iterator j;
        int count = card1[c].assigned_user.size(), flag = 0;
        if (count > 0)
        {
            cout << ", \"assignedTo\": ";
            cout << "[";
            flag = 1;
        }
        for (j = card1[c].assigned_user.begin(); j != card1[c].assigned_user.end(); j++)
        {
            display_member(*j);
            if (--count)
                cout << ", ";
        }
        if (flag)
            cout << "]";
    }
    cout << "}";
}

void List::display_list(string list_id)
{
    List_id l = {list_id};
    if (list1.find(l) == list1.end())
    {
        cout << "List " << list_id << " does not exist";
        return;
    }
    cout << "{\"id\": \"" << list_id << "\", \"name\": \"" << list1[l].list_name;
    if (list1[l].cards.size() > 0)
    {
        vector<string>::iterator j;
        int count = list1[l].cards.size(), flag = 0;
        if (count > 0)
        {
            cout << ", \"cards\": ";
            cout << "[";
            flag = 1;
        }
        for (j = list1[l].cards.begin(); j != list1[l].cards.end(); j++)
        {
            display_card(*j);
            if (--count)
                cout << ", ";
        }
        if (flag)
            cout << "]";
    }
    cout << "\"}";
}
