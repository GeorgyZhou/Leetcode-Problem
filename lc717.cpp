class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        bool res = false;
        for (int i = 0; i < bits.size(); ) {
            if (bits[i] == 1) {
                res = false;
                i += 2;
            } else {
                res = true;
                ++i;
            }
        }
        return res;
    }
};