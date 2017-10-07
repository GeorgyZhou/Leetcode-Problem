class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> dic;
        int m = list1.size(), n = list2.size(), smallest = INT_MAX;
        int index, i;
        vector<string> ret;
        for (i = 0; i < m; i++)
            dic[list1[i]] = i;
        for (i = 0; i < n; i++) {
            if (dic.find(list2[i]) == dic.end()) continue;
            index = dic[list2[i]];
            if (index + i < smallest) { 
                smallest = index + i;
                ret.clear();
            }
            if (index + i <= smallest) ret.push_back(list2[i]);
        }
        return ret;
    }       
};