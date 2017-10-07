class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int cnt[26] = {0}, subCnt[26] = {0};
        if (s2.size() < s1.size()) return false;
        for (char& c : s1) {
            cnt[c - 'a']++;
        }
        int k = s1.size();
        for (int i = 0; i < k; i++)
            subCnt[s2[i] - 'a']++;
        if (isEqual(cnt, subCnt)) return true;
        for (int i = k; i < s2.size(); i++) {
            subCnt[s2[i] - 'a']++;
            subCnt[s2[i-k] - 'a']--;
            if(isEqual(cnt, subCnt)) return true;
        }
        return false;
    }
private:
    bool isEqual(const int cnt1[26], const int cnt2[26]) {
        for (int i = 0; i < 26; i++) {
            if (cnt1[i] != cnt2[i]) return false;
        }
        return true;
    }
};