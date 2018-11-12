class Solution {
public:
  int smallestRangeII(vector<int>& A, int K) {
    std::sort(A.begin(), A.end());
    int max_num = INT_MIN, min_num = INT_MAX, res;
    for (int i = 0; i < A.size(); ++i) {
      max_num = std::max(max_num, A[i]);
      min_num = std::min(min_num, A[i]);
    }
    res = max_num - min_num;
    for (int i = 0; i < A.size() - 1; ++i) {
      res = std::min(res, std::max(max_num - K, A[i] + K) - std::min(min_num + K, A[i+1] - K));
    }
    return res;
  }
};
