class Solution {
public:
    vector<string> ipToCIDR(string ip, int range) {
        long cur = ipToLong(ip);
        cout << longToIp(cur) << endl;
        vector<string> res;
        while (range > 0) {
            int mask = 33 - min(lowestOneBit(cur), bitLength(range));
            res.emplace_back(longToIp(cur) + "/" + to_string(mask));
            cur += (1 << (32 - mask));
            range -= (1 << (32 - mask));
        }
        return res;
    }
    
    int bitLength(int num) {
        int count = 0;
        while (num > 0) {
            ++count;
            num >>= 1;
        }
        return count;
    }
    
    int lowestOneBit(long num) {
        if (num == 0) return 1;
        long ret = num & -num;
        int count = 0;
        while (ret > 0) {
            ++count;
            ret >>= 1;
        }
        return count;
    }
    
    string longToIp(long num) {
        stringstream ss;
        int count = 4;
        vector<string> ip;
        while (count--) {
            ip.emplace_back(to_string(num % 256));
            num /= 256;
        }
        for (int i = 3; i >= 0; --i) {
            ss << ip[i];
            if (i != 0) ss << ".";
        }
        return ss.str();
    }
    
    long ipToLong(string& ip) {
        int n = ip.size();
        long ans = 0L;
        int cur = 0;
        for (int i = 0; i < n; ++i) {
            if (ip[i] == '.') {
                ans = (ans << 8) + cur;
                cur = 0;
            } else {
                cur = cur * 10 + (ip[i] - '0');
            }
        }
        ans = (ans << 8) + cur;
        return ans;
    }
};