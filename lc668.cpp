class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        int mid, lo = 1, hi = m * n;
        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            if (isEnough(mid, m, n, k)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
private:
    bool isEnough(int x, int m, int n, int k) {
        int count = 0;
        for (int i = 1; i <= m; ++i) {
            if (x < i) break;
            count += min(x / i, n);
        }
        return count >= k;
    }
};