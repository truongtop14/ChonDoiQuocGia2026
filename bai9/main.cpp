#include <bits/stdc++.h>
using namespace std;


bool checkPrefix(string s, string p) {

    if (p.size() > s.size())
        return false;

    for (int i = 0; i < (int)p.size(); i++) {

        if (s[i] != p[i])
            return false;

    }

    return true;
}


int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int Q;

    cin >> Q;


    vector<string> dict;


    while (Q--) {


        int type;

        string s;

        cin >> type >> s;


        // Thêm từ
        if (type == 1) {

            dict.push_back(s);

        }


        // Xóa một lần xuất hiện
        else if (type == 2) {


            for (int i = 0; i < (int)dict.size(); i++) {

                if (dict[i] == s) {

                    dict.erase(dict.begin() + i);

                    break;

                }

            }

        }


        // Đếm tiền tố
        else {


            int ans = 0;


            for (string x : dict) {

                if (checkPrefix(x, s))
                    ans++;

            }


            cout << ans << '\n';

        }

    }


    return 0;
}