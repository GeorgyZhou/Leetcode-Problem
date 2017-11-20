class Solution {
public:
    int findRotateSteps(string ring, string key) {
        int m = ring.size(), n = key.size();
        cache.resize(m, vector<int>(n, 0));
        for (int i = 0; i < ring.size(); ++i) {
            maps[ring[i]].emplace_back(i); 
        }
        return dfs(ring, key, 0, 0);
    }
private:
    vector<vector<int>> cache;
    unordered_map<char, vector<int>> maps;
    
    void printVec(vector<vector<int>>& vec) {
        for (int i = 0; i < vec.size(); ++i) {
            for (int j = 0; j < vec[i].size(); ++j) {
                cout << vec[i][j] << " ";
            }
            cout << endl;
        }
    }
    
    int dfs(string& ring, string& key, int ri, int ki) {
        int n = ring.size();
        if (ki == key.size()) return 0;
        if (cache[ri][ki] != 0) return cache[ri][ki];
        int step = INT_MAX, curStep;
        for (int& i : maps[key[ki]]) {
            curStep = min(abs(ri - i), n - abs(i - ri));
            step = min(step, curStep + dfs(ring, key, i, ki + 1));
        }
        if (step != INT_MAX) ++step;
        //cout << ri << " " << ki << " " << step << endl;
        cache[ri][ki] = step;
        return step;
    }
};