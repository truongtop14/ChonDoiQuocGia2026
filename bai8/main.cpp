#include <bits/stdc++.h>
using namespace std;

using ll = long long;


int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int N, Q;

    cin >> N >> Q;


    vector<ll> a(N + 1);


    for (int i = 1; i <= N; i++) {

        cin >> a[i];

    }


    while (Q--) {

        int type;

        cin >> type;


        if (type == 1) {

            int i;
            ll x;

            cin >> i >> x;

            a[i] = x;

        }
        else {

            int l, r;

            cin >> l >> r;


            // Kadane trên đoạn [l,r]

            ll cur = a[l];

            ll ans = a[l];


            for (int i = l + 1; i <= r; i++) {


                cur = max(a[i], cur + a[i]);


                ans = max(ans, cur);

            }


            cout << ans << '\n';

        }

    }


    return 0;
}