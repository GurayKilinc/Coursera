#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n, c1 = 0, c2 = 0, c3 = 0, c4 = 0;
    double p1, p2, p3, p4;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        if (num < 19) {
            c1++;
        } else if (num > 18 && num < 36) {
            c2++;
        } else if (num > 35 && num < 61) {
            c3++;
        } else {
            c4++;
        }
    }
    p1 = (double)c1 / n * 100;
    p2 = (double)c2 / n * 100;
    p3 = (double)c3 / n * 100;
    p4 = (double)c4 / n * 100;
    cout << setiosflags(ios::fixed) << setprecision(2) << "1-18: " << p1 << "%" << endl;
    cout << "19-35: " << p2 << "%" << endl;
    cout << "36-60: " << p3 << "%" << endl;
    cout << "60-: " << p4 << "%" << endl;
}