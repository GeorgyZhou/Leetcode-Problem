class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        unordered_set<int> visited;
        unordered_set<string> shape;
        int key = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                key =  i * grid[0].size() + j;
                if (grid[i][j] == 1 && visited.find(key) == visited.end())
                    shape.insert(dfs(grid, visited, i, j));
            }
        }
        return shape.size();
    }
private:
    int dr[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    string dfs(vector<vector<int>>& grid, unordered_set<int>& visited, int r, int c) {
        int x, y;
        stringstream ss;
        visited.insert(r * grid[0].size() + c);
        for (int i = 0; i < 4; i++) {
            x = r + dr[i][0];
            y = c + dr[i][1];
            if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size()) continue;
            if (grid[x][y] == 0 || visited.find(x * grid[0].size() + y) != visited.end()) continue;
            ss << i + '0';
            ss << dfs(grid, visited, x, y);
            ss << ';';
        }
        return ss.str();
    }
};