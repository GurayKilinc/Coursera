#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int num, maxodd = 1, mineven = 100;
    int odd[6] = {1, 1, 1, 1, 1, 1};
    int even[6] = {100, 100, 100, 100, 100, 100};
    for (int i = 0; i < 6; i++) {
        cin >> num;
        if (num % 2 == 0) {
            even[i] = num;
        } else {
            odd[i] = num;
        }
    }

    for (int i = 0; i < 6; i++) {
        if (maxodd < odd[i]) {
            maxodd = odd[i];
        }
    }
    for (int i = 0; i < 6; i++) {
        if (mineven > even[i]) {
            mineven = even[i];
        }
    }

    if (maxodd > mineven) {
        cout << maxodd - mineven << endl;
    } else {
        cout << mineven - maxodd << endl;
    }

}