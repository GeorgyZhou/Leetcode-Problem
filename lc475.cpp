class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        if (heaters.size() == 0) return 0;
        sort(houses.begin(), houses.end(), less<int>());
        sort(heaters.begin(), heaters.end(), less<int>());
        int index = 0, radius = 0;
        for (int i = 0; i < houses.size(); i++) {
            while (index + 1 < heaters.size() && abs(heaters[index] - houses[i]) >= abs(heaters[index + 1] - houses[i]))
                index++;
            radius = max(radius, abs(heaters[index] - houses[i]));
        }
        return radius;
    }
};