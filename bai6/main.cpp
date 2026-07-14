#include <bits/stdc++.h>
using namespace std;

struct Point {

    long long x, y;

};


double dist(Point a, Point b) {

    long long dx = a.x - b.x;
    long long dy = a.y - b.y;

    return sqrt((double)dx * dx + (double)dy * dy);
}


int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int N;

    cin >> N;


    vector<Point> p(N);


    for (int i = 0; i < N; i++) {

        cin >> p[i].x >> p[i].y;

    }


    double ans = 1e18;


    for (int i = 0; i < N; i++) {

        for (int j = i + 1; j < N; j++) {

            ans = min(ans, dist(p[i], p[j]));

        }

    }


    cout << fixed << setprecision(6) << ans;


    return 0;
}