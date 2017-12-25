#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    while (true) {
        int n;
        cin >> n;
        if (n==0) {
            break;
        } else {
            int array[n], med, med1, med2;
            for (int i=0; i<n; i++) {
                cin >> array[i];
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n-1-i; j++) {
                    if (array[j] > array[j+1]) {
                        int tmp;
                        tmp = array[j];
                        array[j] = array[j+1];
                        array[j+1] = tmp;
                    }
                }
            }
            if (n%2 != 0) {
                med = array[(n+1)/2 - 1];
            } else {
                med1 = array[n/2 - 1];
                med2 = array[n/2];
                med = (med1 + med2)/2;
            }
            cout << med << endl;
        }
    }

    return 0;
}