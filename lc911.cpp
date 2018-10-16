class TopVotedCandidate {
public:
  TopVotedCandidate(vector<int> persons, vector<int> times_) : times(std::move(times_)){
    std::unordered_map<int, int> count;
    int max_vote = -1;
    for (int i = 0; i < persons.size(); ++i) {
      ++count[persons[i]];
      if (count[persons[i]] >= max_vote) {
        max_vote = count[persons[i]];
        res[times[i]] = persons[i];
      } else {
        res[times[i]] = res[times[i-1]];
      }
    }
  }

  int q(int t) {
    int l = 0, r = times.size(), mid;
    while (l < r - 1) {
      mid = (l + r) / 2;
      if (times[mid] > t) {
        r = mid;
      } else {
        l = mid;
      }
    }
    return res[times[l]];
  }
private:
  std::vector<int> times;
  std::unordered_map<int, int> res;
};

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */
