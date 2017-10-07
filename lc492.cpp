class Solution {
public:
    vector<int> constructRectangle(int area) {
        if (area == 0) return {};
        for (int a = sqrt(area); a > 0; a--) 
            if (!(area % a)) return {area/a, a};
        return {};
    }
};