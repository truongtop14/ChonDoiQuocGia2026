#include <bits/stdc++.h>
using namespace std;

#define ll long long

const ll INF = 4e18;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;

    cin >> N >> K;

    vector<ll> a(N + 1);
    vector<ll> sum(N + 1, 0);

    for (int i = 1; i <= N; i++) {

        cin >> a[i];

        sum[i] = sum[i-1] + a[i];
    }


    vector<vector<ll>> dp(K + 1,
                         vector<ll>(N + 1, INF));


    // chia 0 xe cho 0 kiện
    dp[0][0] = 0;


    for (int k = 1; k <= K; k++) {

        for (int i = 1; i <= N; i++) {


            // điểm cắt trước đó
            for (int j = 0; j < i; j++) {


                if (dp[k-1][j] == INF)
                    continue;


                // tải xe cuối
                ll last = sum[i] - sum[j];


                // tải lớn nhất
                ll cost = max(dp[k-1][j], last);


                dp[k][i] = min(dp[k][i], cost);

            }
        }
    }


    cout << dp[K][N];

    return 0;
}