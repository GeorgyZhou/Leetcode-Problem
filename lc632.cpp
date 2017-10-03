class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        int size = nums.size();
        if (size == 0) return {};
        int minLength = INT_MAX;
        int maximum = INT_MIN, minimum = INT_MAX;
        vector<int> range = {minimum, maximum};
        auto cmp = [](tuple<int, int, int> t1, tuple<int, int, int> t2) { 
            return std::get<0>(t1) > std::get<0>(t2); 
        };
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype(cmp)> heap(cmp);
        for (int i = 0; i < size; i++) {
            heap.push(make_tuple(nums[i][0], i, 0));
            maximum = max(maximum, nums[i][0]);
        }
        while (!heap.empty()) {
            auto tuple = heap.top();
            heap.pop();
            // cout << std::get<0>(tuple) << std::get<1>(tuple) << std::get<2>(tuple) << endl;
            int curMin = std::get<0>(tuple), line = std::get<1>(tuple), index = std::get<2>(tuple);
            if (maximum - curMin < minLength) {
                minimum = curMin;
                minLength = maximum - curMin;
                range[0] = minimum;
                range[1] = maximum;
            }
            if (index >= nums[line].size() - 1) break;
            maximum = max(maximum, nums[line][index+1]);
            heap.push(make_tuple(nums[line][index+1], line, index + 1));
        }
        return range;
    }
};