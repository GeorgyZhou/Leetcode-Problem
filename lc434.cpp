class Solution {
public:
    int countSegments(string s) {
        stringstream ss;
        ss << s;
        string op;
        int cnt = 0;
        while (ss >> op) {
            cnt += 1;
        }
        return cnt;
    }
};