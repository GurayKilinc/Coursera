#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main() {
    int id;
    char type;
    float money, money1 = 0.00, money2 = 0.00, money3 = 0.00, moneyA = 0.00, moneyB = 0.00, moneyC = 0.00;

    for (int i=1; i<=3; i++) {
        int n;
        cin >> id >> n;
        for (int j=1; j<=n; j++) {
            cin >> type >> money;
            if (id ==1) {
                money1 += money;
                if (type == 'A') {
                    moneyA += money;
                } else if (type == 'B') {
                    moneyB += money;
                } else if (type == 'C') {
                    moneyC += money;
                }

            } else if (id ==2) {
                money2 += money;
                if (type == 'A') {
                    moneyA += money;
                } else if (type == 'B') {
                    moneyB += money;
                } else if (type == 'C') {
                    moneyC += money;
                }
            } else if (id ==3) {
                money3 += money;
                if (type == 'A') {
                    moneyA += money;
                } else if (type == 'B') {
                    moneyB += money;
                } else if (type == 'C') {
                    moneyC += money;
                }
            }

        }
    }
    cout << fixed << setprecision(2) << 1 << ' ' << money1 << endl;
    cout << 2 << ' ' << money2 << endl;
    cout << 3 << ' ' << money3 << endl;
    cout << 'A' << ' ' << moneyA << endl;
    cout << 'B' << ' ' << moneyB << endl;
    cout << 'C' << ' ' << moneyC << endl;
    return 0;
}