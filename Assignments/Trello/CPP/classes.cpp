#include <bits/stdc++.h>
using namespace std;

class User
{
public:
    int user_id;
    string user_name;
    string email;
};

class Card : public User
{
public:
    int card_id;
    string card_name;
    vector<User> assigned_user;
};

class List : public Card
{
public:
    int list_id;
    string list_name;
    vector<Card> cards;
};

class Board : public List
{
public:
    int board_id;
    string board_name;
    string privacy;
    string url;

private:
    vector<string> members;
    vector<string> lists;
};