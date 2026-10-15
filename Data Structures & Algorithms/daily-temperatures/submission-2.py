class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Idea: using bf to find from current index to the end of the list
        TC: O(n^2)
        SC: O(n)
        """
        # n = len(temperatures)
        # result = [0] * n
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break
        # return result

        """
        Idea: set the temperature to put in a stack when, pop it out when meet a higher temperature because it cannot meet the next one anymore
        TC: O(2n) = O(n)
        SC: O(n)
        """
        n = len(temperatures)
        result = [0] * n
        stack = list()
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
