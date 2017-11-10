class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        if (n == 0) return 0;
        int index = 1, count = 1;
        char currentChar = chars[0];
        for (int i = 1; i < n; ++i) {
            if (currentChar == chars[i]) {
                ++count;
                int cur_size = 0, last_size = 0, tmp = count;
                while (tmp != 0) {
                    tmp /= 10;
                    ++cur_size;
                }
                tmp = count - 1;
                while (tmp != 0) {
                    tmp /= 10;
                    ++last_size;
                }
                tmp = count;
                index += (cur_size - last_size);
                for(int j = 0; j < cur_size; j++) {
                    chars[index - j] = tmp % 10 + '0';
                    tmp /= 10;
                }
            } else {
                if (count > 1) ++index;
                count = 1;
                chars[index++] = chars[i];
                currentChar = chars[i];
            }
        }
        return count > 1 ? index + 1 : index;
    }
};