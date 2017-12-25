#include <iostream>
using namespace std;

int main() {
    char ch[80];
    cin.getline(ch, 80);
    int c1 = 0, c2 = 0, c3 = 0, c4 = 0, c5 = 0;

    for (int i = 0; ch[i] != '\0'; i++) {
        if (ch[i] == 'a') {
            c1++;
        } else if (ch[i] == 'e') {
            c2++;
        } else if (ch[i] == 'i') {
            c3++;
        } else if (ch[i] == 'o') {
            c4++;
        } else if (ch[i] == 'u') {
            c5++;
        }
    }

    cout << c1 << " " << c2 << " " << c3 << " " << c4 << " " << c5;
    return 0;
}