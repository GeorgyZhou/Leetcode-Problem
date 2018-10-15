class Solution {
public:
  vector<int> sortArrayByParityII(vector<int>& A) {
    int i = 0, j = 1;
    std::vector<int> res(A.size());
    for (const auto num : A) {
      if (num % 2) {
        res[j] = num;
        j += 2;
      } else {
        res[i] = num;
        i += 2;
      }
    }
    return res;
  }
};
