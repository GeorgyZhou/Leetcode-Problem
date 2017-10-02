class Solution {
public:
    string nextClosestTime(string time) {
        int num[4];
        int smallest = 0xFFFFFFF;
        int next;
        string ret = "00:00";
        int cur = 60 * stoi(time.substr(0, 2)) + stoi(time.substr(3, 2));
        for (int i=0; i < 4; i++) {
            if (i > 1) {
                num[i] = time[i+1] - '0';
            }
            else {
                num[i] = time[i] - '0';
            }
        }
        bool flag = false;
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++){
                if (num[i]*10 + num[j] < 24) {
                    for (int k = 0; k < 4; k++) {
                        for (int l = 0; l < 4; l++) {
                            if (num[k] * 10 + num[l] < 60) {
                                next = num[i] * 600 + num[j] * 60 + num[k] * 10 + num[l];
                                if (next < cur) next += 24 * 60;
                                if (next == cur) continue;
                                if (((next - cur) % (24 * 60)) < smallest) {
                                    smallest = (next - cur) % (24 * 60);
                                    ret[0] = '0' + num[i];
                                    ret[1] = '0' + num[j];
                                    ret[3] = '0' + num[k];
                                    ret[4] = '0' + num[l];
                                    flag = true;
                                }
                            }
                        }
                    }
                }
            }
        }
        if (!flag) return time;
        return ret;
    }
};