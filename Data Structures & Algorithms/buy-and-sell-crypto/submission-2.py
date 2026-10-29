class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Idea 1: bf to 2 loop to find out
        TC: O(n^2)
        SC: O(1)
        """
        # n = len(prices)
        # maxProfit = 0
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         maxProfit = max(prices[j] - prices[i], maxProfit)
        # return maxProfit

        """
        Idea 2: use a left pointer to point to the smallest prices on left side (always keep updating to smaller price), the right pointer keep moving to find the profit can make with smallest price at left pointer
        TC: O(n)
        SC: O(1)
        """
        maxProfit = 0
        smallestPriceIdx = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[smallestPriceIdx]:
                smallestPriceIdx = i
                # print(f'Update {i} - {smallestPriceIdx}')
            maxProfit = max(maxProfit, prices[i] - prices[smallestPriceIdx])
        return maxProfit