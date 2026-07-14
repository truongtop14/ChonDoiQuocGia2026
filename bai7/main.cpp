#include <bits/stdc++.h>
using namespace std;


int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int N, Q;

    cin >> N >> Q;


    vector<int> a(N + 1);


    for (int i = 1; i <= N; i++) {

        cin >> a[i];

    }


    while (Q--) {

        int type;

        cin >> type;


        if (type == 1) {

            int i, x;

            cin >> i >> x;

            a[i] = x;

        }
        else {

            int l, r;

            cin >> l >> r;


            int ans = a[l];


            for (int i = l + 1; i <= r; i++) {

                ans = max(ans, a[i]);

            }


            cout << ans << '\n';

        }

    }


    return 0;
}