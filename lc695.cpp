class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int area = 0;
        unordered_set<int> visited; 
        for (int i = 0, j; i < grid.size(); i++) {
            for (j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 0 || visited.find(i * grid[0].size() + j) != visited.end()) continue;
                area = max(area, dfs(grid, visited, i, j));
            }
        }
        return area;
    }
private:
    int dr[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}}; 
    int dfs(vector<vector<int>>& grid, unordered_set<int>& visited, int i, int j) {
        int x, y;
        int cnt = 1;
        visited.insert(i * grid[0].size() + j);
        for (int k = 0; k < 4; k++) {
            x = i + dr[k][0];
            y = j + dr[k][1];
            if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size()) continue;
            if (grid[x][y] == 0 || visited.find(x * grid[0].size() + y) != visited.end()) continue;
            cnt += dfs(grid, visited, x, y);
        }
        return cnt;
    } 
};