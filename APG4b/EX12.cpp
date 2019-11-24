/*
文字列.size() //文字列の長さ
文字列.at(i) //i文字目(char型)
string型は全角文字を扱えない(別の文字列型を使う)
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;

    // ここにプログラムを追記
    int sum = 1;
    for (int i = 1; i < S.size(); i++) {
        if (S.at(i) == '+') {
            sum++;
        }
        else if (S.at(i) == '-') {
            sum--;
        }
    }
    cout << sum << endl;
}
