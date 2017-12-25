#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int newplus(int a, int b) {
    int out;
    out  = a + b;
    return out;
}

int newsub(int a, int b) {
    int out;
    out  = a - b;
    return out;
}

int newmulti(int a, int b) {
    int out;
    out  = a * b;
    return out;
}

int newdiv(int a, int b) {
    int out;
    out  = a / b;
    return out;
}

int main() {
    int x1, x2;
    char n;
    cin >> x1 >> x2 >> n;

    if (n == '+') {
        cout << newplus(x1, x2) << endl;
    } else if (n == '-') {
        cout << newsub(x1, x2) << endl;
    } else if (n == '*') {
        cout << newmulti(x1, x2) << endl;
    } else if (n == '/') {
        if (x2 == 0) {
            cout << "Divided by zero!" << endl;
        } else {
            cout << newdiv(x1, x2) << endl;
        }
    } else {
        cout << "Invalid operator!" << endl;
    }
    return 0;
}