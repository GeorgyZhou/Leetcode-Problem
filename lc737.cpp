class Solution {
public:
    bool areSentencesSimilarTwo(vector<string>& words1, vector<string>& words2, vector<pair<string, string>> pairs) {
        int m = words1.size(), n = words2.size();
        if (m != n) return false;
        unordered_map<string, string> parent;
        unordered_map<string, int> sizeOf;
        loadUnionSet(pairs, parent, sizeOf);
        for (int i = 0; i < m; ++i) {
            if (findRoot(parent, words1[i]) != findRoot(parent, words2[i])) return false;
        }
        return true;
    }
private:
    void loadUnionSet(vector<pair<string, string>>& pairs, unordered_map<string, string>& parent, unordered_map<string, int>& sizeOf) {
        for (auto& p : pairs) {
            bool firstHasParent = parent.find(p.first) != parent.end();
            bool secondHasParent = parent.find(p.second) != parent.end();
            if (firstHasParent && secondHasParent) {
                string root1 = findRoot(parent, p.first);
                string root2 = findRoot(parent, p.second);
                if (sizeOf[root1] > sizeOf[root2]) {
                    parent[root2] = root1;
                    sizeOf[root1] += sizeOf[root2];
                    if (root1 != root2) sizeOf.erase(root2);
                } else {
                    sizeOf[root2] += sizeOf[root1];
                    parent[root1] = root2;
                    if (root1 != root2) sizeOf.erase(root1);
                }
            } else if (firstHasParent) {
                string root = findRoot(parent, p.first);
                sizeOf[root]++;
                parent[p.second] = root;
            } else if (secondHasParent) {
                string root = findRoot(parent, p.second);
                sizeOf[root]++;
                parent[p.first] = root;
            } else {
                sizeOf[p.first] = 2;
                parent[p.first] = p.first;
                parent[p.second] = p.first;      
            }
        }
    }
    
    string findRoot(unordered_map<string, string>& parent, string word) {
        while (parent[word] != word) word = parent[word];
        return word;
    }
};