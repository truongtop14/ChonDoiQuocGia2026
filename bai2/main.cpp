#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<long long> a(n + 1);

    for (int i = 1; i <= n; i++)
        cin >> a[i];

    while (q--) {

        int l, r;
        cin >> l >> r;

        long long mn = a[l];

        for (int i = l + 1; i <= r; i++)
            mn = min(mn, a[i]);

        cout << mn << '\n';
    }

    return 0;
}