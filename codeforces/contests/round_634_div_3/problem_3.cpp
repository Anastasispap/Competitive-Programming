#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;

#include <unordered_map>

auto countDuplicutes(int arr[1000])
{
	std::unordered_map<int, int> retv;
	for(int i = 0; i < 1000; ++i)
		++retv[iarr[i]];


return retv;
}

int main()
{
    int cc, num, n;
    scanf("%d", &cc);
    vector<int> vectr;
    unordered_set<int> un_set;
    for(auto i{0}; i < cc; i++)
    {
	scanf("%d", &n);
	for(auto j{0}; j < n; j++)
	{
	    scanf("%d", &num);
	    vectr.push_back(num);
	    un_set.insert(num);
	}

	sort(vectr.begin(), vectr.end());
	int uniqueCount = unique(vectr.begin(), vectr.end()) - vectr.begin();

    }
}
