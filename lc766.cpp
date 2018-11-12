class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int32_t m = static_cast<int32_t>(matrix.size()), n = static_cast<int32_t>(matrix[0].size());
        for (int32_t j = 0; j < n; ++j) {
             int32_t next_j = j;
             int32_t next_i = 0;
             int32_t value{0};
             bool is_null_value = true;
             while (next_j < n && next_i < m) {
                 if (is_null_value) {
                     value = matrix[next_i][next_j];
                     is_null_value = false;
                 }
                 if (matrix[next_i][next_j] != value) {
                     return false;
                 }
                 ++next_j;
                 ++next_i;
             }
        }
        for (int32_t i = 0; i < m; ++i) {
            int32_t next_i{i};
            int32_t next_j{0};
            bool is_null_value = true;
            int32_t value{0};
            while(next_i < m && next_j < n) {
                if (is_null_value) {
                    value = matrix[next_i][next_j];
                    is_null_value = false;
                }
                if (matrix[next_i][next_j] != value) {
                    return false;
                }
                ++next_j;
                ++next_i;
            }
        }
        return true;
    }
};
