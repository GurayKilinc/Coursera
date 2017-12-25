#include <iostream>
using namespace std;

int main() {
    int m, k, count=0;
        cin >> m >> k;
        bool right1 = false, right2 = false;
        if (m % 19 == 0) {
            right1 = true;
        }
        while (m > 0) {
            if (m % 10 == 3) {
                count++;
            }
            m /= 10;
        }
        if (count == k) {
            right2 = true;
        }
        if (right1 && right2) {
            cout << "YES";
        } else {
            cout << "NO";
        }
        return 0;
}