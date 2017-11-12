class Solution {
public:
    vector<vector<string>> partition(string s) {
        if (s.size() == 0) return {{}};
        if (s.size() == 1) return {{s}};
        vector<vector<string>> res;
        for (int i = s.size() - 1; i >= 0; i--) {
            string cur = s.substr(i, s.size() - i);
            if (!isPalindrome(cur)) continue;
            for (vector<string>& part : partition(s.substr(0, i))) {
                part.push_back(cur);
                res.push_back(part);
            }
        }
        return res;
    }
private:
    bool isPalindrome(string s) {
        int left = 0, right = s.size()-1;
        while (left < right) {
            if (s[left++] != s[right--]) return false;
        }
        return true;
    }
};