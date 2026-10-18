class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Idea: using monostack to find the first height that smaller than the current height on left side and right side
        """
        n = len(heights)
        leftMin = [-1] * n
        rightMin = [n] * n
        
        stack = list()

        # track for the left side
        stack.append(0)
        for i in range(1, n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMin[i] = stack[-1]
            stack.append(i)
        
        # track for right side
        stack.clear()
        stack.append(n-1)
        for i in range(n-2, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMin[i] = stack[-1]
            stack.append(i)
        # print(leftMin, rightMin)
        maxRec = 0
        for i in range(n):
            maxRec = max(maxRec, heights[i] * (rightMin[i] - leftMin[i] - 1))
            
        return maxRec