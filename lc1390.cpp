class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        std::unordered_map<int, std::unordered_set<int>> divisors;
        for (int j = 0; j < nums.size(); ++j) {
            int num = nums[j];
            int i = 1;
            while (i * i <= num) {
                if (num % i == 0) {
                    divisors[j].insert(i);
                    divisors[j].insert(num / i);
                    if(divisors[j].size() > 4) {
                        divisors.erase(j);
                        break;
                    }
                }
                ++i;
            }
        }
        int sum = 0;
        for (std::pair<int, std::unordered_set<int>> p : divisors) {
            if (p.second.size() == 4) {
                for (auto const& div : p.second) {
                    sum += div;
                }
            }
        }
        return sum;
    }
};
