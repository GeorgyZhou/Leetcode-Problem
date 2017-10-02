class Solution {
public:
    int maximumSwap(int num) {
        int last[10] = {-1};
        string charNum = to_string(num);
        for (int i = 0; i < charNum.size(); i++) {
            last[charNum[i] - '0'] = i;
        }
        for (int i = 0; i < charNum.size(); i++) {
            int value = (int)(charNum[i] - '0');
            for (int j = 9; j > value; j--) {
                if (last[j] <= i) continue;
                swap(charNum[i], charNum[last[j]]);
                return stoi(charNum);
            }
        }
        return num;
    }
};