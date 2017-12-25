#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int tree[n+1];

    for (int i=0; i<n+1; i++) {
        tree[i] = 1;
    }

    for (int i=0; i<m; i++) {
        int x, y;
        cin >> x >> y;
        for (int a=x; a<y+1; a++) {
            tree[a] = 0;
        }
    }

    int sum = 0;
    for (int i=0; i<n+1; i++) {
        if (tree[i] == 1) {
            sum++;
        }
    }

    cout << sum << endl;

    return 0;
}