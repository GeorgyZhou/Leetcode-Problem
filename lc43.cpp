class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";
        int l1 = num1.size(), l2 = num2.size();
        int p1 = l1 - 1, p2;
        int carry = 0, maxlen = 0;
        vector<string> toBeAdded;
        while (p1 >= 0) {
            stringstream ss("");
            p2 = l2 - 1;
            for (int i = p1; i < l1 - 1; ++i) ss << '0';
            carry = 0;
            while (p2 >= 0) {
                int tmp = (num1[p1] - '0') * (num2[p2] - '0') + carry;
                ss << (tmp % 10);
                carry = tmp / 10;
                --p2;
            }
            if (carry > 0) ss << to_string(carry);
            string midProd(ss.str());
            reverse(midProd.begin(), midProd.end());
            toBeAdded.emplace_back(midProd);
            --p1;
        }
        map_add(toBeAdded);
        return toBeAdded[0];
    }
private:
    void map_add(vector<string>& nums) {
        while (nums.size() >= 2) {
            string num1 = nums.back();
            nums.pop_back();
            string num2 = nums.back();
            nums.pop_back();
            nums.emplace_back(string_add(num1, num2));
        }
    }
    
    string string_add(string num1, string num2) {
        stringstream ss("");
        int p1 = num1.size() - 1, p2 = num2.size() - 1, carry = 0;
        while (p1 >= 0 && p2 >= 0) {
            int sum = (num1[p1] - '0') + (num2[p2] - '0') + carry;
            ss << sum % 10;
            carry = sum / 10;
            --p1;
            --p2;
        }
        while (p1 >= 0) {
            int sum = num1[p1] - '0' + carry;
            ss << sum % 10;
            carry = sum / 10;
            --p1;
        }
        while (p2 >= 0) {
            int sum = num2[p2] - '0' + carry;
            ss << sum % 10;
            carry = sum / 10;
            --p2;
        }
        if (carry > 0) ss << to_string(carry);
        string res(ss.str());
        reverse(res.begin(), res.end());
        return res;
    }
};