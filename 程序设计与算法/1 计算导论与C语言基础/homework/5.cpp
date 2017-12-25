#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int m, n, x, sum;
    sum = 0;
    cin >> m >> n;
    if (m % 2 == 0) {
        m += 1;
    }
    x = round((n - m)/2);
    for (int i = 0; i < x + 1; i++) {
        if (m > n) {
            sum = 0;
            break;
        }
        sum += m + i * 2;
    }
    cout << sum;
    return 0;
}