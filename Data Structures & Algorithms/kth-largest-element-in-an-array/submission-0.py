class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Idea 1: sort then return the kth largest element
        """
        nums.sort(reverse=True)
        return nums[k-1]