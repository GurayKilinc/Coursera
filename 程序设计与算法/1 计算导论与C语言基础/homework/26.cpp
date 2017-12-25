#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n, a[90];
    cin >> n;

    for (int i = 0; i < 90; i++) {

        int n1, n2;
        n1 = (i+10) / 10;
        n2 = (i+10) % 10;
        if ((i+10) % (n1 + n2) == 0) {
            a[i] = i+10;
        } else {
            a[i] = 100;
        }
    }

    for (int i = 0; i < 90; i++) {
        if (a[i] < n) {
            cout << a[i] << endl;
        }
    }
}