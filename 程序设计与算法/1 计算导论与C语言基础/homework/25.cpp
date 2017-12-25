#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n, k, outcome = 0;
    cin >> n >> k;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            if (a[i] + a[j] == k) {
                outcome++;
            }
        }
    }
    if (outcome == 0) {
        cout << "no" << endl;
    } else {
        cout << "yes" << endl;
    }
}