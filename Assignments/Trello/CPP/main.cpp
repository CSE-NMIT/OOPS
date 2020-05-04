#include<bits/stdc++.h>
#include "classes.cpp"

int main()
{
    vector<Board> b;
    string initials;
    while(1)
    {
        cin>>initials;
        if(initials=="BOARD")
        {
            string board_parameter_one;
            cin>>board_parameter_one;
            if(board_parameter_one[0]=='C')
            {
                cin>>board_parameter_one;
                Board temp;
                temp.board_name=board_parameter_one;
                b.push_back(temp);
            }
            else if(board_parameter_one[0]=='D')
            {

            }
            else
            {
                int id;
                stringstream one(board_parameter_one);
                one>>id;

            }
        }
    }
    return 0;
}