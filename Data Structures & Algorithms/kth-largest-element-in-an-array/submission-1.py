class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Idea 2: using heap to keep tracking top k largest element, but using min heap to return the first element after iterate all num
        TC: nlogn
        SC: 1
        """
        heapList = list()
        for num in nums:
            heapq.heappush(heapList, num)
            if len(heapList) > k:
                heapq.heappop(heapList)
        return heapList[0]
        """
        Idea 1: sort then return the kth largest element
        """
        # nums.sort(reverse=True)
        # return nums[k-1]