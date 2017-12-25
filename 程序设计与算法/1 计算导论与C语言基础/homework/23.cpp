#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int dis;
        cin >> dis;
        if (dis < 100) {
            cout << "Walk" << endl;
        } else if (dis > 100) {
            cout << "Bike" << endl;
        } else {
            cout << "All" << endl;
        }
    }
}