#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x, ans = 0;
        cin >> x;
        while (x > 0) {
            if (x % 2 != 0) {
                ans++;
                x /= 2;
            } else {
                x /= 2;
            }
        }
        cout << ans << endl;
    }
    return 0;
}