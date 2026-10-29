class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Idea 1: bf to 2 loop to find out
        """
        n = len(prices)
        maxProfit = 0
        for i in range(n-1):
            for j in range(i+1, n):
                maxProfit = max(prices[j] - prices[i], maxProfit)
        return maxProfit

        """
        Idea 2L
        """