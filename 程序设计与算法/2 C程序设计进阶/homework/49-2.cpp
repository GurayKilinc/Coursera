#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

void clean(char str[101]) {
    for (int i=0; i<100; i++) {
        for (int j=i+1; j<100; j++) {
            if (str[i] == 40 && str[j] == 41) {
                if (j == i+1) {
                    str[i] = 32;
                    str[j] = 32;
                    clean(str);
                } else {
                    int mark = 0;
                    for (int x=i+1; x<j; x++) {
                        if (str[x] != ' ') {
                            mark++;
                        }
                    }
                    if (mark == 0) {
                        str[i] = 32;
                        str[j] = 32;
                        clean(str);
                    }
                }
            }
        }
    }
}

int main() {
    char input[101] = {'\0'};
    cin.getline(input, 101);

    for (int i=0; i<100; i++) {
        if (input[i]!=40 && input[i]!=41) {
            input[i] = 32;
        }
    }

    clean(input);
    for (int i=0; i<100; i++) {
        if (input[i]==40) {
            input[i] = '$';
        } else if (input[i]==41) {
            input[i] = '?';
        }
    }
    for (int i=99; i>=0; i--) {
        if (input[i]==32) {
            input[i] = '\0';
        } else {
            break;
        }
    }

    for (int i=0; i<101; i++) {
        cout << input[i];
    }

    return 0;
}
