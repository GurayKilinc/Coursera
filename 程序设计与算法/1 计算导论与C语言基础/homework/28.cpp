#include <iostream>
using namespace std;

int main() {
    bool state = 1;
    char ch1[80], ch2[80];
    cin.getline(ch1, 80);
    cin.getline(ch2, 80);

    for (int i = 0; ch1[i] != '\0'; i++) {
        if (ch1[i] < 97) {
            ch1[i] += 32;
        }
    }
    for (int i = 0; ch2[i] != '\0'; i++) {
        if (ch2[i] < 97) {
            ch2[i] += 32;
        }
    }

    for (int i = 0; ch1[i] != '\0'; i++) {
        if (ch1[i] == ch2[i]) {
            continue;
        } else if (ch1[i] > ch2[i]) {
            state = 0;
            cout << ">" << endl;
            break;
        } else {
            state = 0;
            cout << "<" << endl;
            break;
        }
    }
    if (state) {
        cout << "=" << endl;
    }

    return 0;
}