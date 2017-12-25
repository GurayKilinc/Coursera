#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n, sum = 0;
    cin >> n;

    for (int i = 0; i < 5; i++) {
        int num;
        cin >> num;
        if (num < n) {
            sum += num;
        }
    }
    cout << sum << endl;
}