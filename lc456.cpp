class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int> st;
        int n = nums.size();
        if (n < 3) return false;
        int mins[n];
        mins[0] = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            mins[i] = min(nums[i], mins[i-1]);
        }
        st.push(nums[n-1]);
        for (int i = n-2; i >= 0; i--) {
            if (nums[i] > mins[i]) {
                while(st.size() > 0 && mins[i] >= st.top()) st.pop();
                if (st.size() > 0 && st.top() < nums[i]) return true;
            }
            st.push(nums[i]);
        }
        return false;
    }
};