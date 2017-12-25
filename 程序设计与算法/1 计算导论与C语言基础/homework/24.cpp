#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int k;
    double n;
    cin >> n >> k;
    double price = 200.00, money = n;
    if (n >= 200) {
        cout << 1 << endl;
    } else {
        for (int i = 2; i < 21; i++) {
            money = n * i;
            price = price + price * ((double)k/100);
            if (money >= price) {
                cout << i << endl;
                break;
            }
        }
        if (money < price) {
            cout << "Impossible" << endl;
        }
    }
}