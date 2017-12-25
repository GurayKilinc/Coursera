bool operator < (const A& a1, const A& a2)
{
    return a1.get_size() < a2.get_size();
}

template <class Iterator, class Function>//函数模板
void Show(Iterator begin, Iterator end, Function print)
{
    for (Iterator iterator1 = begin; iterator1 != end; iterator1++)
    {
        print(*iterator1);
    }
}

class Print //函数对象类
{
public:
    void operator() (const A& a)
    {
        cout << a.get_name() << " ";
    }
};

template <class A>  //函数对象类模板
struct MyLarge
{
    inline bool operator() (const A& a1, const A& a2)
    {
        return a1.get_name() < a2.get_name();
    }
};
