#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

void flu(char str[102][102], int d, int s, int stop) {
    for (int i=1; i<=100; i++) {
        for (int j=1; j<=100; j++) {
            if (str[i][j] == '@') {
                if (str[i][j-1] == '.') {
                    str[i][j-1] = '+';
                }
                if (str[i][j+1] == '.') {
                    str[i][j+1] = '+';
                }
                if (str[i-1][j] == '.') {
                    str[i-1][j] = '+';
                }
                if (str[i+1][j] == '.') {
                    str[i+1][j] = '+';
                }
            }
        }
    }
    d++;
    for (int i=1; i<=100; i++) {
        for (int j=1; j<=100; j++) {
            if (str[i][j] == '+') {
                str[i][j] = '@';
                s++;
            }
        }
    }
    if (d == stop) {
        cout << s << endl;
    } else {
        return flu(str, d, s, stop);
    }
}

int main() {
    int n = 0, sum = 0, day = 1, stopday;
    cin >> n;
    char a[102][102];
    for (int i=0; i<n+2; i++) {
        for (int j=0; i<n+2; i++) {
            a[i][j] = '#';
        }
    }

    for (int i=1; i<=n; i++) {
        char temp[n+1];
        cin >> temp;
        for (int j=1; j<=n; j++) {
            a[i][j] = temp[j-1];
        }
    }

    cin >> stopday;

    for (int i=1; i<=100; i++) {
        for (int j=1; j<=100; j++) {
            if (a[i][j] == '@') {
                sum++;
            }
        }
    }

    if (stopday == 1) {
        cout << sum << endl;
    } else {
        flu(a, day, sum, stopday);
    }

    return 0;
}
