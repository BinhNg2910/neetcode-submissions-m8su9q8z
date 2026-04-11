class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. BF - TC: O(n^2) - SC: O(1)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] + nums[i] == target:
                    return [i, j]
        return [-1, -1]
                    