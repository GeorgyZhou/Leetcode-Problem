class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        if (image.size() == 0 || image[0].size() == 0) return {{}};
        int color = image[sr][sc];
        unordered_set<int> visited;
        dfs(image, visited, sr, sc, color, newColor);
        return image;
    }
    
private:
    vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    void dfs(vector<vector<int>>& image, unordered_set<int> visited, int x, int y, int oriColor, int newColor) {
        image[x][y] = newColor;
        visited.insert(x * image[0].size() + y);
        for (auto& dir : dirs) {
            int nx = x + dir[0], ny = y + dir[1];
            if (visited.find(nx * image[0].size() + ny) != visited.end()) continue;
            if (nx >= 0 && nx < image.size() && ny >= 0 && ny < image[0].size() && image[nx][ny] == oriColor) {
                dfs(image, visited, nx, ny, oriColor, newColor);
            }
        }
    }
};