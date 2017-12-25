#include <iostream>
using namespace std;

void clean(char str[], int n[]) {
    for (int i = 0; i < 100; i++) {
        if (str[i] == '\0') {
            break;
        } else if (str[i] == '(') {
            continue;
        } else if (str[i] == ')') {
            continue;
        } else {
            for (int j=i; j < 100; j++) {
                str[j] = str[j+1];
                n[j] = n[j+1];
            }
            clean(str, n);
        }
    }
}

void mark(char str[], int n[]) {
    for (int i = 0; i < 100; i++) {
        if (str[i] == '(' && str[i+1] == ')') {

            for (int j=i; j < 100; j++) {
                str[j] = str[j+2];
                n[j] = n[j+2];
            }
            return mark(str, n);
        }
    }
}

int main() {
    char ch[102] = {'\0'};
    char mk[102] = {'\0'};
    int num[102];
    int sum = 0;
    int count = 0;
    char out[100] = {'\0'};

    cin.getline(ch, 102);
    cout << ch << endl;

    for (int i = 0; i < 100; i++) {
        if (ch[i] == '(') {
            mk[i] = '$';
        } else if (ch[i] == ')') {
            mk[i] = '?';
        } else if (ch[i] == '\0') {
            mk[i] = '\0';
        } else {
            mk[i] = ' ';
        }
    }
    for (int i = 0; i < 102; i++) {
        num[i] = 200;
    }
    for (int i = 0; i < 100; i++) {
        if (ch[i] != '\0') {
            num[i] = i;
            out[i] = ' ';
            count++;
        }
    }

    clean(ch, num);
    mark(ch, num);

    for (int i = 0; i < 100; i++) {
        if (num[i] != 200) {
            sum++;
        }
    }

    if (sum == 0) {
        for (int i = 0; i < 100; i++) {
            out[i] = '\0';
        }
    } else {
        for (int i = 0; i < sum; i++) {
            out[num[i]] = mk[num[i]];
        }
        if (num[sum-1] < count) {
            for (int i = num[sum-1]+1; i < 100; i++) {
                out[i] = '\0';
            }
        }
    }

    cout << out;

    return 0;
}