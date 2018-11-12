class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string S) {
        int32_t occupied = 0;
        int32_t line = 0;
        for (auto& chr: S) {
            if (line == 0) {
                line = 1;
            }
            if (occupied + widths[chr - 'a'] > 100) {
                occupied = 0;
                ++line;
            }
            occupied += widths[chr - 'a'];
        }
        return {line, occupied};
    }
};
