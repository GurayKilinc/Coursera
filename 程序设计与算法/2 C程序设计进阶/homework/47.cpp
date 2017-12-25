#include <iostream>
using namespace std;

int jg(int x) {
    if(x == 1) {
        cout << "End" << endl;
        return 0;
    } else if(x % 2 != 0) {
        cout << x;
        x = x * 3 + 1;
        cout << "*3+1=" << x << endl;
        return jg(x);
    } else {
        cout << x;
        x = x / 2;
        cout << "/2=" << x << endl;
        return jg(x);
    }
}

int main() {
    int n;
    cin >> n;
    jg(n);

    return 0;
}