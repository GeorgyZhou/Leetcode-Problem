class Solution {
public:
    bool checkValidString(string s) {
        int len = s.size();
        int lo = 0, hi = 0;
        for (int i = 0; i < len; i++) {
            lo += s[i] == '(' ? 1 : -1;
            hi += s[i] != ')' ? 1 : -1;
            if (hi < 0) break;
            lo = max(lo, 0);
        }
        return lo == 0;
    }
};