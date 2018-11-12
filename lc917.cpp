class Solution {
public:
  string reverseOnlyLetters(string S) {
    int i = 0, j = S.size();
    UpdateIndexes(i, j, S);
    while (i < j) {
      char temp;
      temp = S[i];
      S[i] = S[j];
      S[j] = temp;
      ++i;
      --j;
      this->UpdateIndexes(i, j, S); 
    }
    return S;
  }
private:
  void UpdateIndexes(int &i, int &j, const std::string &S) {
    while (i < S.size() && (S[i] < 'a' || S[i] > 'z') && (S[i] < 'A' || S[i] > 'Z')) {
      ++i;
    }
    while (j >= 0 && (S[j] < 'a' || S[j] > 'z') && (S[j] < 'A' || S[j] > 'Z')) {
      --j;
    }
  }
};
