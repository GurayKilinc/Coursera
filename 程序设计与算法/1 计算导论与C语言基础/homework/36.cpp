#include <iostream>
using namespace std;

int main() {
    int n;
    bool y3, y5, y7;
    cin >> n;

    y3 = n%3;
    y5 = n%5;
    y7 = n%7;

    if (!y3 && !y5 && !y7) {
        cout << 3 << ' ' << 5 << ' ' << 7 << endl;
    } else if (!y3 && !y5) {
        cout << 3 << ' ' << 5 << endl;
    } else if (!y3 && !y7) {
        cout << 3 << ' ' << 7 << endl;
    } else if (!y5 && !y7) {
        cout << 5 << ' ' << 7 << endl;
    } else if (!y3) {
        cout << 3 << endl;
    } else if (!y5) {
        cout << 5 << endl;
    } else if (!y7) {
        cout << 7 << endl;
    } else {
        cout << 'n' << endl;
    }

    return 0;
}