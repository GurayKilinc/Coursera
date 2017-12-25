#include <iostream>

using namespace std;

int main() {
    int n, x, y;
    double out;
    cin >> n >> x >> y;
    if (y%x == 0) {
        n = n - y/x;
    } else {
        n = n - y/x - 1;
    }
    cout << n << endl;
    return 0;
}