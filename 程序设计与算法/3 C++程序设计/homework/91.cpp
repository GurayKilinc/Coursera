class CMy_add
{
private:
    int& sum;
public:
    CMy_add(int& n):sum(n) {}
    void operator() (int x)
    {
        x %= 8;//得到其低3位
        sum += x;
    }
};