#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int array[n];

    for (int i=0; i<n; i++) {
            cin >> array[i];
    }

    for (int j=0; j<m; j++) {
        int *p, tmp;
        p = array;
        tmp = *(p+n-1);
        for (int i=n-2; i>=0; i--) {
            *(p+i+1) = *(p+i);
        }
        *p = tmp;
    }

    for (int j=0; j<n; j++) {
        cout << array[j] << " ";
    }

    return 0;
}