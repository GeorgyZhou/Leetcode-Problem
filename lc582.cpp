class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, int kill) {
        unordered_map<int, vector<int>> path;
        for (int i = 0; i < pid.size(); i++) {
            if (path.find(ppid[i]) == path.end()) path[ppid[i]] = {};
            path[ppid[i]].push_back(pid[i]);
        }
        vector<int> killIds;
        dfs(path, killIds, kill);
        return killIds;
    }
private:
    void dfs(unordered_map<int, vector<int>>& path, vector<int>& killIds, int id) {
        killIds.push_back(id);
        if (path.find(id) == path.end()) return;
        for (auto& cid : path[id]) dfs(path, killIds, cid);
    }
};