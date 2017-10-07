class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int cnt = 0;
        for (int i = 0; i < flowerbed.size(); i++) {
            if (flowerbed[i] == 1) continue;
            if ((i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.size() - 1 || flowerbed[i+1] == 0)) {
                cnt++;
                flowerbed[i] = 1;
            }
            if (cnt >= n) return true;
        }
        return cnt >= n;
    }
};