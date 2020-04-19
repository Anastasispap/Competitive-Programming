#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    int cases;
    scanf("%d", &cases);
    for(auto i{1}; i <= cases; i++)
    {
		int n; cin >> n;
		int64_t d; cin >> d;
		vector<int64_t> v(n);
		
		for(auto j{0}; j < n; j++)
			cin >> v[j];
		
		for(auto j{n-1}; j >= 0; j--)
			d = d - (d % v[j]);
		
		cout << "Case #" << i << ": " << d << "\n";
    }
}
