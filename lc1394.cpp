class Solution {
public:
    int findLucky(vector<int>& arr) {
        std::unordered_map<int, int> freq_map;
        for (auto const& value : arr) {
            if (freq_map.find(value) == freq_map.end()) {
                freq_map[value] = 0;
            }
            freq_map[value] += 1;
        }
        int val = -1;
        for (auto it = freq_map.begin(); it != freq_map.end(); ++it) {
            if (it->first == it->second) {
                val = std::max(val, it->first);
            }
        }
        return val;
    }
};
