#include <iostream>
#include <string>
#include <cstdio>
#include <iomanip>
#include <math.h>
using namespace std;

class Student {
private:
    char name[100], id[100];
    int age, avg1, avg2, avg3, avg4, avg;
public:
    void init(char _name[], char _id[], int _age, int _avg1, int _avg2, int _avg3, int _avg4){
        strcpy(name, _name);
        strcpy(id, _id);
        age = _age;
        avg1 = _avg1;
        avg2 = _avg2;
        avg3 = _avg3;
        avg4 = _avg4;
    }
    int getAvg() {
        avg = (avg1 + avg2 + avg3 + avg4)/4;
        return avg;
    }
    int getAge() {
        return age;
    }
    char * getName() {
        return name;
    }
    char * getId() {
        return id;
    }
};

int main() {
    char name[100], id[100], a;
    int age, avg1, avg2, avg3, avg4;
    cin.getline(name, 100, ',');
    cin >> age;
    a = getchar();
    cin.getline(id, 100, ',');
    cin >> avg1 >> a >> avg2 >> a >> avg3 >> a >> avg4;
    Student s;
    s.init(name, id, age, avg1, avg2, avg3, avg4);
    cout << s.getName() << ',' << s.getAge() << ',' << s.getId() << ',' << s.getAvg();
    
    return 0;
}

