#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define F first
#define S second

const int MAXN = 1e5 + 10;
const int C = 26;

int n, cnt[C][MAXN], q;
string s;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;	cin >> te;
    for (int w = 1; w <= te; w++){
        cout << "Case #" << w << ": ";
        cin >> n >> q;
        cin >> s;
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; i++) {
            for (int w = 0; w < C; w++)
                cnt[w][i+1] = cnt[w][i];
            cnt[s[i]-'A'][i+1]++;
        }

        int ans = 0;
        while (q--){
            int l, r; cin >> l >> r, l--;
            int c = 0;
            for (int w = 0; w < C; w++)
                if ((cnt[w][r] - cnt[w][l])&1)
                    c++;
            ans += c <= 1;
        }
        cout << ans << "\n";
    }
    return 0;
}