Complex & operator = (const string s) {
        int position = s.find("+", 0);
        string firstpart = s.substr(0, position);
        string secondpart = s.substr(position+1, s.length()-position-2);
        r = atof(firstpart.c_str());
        i = atof(secondpart.c_str());
        return * this;
    }