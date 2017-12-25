#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, sum = 0;
    cin >> n;
    int array[n][n];

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> array[i][j];
        }
    }

    for (int i=1; i<n-1; i++) {
        for (int j=1; j<n-1; j++) {
            if (array[i][j]+50 <= array[i-1][j] && array[i][j]+50 <= array[i+1][j] && array[i][j]+50 <= array[i][j-1] && array[i][j]+50 <= array[i][j+1]) {
                sum += 1;
            }
        }
    }

    cout << sum;

    return 0;
}