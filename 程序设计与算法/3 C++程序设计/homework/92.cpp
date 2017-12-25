class MyString : public string
{
public:
    MyString():string() {/*cout << "!";*/};
    MyString(const string &str):string(str) {/*cout << "@";*/}; //类型转换构造函数
    MyString(const char* str):string(str) {/*cout << "#";*/};//char*是数据类型，而string是类，要弄清楚。
    MyString(MyString& myStr):string(myStr) {/*cout << "$";*/};//复制构造函数
    /*
    我们发现在派生类的拷贝构造函数中的初始化列表中，基类拷贝构造函数的参数是派生类，但是
    这样子是没有关系的，编译系统会自动将派生类缩减成基类规模（这是我的个人理解，进行缩减的
    只是派生类的临时对象，不会对参数进行修改），然后传入给基类的拷贝构造函数，然后在派生类
    的拷贝构造函数当中再将派生类比基类多出的成员变量进行拷贝。
    */
    MyString operator()(int start, int length)
    {
//      cout << "%";
        return this->substr(start, length);
    };
};