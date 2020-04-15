class Solution{
    const int INF = 1e9 + 5;
public:
    int maxProfit(vector<int>& prices){
        int without = 0, with = -INF;
        for(int price: prices){
            with = max(with, without - price)
            without = max(without, with + price)
        }
        return without
    }
};