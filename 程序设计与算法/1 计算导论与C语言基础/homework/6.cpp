#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n, c1 = 0, c5 = 0, c10 = 0;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        if (a[i] == 1) {
            c1++;
        } else if (a[i] == 5) {
            c5++;
        } else if (a[i] == 10) {
            c10++;
        }
    }
    cout << c1 << endl;
    cout << c5 << endl;
    cout << c10 << endl;
    return 0;
}