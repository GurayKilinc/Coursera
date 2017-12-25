#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int num;
    cin >> num;
    cout << hex << num << endl;
    cout.fill('0');
    cout << dec << setw(10) << num << endl;
    return 0;
}