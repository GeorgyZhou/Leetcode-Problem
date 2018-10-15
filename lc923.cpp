// Given an integer array A, and an integer target, return the number of tuples
// i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
// As the answer can be very large, return it modulo 10^9 + 7

class Solution {
public:
  int threeSumMulti(vector<int>& A, int target) {
    int mod = 1000000000 - 7;
    for (int i = 0, j; i < size - 1; ++i) {
      std::unordered_map<int, int> occ;
      real_target = target - A[i];
      for (j = i + 1; j < size; ++j) {
        if (occ.find(real_target - A[j]) != occ.end()) {
          res += occ[real_target - A[j]];
          if (res > mod) {
            res %= mod;
          }
        }
        occ[j] += 1
      }
    }
    return res;
  }
};
