class Solution {
public:
    string solveEquation(string equation) {
        int n = equation.length();
        int index = equation.find('=');
        auto left = getCoe(equation.substr(0, index));
        auto right = getCoe(equation.substr(index + 1, n - index - 1));
        int xCoe = left[0] - right[0];
        int constCoe = right[1] - left[1];
        if (xCoe == 0 && constCoe != 0) return "No solution";
        if (xCoe == 0 && constCoe == 0) return "Infinite solutions";
        return "x=" + to_string(constCoe/xCoe);
    }
private:
    vector<int> getCoe(string s) {
        stack<int> st;
        int xCoe = 0, constCoe = 0;
        bool isAdd = true;
        bool isX = false;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '-' || s[i] == '+') {
                int coe = 0, factor = 1;
                while (!st.empty()) {
                    coe += st.top() * factor;
                    st.pop();
                    factor *= 10;
                }
                if (isX) {
                    xCoe = isAdd ? xCoe + coe : xCoe - coe;
                    isX = false;
                } else {
                    constCoe = isAdd ? constCoe + coe : constCoe - coe;
                }
                isAdd = (s[i] == '+');
            } else if (s[i] == 'x') {
                if (st.empty()) st.push(1);
                isX = true;
            } else {
                st.push(s[i] - '0');
            }
        }
        int coe = 0, factor = 1;
        while (!st.empty()) {
            coe += st.top() * factor;
            st.pop();
            factor *= 10;
        }
        if (isX) {
            xCoe = isAdd ? xCoe + coe : xCoe - coe;
        } else {
            constCoe = isAdd ? constCoe + coe : constCoe - coe;
        }
        return {xCoe, constCoe};
    }
};