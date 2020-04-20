#include<bits/stdc++.h>

using namespace std;

auto func(vector<pair<char, int>> counts)
{
    int cnt_i = 1;
    int cnt_j = 1;
    pair<int, int> coords;
    for(pair<char, int> pr : counts)
    {
        char x = pr.first;
        switch(x)
        {
            case 'S':
                cnt_i += pr.second;
                break;
            case 'N':
                cnt_i -= pr.second;
                break;
            case 'E':
                cnt_j += pr.second;
                break;
            case 'W':
                cnt_j -= pr.second;
                break;
        }
    }
    coords.first = cnt_i;
    coords.second = cnt_j;
    return coords;
}

int main()
{
    const int max = 1000000000;
    int cc; cin >> cc;
    for(auto l{1}; l <= cc; l++)
    {
        string program;
        cin >> program;
        string str = "";
        int mult = 1;
        vector<pair<char, int>> counts;
        stack<int> X;
        for(char c : program)
        {
            pair<char, int> pr;
            if(isdigit(c))
            {
                int num = c - '0';
                mult *= (num);
                X.push(num);
            }
            else if(c != '(' and c != ')')
            {
                pr.first = c;
                pr.second = mult;
                counts.push_back(pr);
            }
            else if(c == ')')
            {
                mult /= X.top();
                X.pop();
            }
        }

        pair<int, int> coords = func(counts);
        if(coords.first <= 0)
            coords.first = max + coords.first;
        if(coords.second <= 0)
            coords.second = max + coords.second;
        cout << "Case #" << l << ": "<< coords.second << " " << coords.first << "\n";
    }
}