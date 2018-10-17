class Solution {
public:
  int smallestRangeI(vector<int>& A, int K) {
    int min_num = INT_MAX, max_num = INT_MIN, res;
    for (const auto &num : A) {
      min_num = std::min(min_num, num);
      max_num = std::max(max_num, num);
    }
    res = max_num - min_num;
    return std::max(res - 2 * K, 0);
  }
};
