class Solution {
public:
    int countPrimeSetBits(int L, int R) {
        int32_t res = 0;
        for (int32_t i = L; i <= R; ++i) {
            auto bits_count = get_bits(i);
            if (bits_count == 2 || bits_count == 3 || bits_count == 5 || bits_count == 7 || bits_count == 11 || bits_count == 13 || bits_count == 17 || bits_count == 19 || bits_count == 23 || bits_count == 29 || bits_count == 31) {
                ++res;
            }
        }
        return res;
    }
    
    int32_t get_bits(int32_t num) {
        int32_t res = 0;
        while (num) {
            num = num & (num - 1);
            ++res;
        }
        return res;
    }
};