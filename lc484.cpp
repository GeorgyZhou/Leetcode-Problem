class Solution {
public:
    vector<int> findPermutation(string s) {
        if (s.size() == 0) return {1};
        vector<int> perm;
        for (int i = 0; i <= s.size(); i++)
            perm.push_back(i+1);
        int first = 0, second = 1, left, right;
        for (char& c : s) {
            if (c == 'D') {
                second++;
                continue;
            }
            reverse(perm.begin() + first, perm.begin() + second);
            first = second;
            second++;
        }
        if (second - first != 1) reverse(perm.begin() + first, perm.begin() + second);
        return perm;
    }
};