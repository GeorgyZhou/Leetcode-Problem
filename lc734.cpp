class Solution {
public:
    bool areSentencesSimilar(vector<string>& words1, vector<string>& words2, vector<pair<string, string>> pairs) {
        unordered_map<string, unordered_set<string>> sim;
        int m = words1.size(), n = words2.size();
        if (m != n) return false;
        for (auto& p : pairs) {
            sim[p.first].insert(p.second);
            sim[p.second].insert(p.first);
        }
        for (int i = 0; i < m; ++i) {
            if (words1[i] != words2[i] && sim[words1[i]].find(words2[i]) == sim[words1[i]].end()) return false;
        }
        return true;
    }
};