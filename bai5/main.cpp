#include <bits/stdc++.h>
using namespace std;


bool isPrime(int n) {

    if (n < 2)
        return false;

    if (n == 2)
        return true;

    if (n % 2 == 0)
        return false;


    for (int i = 3; i * 1LL * i <= n; i += 2) {

        if (n % i == 0)
            return false;

    }

    return true;
}



int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int N;

    cin >> N;


    int ans = 0;


    for (int i = 2; i <= N; i++) {

        if (isPrime(i))
            ans++;

    }


    cout << ans;


    return 0;
}