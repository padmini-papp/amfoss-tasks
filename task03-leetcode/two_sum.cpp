// Two Sum - Easy
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};

// Approach: used a hash map to store each number and its index as I go. For each
// number, check if its complement (target minus number) already exists in the map.
// If it does, found the answer immediately, in one pass. Time complexity O(n).
