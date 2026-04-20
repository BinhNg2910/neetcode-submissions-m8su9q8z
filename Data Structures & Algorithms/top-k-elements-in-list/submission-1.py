class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Idea: count the frequency then using heap to get the top freq
        TC: n + mlogm + klogk -> O(n)
        SC: O(n)
        """
        cnt = collections.Counter(nums)
        heapList = list()
        for num, freq in cnt.items():
            heapq.heappush(heapList, (-freq, num)) # make the maxheap (python just support minHeap)

        return [heapq.heappop(heapList)[1] for i in range(k)]