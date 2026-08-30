class KthLargest:
    """
    Idea: using min heap to store k largest element, popout and add new element when new value is larger than the first value in mean heap, then return the first element in min heap after adding
    TC: O(n*logk) - O(logk)
    SC: O(k)
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = list()
        for num in nums:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)
        print(self.minHeap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

    # def __init__(self, k: int, nums: List[int]):
    #     self.stream = nums[:]
    #     self.k = k

    # def add(self, val: int) -> int:
    #     self.stream.append(val)
    #     self.stream.sort(reverse = True)
    #     return self.stream[self.k - 1]