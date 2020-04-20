#include<bits/stdc++.h>

using namespace std;

int main()
{
    int cases; cin >> cases;
    for(auto cc{1}; cc <= cases; cc++)
    {
        int n; cin >> n;
        int64_t d; cin >> d;
        vector<int64_t> v;
        int num;
        for(auto i{0}; i < n; i++)
        {
            cin >> num;
            v.push_back(num);
        }


        for(auto i{n-1}; i >= 0; i--)
            d = d - (d % v[i]);

        cout << "Case #" << cc << ": " << d << "\n";
    }
}