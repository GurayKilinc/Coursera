#include <iostream>
#include <string>
using namespace std;

class Warrior {
    static int countR = 0, countB = 0, total = 0;
    string type;
public:
    Warrior(char t, int l, int c) {
        total++;
        switch (t) {
            case 'd':
                type = "dragon";
                break;
            case 'n':
                type = "ninja";
                break;
            case 'i':
                type = "iceman";
                break;
            case 'l':
                type = "lion";
                break;
            case 'w':
                type = "wolf";
                break;
        }
        if (c == 0) {
            countR++;
            cout << "red " << type << " " << total << " born with strength " << l << "," << countR << " dragon in red headquarter" << endl;
        } else {
            countB++;
            cout << "blue" << type << " " << total << " born with strength " << l << "," << countB << " dragon in blue headquarter" << endl;
        }
    }
};

string countTime(int t) {
    t++;
    if (t<10) {
        return "00"+to_string(t);
    } else if (t<100) {
        return "0"+to_string(t);
    } else {
        return to_string(t);
    }
}

int main() {
    int n, baseLife1, baseLife2, dLife, nLife, iLife, lLife, wLife, color, time = 0;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> baseLife1 >> dLife >> nLife >> iLife >> lLife >> wLife;
        baseLife2 = baseLife1;
        cout << "Case:" << n << endl;
        while (baseLife1 > 0 || baseLife2 > 0) {
            Warrior('i', iLife, 0);
            Warrior('l', lLife, 1);

            Warrior('l', lLife, 0);
            Warrior('d', dLife, 1);

            Warrior('w', wLife, 0);
            Warrior('n', nLife, 1);

            Warrior('n', nLife, 0);
            Warrior('i', iLife, 1);

            Warrior('d', dLife, 0);
            Warrior('w', wLife, 1);
        }
    }



    return 0;
}
