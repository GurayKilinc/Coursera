#include <string>
class MyString: public string {
public:
    MyString (): string () {}
    MyString (const char *s): string (s) {}
    MyString (const string &s): string (s) {}

    MyString operator() (int _x, int _y) {
        return string::substr(_x, _y);
    }
};