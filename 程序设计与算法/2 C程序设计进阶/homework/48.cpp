#include <iostream>
using namespace std;

int game(char str[], int n[], char x, char y) {
    for (int i = 0; i < 100; i++) {
        if (str[i] == x && str[i+1] == y) {
            cout << n[i] << ' ' << n[i+1] << endl;
            for (int j=i; j < 100; j++) {
                str[j] = str[j+2];
                n[j] = n[j+2];
            }
            return game(str, n, x, y);
        }
    }
    return 0;
}

int main() {
    char m, f;
    char ch[102];
    int num[102];
    cin.getline(ch, 102);
    m = ch[0];
    for (int i = 0; i < 102; i++) {
        if (ch[i] != m) {
            f = ch[i];
            break;
        }
    }
    for (int i = 0; i < 102; i++) {
        num[i] = i;
    }
    game(ch, num, m, f);

    return 0;
}