class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex < 0) return {};
        vector<int> row = {1};
        for (int i = 1, j; i <= rowIndex; i++) {
            int last = 0;
            for (j = 0; j < i; j++) {
                last = row[j] ^ last;
                row[j] = last ^ row[j];
                last = last ^ row[j];
                row[j] += last;
            }
            row.push_back(last);
        }
        return row;
    }
};