#include <bits/stdc++.h>
using namespace std;

struct User_id
{
    string user_id;
    bool operator<(const User_id &t) const
    {
        return (this->user_id < t.user_id);
    }
};
class User
{
public:
    string user_name;
    string email;
    void createUser(string,string);
    void display_member(string);
};

struct Card_id
{
    string card_id;
    bool operator<(const Card_id &t) const
    {
        return (this->card_id < t.card_id);
    }
};
class Card : public User
{
public:
    string list__id;
    string card_name;
    string description;
    vector<string> assigned_user;
    void createCard(vector<string>);
    void deleteCard(string);
    void cardModify(string, string, string);
    void display_card(string);
};

struct List_id
{
    string list_id;
    bool operator<(const List_id &t) const
    {
        return (this->list_id < t.list_id);
    }
};
class List : public Card
{
public:
    string board__id;
    string list_name;
    vector<string> cards;
    void createList(vector<string>);
    void deleteList(string);
    void display_list(string);
};

struct Board_id
{
    string board_id;
    bool operator<(const Board_id &t) const
    {
        return (this->board_id < t.board_id);
    }
};

class Board : public List
{
public:
    string board_name;
    string privacy = "PUBLIC";
    string url;
    vector<string> members;
    vector<string> lists;
    void show(vector<Board>, vector<string>);
    void createBoard(string);
    void deleteBoard(string);
    void modify(string, string, string);
    void display_board(map<Board_id, Board>::iterator);
    void show(vector<string>);
};
