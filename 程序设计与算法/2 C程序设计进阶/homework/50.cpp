#include <iostream>
#include <cstring>
#include <iomanip>
#include <math.h>
using namespace std;

char clear(char str[81]) {
    for (int i=0; i<81; i++) {
        str[i] = '\0';
    }
    return str[81];
}

int main() {
    int n, count = 0;
    cin >> n;
    char str[41] = {'\0'}, space[2] = {' ', '\0'}, text[81] = {'\0'};

    for (int i=0; i<n-1; i++) {
        cin >> str;
        count += strlen(str) + 1;
        if (count < 81) {
            strcat(text, str);
            strcat(text, space);
            continue;
        } else if (count == 81) {
            strcat(text, str);
            cout << text << endl;
            clear(text);
            count = 0;
        } else {
            for (int i=79; i>=0; i--) {
                if (text[i] == ' ') {
                    text[i] = '\0';
                    break;
                }
            }
            cout << text << endl;
            clear(text);
            count = 0;
            strcat(text, str);
            strcat(text, space);
            count = strlen(str) + 1;
        }
    }

    cin >> str;
    count += strlen(str) + 1;
    if (count <= 81) {
        strcat(text, str);
        cout << text;
    } else {
        cout << text << endl;
        cout << str;
    }

    return 0;
}
