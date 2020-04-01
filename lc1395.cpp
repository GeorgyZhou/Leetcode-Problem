class Solution {
public:
    int numTeams(vector<int>& rating) {
        if (rating.size() < 3) {
            return 0;
        }
        std::vector<std::vector<int>> inc_dec(rating.size(), std::vector<int>(2, 0));
        for (int i = 1; i < rating.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (rating[i] > rating[j]) {
                    inc_dec[i][0] += 1;
                } else if (rating[i] < rating[j]) {
                    inc_dec[i][1] += 1;
                }
            }
        }
        int cnt = 0;
        for (int i = 1; i < inc_dec.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (rating[i] > rating[j]) {
                    cnt += inc_dec[j][0];
                } else if (rating[i] < rating[j]) {
                    cnt += inc_dec[j][1];
                }
            }
        }
        return cnt;
    }
};
