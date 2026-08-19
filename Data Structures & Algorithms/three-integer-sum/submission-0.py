class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Idea 1: using brute force - TC: O(n^3)
        Idea 2: using 2 pointers with 1 loop to fix the first number, than 2 pointers to find for the rest subarray
        TC: O(n^2 + nlogn) = O(n^2)
        SC: O(1)
        """
        nums.sort()
        result = list()
        print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                if currSum == 0:
                    # print(f'Get indexes {i} - {left} - {right}')
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
        return result