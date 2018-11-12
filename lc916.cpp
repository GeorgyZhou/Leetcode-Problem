class Solution {
public:
  std::vector<std::string> wordSubsets(vector<string>& A, vector<string>& B) {
    std::vector<std::string> res;
    std::vector<std::vector<int>> cand_counts(A.size(), std::vector<int>(26, 0));
    std::vector<int> op_counts(26, 0);
    std::vector<int> char_counts(26, 0);
    for (int i = 0; i < A.size(); ++i) {
      for (const auto &ch : A[i]) {
        ++cand_counts[i][ch - 'a'];
      }
    }
    for (int i = 0; i < B.size(); ++i) {
      for (const auto &ch : B[i]) {
        ++op_counts[ch - 'a'];
      }
      for (int j = 0; j < 26; ++j) {
        char_counts[j] = std::max(char_counts[j], op_counts[j]);
        op_counts[j] = 0;
      }
    }
    for (int i = 0, j; i < A.size(); ++i) {
      for (j = 0; j < 26; ++j) {
        if (cand_counts[i][j] < char_counts[j]) {
          break;
        }
      }
      if (j == 26) {
        res.emplace_back(A[i]);
      }
    }

    return res;
  }
};
