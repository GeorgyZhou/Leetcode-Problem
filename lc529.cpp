class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        if (board[click[0]][click[1]] == 'M') {
            board[click[0]][click[1]] = 'X';
            return board;
        }
        dfs(board, click[0], click[1], board.size(), board[0].size());
        return board;
    }
private:
    int dir[8][2] = {{1, 1}, {1, -1}, {1, 0}, {0, -1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}};
    
    void dfs(vector<vector<char>>& board, int r, int c, int m, int n) {
        int x, y, cnt = 0;
        for (int i = 0; i < 8; i++) {
            x = r + dir[i][0];
            y = c + dir[i][1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (board[x][y] == 'M') cnt++;
        }
        board[r][c] = cnt > 0 ? cnt + '0' : 'B';
        if (board[r][c] != 'B') return;
        for (int i = 0; i < 8; i++) {
            x = r + dir[i][0];
            y = c + dir[i][1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (board[x][y] == 'E') dfs(board, x, y, m, n);
        }
    }
};