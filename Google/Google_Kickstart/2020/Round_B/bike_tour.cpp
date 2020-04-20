#include<bits/stdc++.h>

using namespace std;

int main()
{
    int cases;
    scanf("%d", &cases);
    for(auto cc{1}; cc <= cases; cc++)
    {
        int N, num;
        scanf("%d", &N);
        vector<int> v;
        for(auto i{0}; i < N; i++)
        {
            scanf("%d", &num);
            v.push_back(num);
        }

        int cnt{0};
        for(auto i{1}; i < N-1; i++)
        {
            if(v[i] > v[i-1] && v[i] > v[i+1])
                cnt++;
        }

        printf("Case #%d: %d\n", cc, cnt);
    }
}