#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n%4 == 0) {
        if (n%100 == 0 && n%400 != 0) {
            cout << 'N';
        } else if (n%3200 == 0) {
            cout << 'N';
        } else {
            cout << 'Y';
        }
    } else {
        cout << 'N';
    }
    return 0;
}