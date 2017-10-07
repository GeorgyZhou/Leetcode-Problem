class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        if (s.size() < p.size()) return {};
        vector<int> ret;
        int mask[26] = {0};
        for (char& c : p) {
            mask[c - 'a'] += 1; 
        }
        int cur[26] = {0};
        for (int i = 0; i < p.size(); i++) 
            cur[s[i] - 'a'] += 1;
        if (check(cur, mask)) ret.push_back(0);
        for (int i = 1; i <= s.size() - p.size(); i++) {
            cur[s[i-1] - 'a'] -= 1;
            cur[s[i+p.size()-1] - 'a'] += 1;
            if (check(cur, mask)) ret.push_back(i);
        }
        return ret;
    }
private:
    bool check(int cur[26], int mask[26]) {
        for (int i = 0; i < 26; i++) {
            if (cur[i] != mask[i]) return false;
        }
        return true;
    }
};