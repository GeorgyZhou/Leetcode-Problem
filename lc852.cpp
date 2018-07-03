class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int32_t peak = 1;
        for (int32_t i = 1; i < A.size() - 1; ++i) {
            if (A[i] < A[peak]) {
                 break;
            }
            peak = i;
        }
        return peak;
    }
};
