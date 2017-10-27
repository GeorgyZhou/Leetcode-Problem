class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        if (n == 0 || citations[n-1] == 0) return 0;
        int mid, left = 0, right = n-1;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (citations[mid] >= n - mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return n - right;
    }
};