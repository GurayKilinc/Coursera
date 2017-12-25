#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main() {
    int p,d,t,h;
    for(p=1;p<=4;p++) {
        for(d=1;d<=4;d++) {
            for(t=1;t<=4;t++) {
                for(h=1;h<=4;h++) {
                    if( (p!=d && p!=t && p!=h && d!=h && d!=h && t!=h) //每个湖的排名各不相同
                        &&(((d==1)+(h==4)+(p==3))==1)      //4个每人仅答对一个
                        &&(((h==1)+(d==4)+(p==2)+(t==3))==1)
                        &&(((h==4)+(d==3))==1)
                        &&(((p==1)+(t==4)+(h==2)+(d==3))==1)
                        &&((p+d+t+h)==10) ) {
                        cout << p << endl;
                        cout << d << endl;
                        cout << t << endl;
                        cout << h << endl;
                        return 0;
                    }

                }
            }
        }
    }  //穷举各种情况
    return 0;
}