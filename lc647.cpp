class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        if (n == 0) return 0;
        vector<char> vec;
        int cnt = n, curCnt;
        for (int i = 0; i < n; i++) {
            vec.push_back(s[i]);
            vec.push_back('#');
        }
        vec.pop_back();
        for (int i = 0, j; i < vec.size(); i++) {
            j =  (i % 2 == 0 ? 2 : 1);
            curCnt = 0;
            for (; i + j < vec.size() && i - j >= 0; j += 2, curCnt++) {
                if (vec[i - j] != vec[i + j]) break;
            }
            cnt += curCnt;
        }
        return cnt;
    }
};