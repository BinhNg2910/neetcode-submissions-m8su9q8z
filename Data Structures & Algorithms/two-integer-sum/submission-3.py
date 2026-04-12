class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. BF - TC: O(n^2) - SC: O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[j] + nums[i] == target:
        #             return [i, j]
        # return [-1, -1]
                    
        # 2. Sort then using 2 pointers
        # TC: O(nlogn + n) - SC: O(n)
        # n = len(nums)
        # pairs = [(num, idx) for (idx, num) in enumerate(nums)]
        # pairs.sort(key = lambda x: x[0])
        # left, right = 0, n-1
        # while left < right:
        #     curr = pairs[left][0] + pairs[right][0]
        #     if curr == target:
        #         return [pairs[left][1], pairs[right][1]] if pairs[left][1] < pairs[right][1] else [pairs[right][1], pairs[left][1]]
        #     elif curr < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return [-1, -1]

        # 3. using hashtable for complement
        # TC: O(n) - SC: O(n)
        complement = dict()
        for i, num in enumerate(nums):
            if target - num in complement:
                return [complement[target-num], i]
            else:
                complement[num] = i
        return [-1, -1]
            