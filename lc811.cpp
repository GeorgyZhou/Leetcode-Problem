class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        std::unordered_map<std::string, int32_t> domain_count;
        for (auto& s: cpdomains) {
            int32_t delimiter_index = s.find(' ');
            int32_t count = std::stoi(s.substr(0, delimiter_index));
            std::string domain{s.substr(delimiter_index + 1)};
            std::string subdomain{""};
            size_t pos = s.size();
            size_t last_pos = s.size();
            domain_count[domain] += count;
            while ((pos = domain.rfind(".", last_pos - 1)) != std::string::npos) {
                subdomain = domain.substr(pos + 1);
                domain_count[subdomain] += count;
                last_pos = pos;
            }
        }
        std::vector<std::string> res;
        for (auto& kv : domain_count) {
            res.emplace_back(std::to_string(kv.second) + " " + kv.first);
        }
        return res;
    }
};
