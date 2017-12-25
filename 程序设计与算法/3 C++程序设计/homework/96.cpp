class A
{
public:
    static int count;
    A() {count++;}
    A(int a) {count++;}
    virtual ~A()
    {
        cout << "A::destructor" << endl;
    }
    /*
    使用了delete释放某个重载了delete的类的对象空间时，先调用类的析构函数，
    然后再调用重载的delete函数。
    */
    void operator delete(void* a)//重载delete
    {
        count--;
    }
};
class B: public A
{
public:
    B():A() {}
    B(int b):A() {}
    B& operator = (B& b)
    {
        return b;
    }
    virtual ~B()
    {
        cout << "B::destructor" << endl;
    }
};