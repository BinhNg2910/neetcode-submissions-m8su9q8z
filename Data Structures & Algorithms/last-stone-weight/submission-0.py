class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        TC: O(n)
        SC: O(n)
        n is number of stone
        """

        # implement max heap for stone's weight
        maxHeap = list()
        for w in stones:
            heapq.heappush(maxHeap, -w)
        
        while len(maxHeap) > 1:
            w1, w2 = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if w1 == w2:
                continue
            else:
                heapq.heappush(maxHeap, -abs(w1-w2))
        
        return 0 if len(maxHeap) == 0 else -maxHeap[0]

        