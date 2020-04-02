class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        std::vector<int> new_index;
        new_index.push_back(index[0]);
        for (int i = 1; i < index.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (index[i] <= new_index[j]) {
                    ++new_index[j];
                }
            }
            new_index.push_back(index[i]);
        }
        std::vector<int> results(index.size());
        for (int i = 0; i < index.size(); ++i) {
            results[new_index[i]] = nums[i];
        }
        return results;
    }
};
