class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Using hashset and check when meet nuw number
        """
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False