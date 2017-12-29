class Solution {
public:
    string crackSafe(int n, int k) {
        if (n == 1 && k == 1) return "0";
        unordered_set<string> visited;
        stringstream ans;
        string node = "";
        for (int i = 0; i < n - 1; ++i) {
            node += "0";
        }
        dfs(visited, ans, node, k);
        ans << node;
        return ans.str();
    }
    
    void dfs(unordered_set<string>& visited, stringstream& ans, string node, int k) {
        for (int i = 0; i < k; ++i) {
            string seq = node + to_string(i);
            if (visited.find(seq) != visited.end()) continue;
            visited.insert(seq);
            dfs(visited, ans, seq.substr(1, seq.size() - 1), k);
            ans << i;
        }
    }
};