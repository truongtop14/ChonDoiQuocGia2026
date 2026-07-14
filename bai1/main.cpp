#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long K;
    cin >> N >> K;

    vector<int> a(N);

    int mx = 0;

    for (int i = 0; i < N; i++) {
        cin >> a[i];
        mx = max(mx, a[i]);
    }

    int ans = 0;

    for (int len = 1; len <= mx; len++) {

        long long cnt = 0;

        for (int x : a) {
            cnt += x / len;
        }

        if (cnt >= K)
            ans = len;
    }

    cout << ans;

    return 0;
}