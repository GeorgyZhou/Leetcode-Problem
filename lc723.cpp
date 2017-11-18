class Solution {
public:
    vector<vector<int>> candyCrush(vector<vector<int>>& board) {
        bool changed = true;
        while(changed) solve(board, changed);
        return board;
    }
private:
    void solve(vector<vector<int>>& board, bool& changed) {
        changed = false;
        int m = board.size(), n = board[0].size();
        vector<pair<int, int>> marked;
        for (int i = 0, j; i < m; i++) {
            for (j = 0; j < n; j++) {
                if (board[i][j]) {
                    int i1 = i, i0 = i, j1 = j, j0 = j;
                    while (i0 > max(-1, i - 3) && board[i0][j] == board[i][j]) --i0;
                    while (i1 < min(i + 3, m) && board[i1][j] == board[i][j]) ++i1;
                    while (j0 > max(-1, j - 3) && board[i][j0] == board[i][j]) --j0;
                    while (j1 < min(j + 3, n) && board[i][j1] == board[i][j]) ++j1;
                    if (j1 - j0 > 3 || i1 - i0 > 3) marked.push_back({i, j});
                }
            }
        }
        if (marked.empty()) return;
        changed = true;
        for (auto& p : marked) board[p.first][p.second] = 0;
        for (int j = 0; j < n; ++j) {
            int t = m-1;
            for (int i = m-1; i >= 0; --i) if (board[i][j]) swap(board[i][j], board[t--][j]);
            for (int i = t; i >= 0; --i) board[i][j] = 0;
        }
        return;
    }
};