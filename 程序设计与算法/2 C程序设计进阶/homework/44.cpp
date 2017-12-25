#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    int num[n], q1[n], q2[n], mark = 0, c1 = 0, c2 = 0;
    double rep[n];
    for (int i = 0; i < n; i++) {
        cin >> num[i];
        cin >> q1[i];
        cin >> q2[i];
        rep[i] = (double)q2[i] / q1[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n-1-i; j++) {
            int tmp1, tmp2;
            if (rep[j] > rep[j+1]) {
                tmp1 = rep[j];
                rep[j] = rep[j+1];
                rep[j+1] = tmp1;
                tmp2 = num[j];
                num[j] = num[j+1];
                num[j+1] = tmp2;
            }
        }
    }

    int diff = 0, maxdiff = 0;
    for (int i = 0; i < n-1; i++) {
        diff = rep[i+1] - rep[i];
        if (maxdiff < diff) {
            maxdiff = diff;
            mark = i;
            c1 = i+1;
            c2 = n-i-1;
        }
    }

    cout << c2 << endl;
    for (int i = c1; i < n; i++) {
        cout << num[i] << endl;
    }
    cout << c1 << endl;
    for (int i = 0; i < c1; i++) {
        cout << num[i] << endl;
    }

    return 0;
}