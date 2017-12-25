int operator * (Number &n)
    {
        return this->num * n.num;
    }
    //重载类型转换方程，不能能有返回值
    operator int()
    {
        return num;
    }