#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n, z1, z2, z3, z4, z5, z6;
    cin >> n;
    z1 = n/ 100;
    n = n % 100;
    z2 = n/ 50;
    n = n % 50;
    z3 = n/ 20;
    n = n % 20;
    z4 = n/ 10;
    n = n % 10;
    z5 = n/ 5;
    n = n % 5;
    z6 = n;
    cout << z1 << endl;
    cout << z2 << endl;
    cout << z3 << endl;
    cout << z4 << endl;
    cout << z5 << endl;
    cout << z6 << endl;
}