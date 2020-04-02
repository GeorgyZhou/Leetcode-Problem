class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        size_t m = grid.size();
        size_t n = grid[0].size();
        if (m == 1 && n == 1) {
            return true;
        }
        if (grid[0][0] == 5) {
            return false;
        }
        if (grid[0][0] == 4) {
            return dfs(grid, 1, 0, m, n, 1)  || dfs(grid, 0, 1, m, n, 4);
        }
        int from = grid[0][0] == 1 || grid[0][0] == 6 ? 4 : 1;

        return dfs(grid, grid[0][0] == 1 || grid[0][0] == 6 ? 0 : 1, grid[0][0] == 1 || grid[0][0] == 6 ? 1 : 0, m, n, from);
    }

    bool dfs(vector<vector<int>>& grid, int x, int y, int m, int n, int from) {
        if (x < 0 || x >= m || y < 0 || y >= n) {
            return false;
        }
        switch (grid[x][y]) {
            case 1:
                if (from != 2 && from != 4) {
                    return false;
                }
                if (x == m - 1 && y == n - 1) {
                    return true;
                } 
                return from == 2 ? dfs(grid, x, y - 1, m, n, 2) : dfs(grid, x, y + 1, m, n, 4);
                break;
            case 2:
                if (from != 1 && from != 3) {
                    return false;
                }
                if (x == m - 1 && y == n - 1) {
                    return true;
                } 
                return from == 1 ? dfs(grid, x + 1, y, m, n, 1) : dfs(grid, x - 1, y, m, n, 3);
                break;
            case 3:
                if (from != 3 && from != 4) {
                    return false;
                }
                if (x == m - 1 && y == n - 1) {
                    return true;
                } 
                return from == 4 ? dfs(grid, x + 1, y, m, n, 1) : dfs(grid, x, y - 1, m, n, 2);
                break;
            case 4:
                if (from != 2 && from != 3) {
                    return false;
                }
                if (x == m - 1 && y == n - 1) {
                    return true;
                } 
                return from == 2 ? dfs(grid, x + 1, y, m, n, 1) : dfs(grid, x, y + 1, m, n, 4);
                break;
            case 5:
                if (from != 1 && from != 4) {
                    return false;
                }
                if (x == m - 1 && y == n - 1) {
                    return true;
                } 
                return from == 1 ? dfs(grid, x, y - 1, m, n, 2) : dfs(grid, x - 1, y, m, n, 3);
                break;
            case 6:
                if (from != 1 && from != 2) {
                    return false;
                }
                if (x == m - 1 && y == n - 1) {
                    return true;
                } 
                return from == 1 ? dfs(grid, x, y + 1, m, n, 4) : dfs(grid, x - 1, y, m, n, 3);
                break;
        }
        return false;
    }
};
