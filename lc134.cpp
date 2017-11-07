class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        int min = gas[0] - cost[0];
        int sum = min;
        int index = 0;
        for (int i = 1; i < n; i++) {
            sum += gas[i] - cost[i];
            if (sum < min) {
                min = sum;
                index = i;
            }
        }
        return sum >= 0 ? (index + 1) % n : -1;
    }
};