#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a1[n], a2[n];
    for (int i = 0; i < n; i++) {
        cin >> a1[i];
        a2[n-1-i] = a1[i];
    }
    for (int i = 0; i < n; i++) {
        cout << a2[i] << " ";
    }
    return 0;
}