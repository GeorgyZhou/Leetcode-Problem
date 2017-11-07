class Solution {
public:
    int calculate(string s) {
        int num = 0, res = 0;
        vector<int> st;
        char sign = '+';
        for (int i = 0; i < s.size(); i++) {
            if ('0' <= s[i] && '9' >= s[i]) num = num * 10 + s[i] - '0';
            if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' || i == s.size() - 1) {
                if (sign == '+') {
                    st.push_back(num);
                } else if (sign == '-') {
                    st.push_back(-num);
                } else if (sign == '*') {
                    int back = st[st.size() - 1];
                    st.pop_back();
                    st.push_back(num * back);
                } else if (sign == '/') {
                    int back = st[st.size() - 1];
                    st.pop_back();
                    st.push_back(back / num);
                }
                num = 0;
                sign = s[i];
            }
        }
        for (int& num : st) {
            res += num;
        }
        return res;
    }
};