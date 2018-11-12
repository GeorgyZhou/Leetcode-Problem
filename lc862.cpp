class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        vector<int> sums(A.size() + 1, 0);
        for (int32_t i = 0; i < A.size(); ++i) {
            sums[i+1] = A[i] + sums[i];
        }
        std::deque<int32_t> indexes;
        int res = A.size() + 1;
        for (int32_t i = 0; i < sums.size(); ++i) {
            while (!indexes.empty() && sums[i] <= sums[indexes.back()]) {
                indexes.pop_back();
            }
            while (!indexes.empty() && sums[i] >= sums[indexes.front()] + K) {
                res = std::min(res, i - indexes.front());
                indexes.pop_front();
            }
            indexes.push_back(i);
        }
        return res > A.size() ? -1 : res;
    }
};
