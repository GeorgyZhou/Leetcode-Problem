class Solution {
public:
    Solution(vector<int> nums) {
        this->shuffles = nums;
        this->original = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        shuffles = original;
        return shuffles;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        for (int i = 0; i < shuffles.size(); i++) {
            swap(shuffles[i], shuffles[i + rand() % (shuffles.size() - i)]);
        }
        return shuffles;
    }
private:
    vector<int> original;
    vector<int> shuffles;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */