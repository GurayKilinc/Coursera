#include <iostream>
using namespace std;

int main() {
    char ch1[500];
    cin.getline(ch1, 500, '.');

    int index = 0, length = 0, maxLength = 0;

    for (int i = 0; ch1[i] != '\0'; i++) {
        if (ch1[i] == ' ') {
            length = 0;
        } else {
            length++;
            if (maxLength < length) {
                maxLength = length;
            }
        }
    }

    length = 0;
    for (int i = 0; ch1[i] != '\0'; i++) {
        index++;
        if (ch1[i] == ' ') {
            length = 0;
        } else {
            length++;
            if (length == maxLength) {
                break;
            }
        }
    }
    for (int i = index - maxLength; i < index; i++) {
        cout << ch1[i];
    }

    return 0;
}