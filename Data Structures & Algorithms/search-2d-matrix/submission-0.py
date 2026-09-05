class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Idea: using BS to find the correct row which this target belong to, then use BS again to find the correct index on that row
        TC: O(logn + logm) with n and m is number of row and number of column
        SC: O(1)
        """
        row, col = len(matrix), len(matrix[0])
        # find the correct row that contains the target
        r1, r2 = 0, row-1
        targetRow = 0
        while r1 <= r2:
            midRow = r1 + (r2 - r1) // 2
            if matrix[midRow][0] <= target:
                targetRow = midRow
                r1 = midRow + 1
            else: # the first element on this row greater than target -> this row does not contain the target I want
                r2 = midRow - 1
        
        print(f"Target row: {targetRow}")
        c1, c2 = 0, col-1
        while c1 <= c2:
            midCol = c1 + (c2-c1) // 2
            if matrix[targetRow][midCol] == target:
                return True
            elif matrix[targetRow][midCol] > target:
                c2 = midCol - 1
            else:
                c1 = midCol + 1
        return False

