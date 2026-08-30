// Maximum Subarray - Medium
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            currentSum = max(nums[i], currentSum + nums[i]);
            maxSum = max(maxSum, currentSum);
        }
        return maxSum;
    }
};

// Approach: known as Kadane's algorithm. Walked through the array once keeping a
// running sum. At each number, decided whether to keep extending the current
// subarray or start fresh from that number alone, whichever gives a bigger sum.
// Kept track of the best sum seen at any point. Time complexity O(n).
