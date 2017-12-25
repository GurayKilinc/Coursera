#include <iostream>
#include <iomanip>
using namespace std;

bool arrayChange(int a[5][5], int b, int c) {
    if ((b>=0 && b<5) && (c>=0 && c <5)) {
        int tmp[5][5];
        for (int i = 0; i < 5; i++) {
            tmp[b][i] = a[b][i];
            a[b][i] = a[c][i];
            a[c][i] = tmp[b][i];
        }
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int n, m;
    int array[5][5];
    for (int i=0; i<5; i++) {
        for (int j=0; j<5; j++) {
            cin >> array[i][j];
        }
    }
    cin >> n >> m;
    if (arrayChange(array, n, m)) {
        for (int i=0; i<5; i++) {
            for (int j=0; j<5; j++) {
                cout << setw(4) << array[i][j];
            }
            cout << endl;
        }
    } else {
        cout << "error" << endl;
    }
    return 0;
}