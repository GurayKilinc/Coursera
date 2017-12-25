#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n / 100 > 0) {
        cout << n / 100 << endl;
        n = n % 100;
    }
    if (n / 10 > 0) {
        cout << n / 10 << endl;
        n = n % 10;
    }
    cout << n << endl;
}