#include <iostream>
#include <cstring>
#include <iomanip>
#include <math.h>
using namespace std;

int main() {
    int num, m, n, sum1 = 0, sum2 = 0;
    cin >> num;

    for (int i=0; i<num; i++) {
        cin >> m >> n;
        int arr[m][n];
        for (int x=0; x<m; x++) {
            for (int y=0; y<n; y++) {
                cin >> arr[x][y];
                sum1 += arr[x][y];
            }
        }
        for (int x=1; x<m-1; x++) {
            for (int y=1; y<n-1; y++) {
                sum2 += arr[x][y];
            }
        }
        cout << sum1 - sum2 << endl;
        sum1 = 0;
        sum2 = 0;
    }

    return 0;
}
