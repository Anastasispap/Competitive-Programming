#include<bits/stdc++.h>

using namespace std;

int main()
{
	int cc; cin >> cc;
	
	int n;
	for(auto c{0}; c < cc; c++)
	{
		vector<int> v;
		cin >> n;
		for(auto i{0}; i < n; i++)		
			cin >> v[i];
		
		auto cnt{0};
		for(auto i{1}; i < n-1; i++)
		{
			if(v[i] > v[i-1] && v[i] > v[i+1])
				cnt++;
		}
		printf("Case #%d: %d\n", c+1, cnt);
	}
}
			
