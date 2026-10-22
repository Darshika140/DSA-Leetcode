
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int size = nums.size();
        int zero = 0;

        // Find the position of 0
        for (int i = 0; i < size; i++) {
            if (nums[i] == 0) {
                zero = i;
                break;
            }
        }

        // Check circular order in either direction
        bool left = true, right = true;

        for (int i = 1; i < size; i++) {
            int prev = (zero + i - 1) % size;
            int curr = (zero + i) % size;

            if (nums[curr] != nums[prev] + 1)
                left = false;

            prev = (zero - i + size) % size;
            curr = (zero - i + 1 + size) % size;

            if (nums[prev] != nums[curr] + 1)
                right = false;
        }

        int ans = INT_MAX;

        if (left) {
            ans = min(ans, zero);
            ans = min(ans, size - zero + 2);
        }

        if (right) {
            ans = min(ans, zero + 2);
            ans = min(ans, size - zero);
        }

        return ans == INT_MAX ? -1 : ans;
    }
};
