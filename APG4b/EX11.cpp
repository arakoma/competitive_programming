/*
for (初期化; 条件式; 更新) {
    処理
}

//N回回す
for (int i = 0; i < N; i++) {
    処理
}
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A;
    cin >> N >> A;

    // ここにプログラムを追記
    string op;
    int B;
    for (int i = 0; i < N; i++) {
        cin >> op >> B;
        if (op == "+") {
            A += B;
        }
        else if (op == "-") {
            A -= B;
        }
        else if (op == "*") {
            A *= B;
        }
        else if (op == "/" && B != 0) {
            A /= B;
        }
        else {
            cout << "error" << endl;
            break;
        }
        cout << i+1 << ":" << A << endl;
    }
}
