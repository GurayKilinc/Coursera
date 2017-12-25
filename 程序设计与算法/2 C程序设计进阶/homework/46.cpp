#include <iostream>
using namespace std;

int main() {
    char input[500], *x = NULL, *y = NULL;
    cin.getline(input, 500);
    for(x = input; x < input + 500; x++) {
        if(*x == '\0') {
            break;
        } else if(*x == ' ') {
            continue;
        } else {
            y = x;
            int count = 0;
            while(*y != ' ' && *y != '\0') {
                y++;
            }
            y--;
            for(;x<y; x++, y--) {
                char tmp;
                tmp = *x;
                *x = *y;
                *y = tmp;
                count++;
            }
            x = x + count;

        }
    }

    cout << input << endl;

    return 0;
}