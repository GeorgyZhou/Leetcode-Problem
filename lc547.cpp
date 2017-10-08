
class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        if (M.size() == 0) return 0;
        unordered_set<int> visited;
        int cnt = 0;
        for (int i = 0; i < M.size(); i++) {
            if (visited.find(i) != visited.end()) continue;
            cnt++;
            dfs(M, visited, i);
        }
        return cnt;
    }
private:
    void dfs(vector<vector<int>>& M, unordered_set<int>& visited, int j) {
        visited.insert(j);
        for (int i = 0; i < M.size(); i++) {
            if (M[i][j] == 1 && visited.find(i) == visited.end()) dfs(M, visited, i);
        }
    }
};