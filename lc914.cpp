class Solution {
public:
  bool hasGroupsSizeX(vector<int>& deck) {
    std::unordered_map<int, int> count;
    for (const auto &num : deck) {
      ++count[num];
    }
    for (int i = 2, j; i <= deck.size(); ++i) {
      if (deck.size() % i == 0) {
        for (j = 0; j < deck.size(); ++j) {
          if (count[deck[j]] % i != 0) {
            break;
          }
        }
        if (j == deck.size()) {
            return true;
        }
      }
    }
    return false;
  }
};
