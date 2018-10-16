class Solution {
public:
  int partitionDisjoint(vector<int>& A) {
    int res = A.size(), left_max = -1;
    std::vector<int> right_min(A.size(), 1000001);
    right_min[A.size() - 1] = A.back();
    for (int i = A.size() - 2; i >= 0; --i) {
      right_min[i] = std::min(A[i], right_min[i+1]);
    }
    for (int i = 0; i < A.size(); ++i) {
      if (left_max != -1 && left_max <= right_min[i]) {
        return i;
      }
      if (A[i] > left_max) {
        left_max = A[i];
      }
    }
    return 0;
  }
}
