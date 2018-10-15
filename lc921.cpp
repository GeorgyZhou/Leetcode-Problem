class Solution {
public:
  int minAddToMakeValid(string S) {
    int s1 = 0, s2 = 0;
    for (const auto &c : S) {
      if (c == '(') {
        s1 += 1;
      } else {
        if (s1 == 0) {
          s2 += 1;
        } else {
          --s1;
        }
      }
    }
    return s1 + s2;
  }
};
