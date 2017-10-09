class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int, int> freq;
        int biggest = 0;
        for (int i = 0, j; i < wall.size(); i++) {
            for (j = 0; j < wall[i].size(); j++) {
                if (j != 0) wall[i][j] += wall[i][j-1];
                if (j == wall[i].size() - 1) continue;
                int key = wall[i][j];
                if (freq.find(key) == freq.end()) freq[key] = 0;
                freq[key]++;
                biggest = max(biggest, freq[key]);
            }
        }
        return wall.size() - biggest;
    }
};