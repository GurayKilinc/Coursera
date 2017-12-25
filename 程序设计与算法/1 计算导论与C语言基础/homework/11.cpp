#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    const double pi = 3.14159;
    const int drink = 20000;
    int h, r, n;
    double barrel;
    cin >> h >> r;
    barrel = pi * r * r * h;
    n = drink / barrel + 1;
    cout << n << endl;
}