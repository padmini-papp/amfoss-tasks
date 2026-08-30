// Container With Most Water - Medium
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxWater = 0;
        while (left < right) {
            int width = right - left;
            int h = min(height[left], height[right]);
            int water = width * h;
            maxWater = max(maxWater, water);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxWater;
    }
};

// Approach: used two pointers, one at each end. Water held is width times the
// shorter of the two heights. Moved whichever pointer had the smaller height
// inward, since that's the one limiting how much water can be held, and kept
// track of the best answer found. Time complexity O(n).
