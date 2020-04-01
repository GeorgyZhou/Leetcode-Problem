class UndergroundSystem {
public:
    UndergroundSystem() {

    }

    void checkIn(int id, string stationName, int t) {
        in_times[id] = std::make_pair(stationName, t);
    }

    void checkOut(int id, string stationName, int t) {
        std::pair<string, int> check_in = in_times[id];
        in_times.erase(id);
        string key = check_in.first + "_" + stationName;
        if (trip_durations.find(key) == trip_durations.end()) {
            trip_durations[key] = std::make_pair(0, 0);
        }
        trip_durations[key] = std::make_pair(trip_durations[key].first + (t - check_in.second), trip_durations[key].second + 1);
    }

    double getAverageTime(string startStation, string endStation) {
        string key = startStation + "_" + endStation;
        return trip_durations[key].first / trip_durations[key].second;
    }

private:
    std::unordered_map<string, std::pair<int, double>> trip_durations;
    std::unordered_map<int, std::pair<string, int>> in_times;
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */
