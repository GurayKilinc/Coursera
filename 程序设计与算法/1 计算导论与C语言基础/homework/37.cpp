#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    double dots[n][2], dis[6][5], max = 0;
    for (int i=0; i<n; i++) {
        cin >> dots[i][0] >> dots[i][1];
    }

    for (int i=0; i<n; i++) {
        for (int j=i+1; j<n; j++) {
            dis[i][j-1] = sqrt( pow(dots[i][0]-dots[j][0], 2) + pow(dots[i][1]-dots[j][1], 2) );
        }
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n-1; j++) {
            if (max < dis[i][j]) {
                max = dis[i][j];
            }
        }
    }

    cout << fixed << setprecision(4) << max << endl;

    return 0;
}