#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main() {
    char str[11] = {'\0'}, substr[4], out[14], max = 0;
    int n = 0;
    cin >> str >> substr;

    for (int i=0; i<10; i++) {
        if (max < str[i]) {
            max = str[i];
            n = i;
        }
    }

    for (int i=0; i<n+1; i++) {
        out[i] = str[i];
    }
    for (int i=n+1; i<n+4; i++) {
        out[i] = substr[i-n-1];
    }
    for (int i=n+4; i<13; i++) {
        out[i] = str[i-3];
    }
    out[13] = '\0';

    cout << out << endl;

    return 0;
}
