#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main() {
    int n, x[100] = {0}, count = 0;
    cin >> n;
    for (int i=0; i < n; i++) {
        cin >> x[i];
    }

    for (int i=0; i < n; i++) {
        if (x[i] == i) {
            count++;
            cout << i;
            break;
        }
    }
    if (count == 0) {
        cout << "N";
    }

    return 0;
}