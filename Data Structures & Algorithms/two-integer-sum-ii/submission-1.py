class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Idea 1: just bruteforce - TC: O(n^2) - O(1)
        Idea 2: 2 pointers from left and right, move left when sum smaller and move right and sum larger
        TC: O(n) - SC: O(1)
        Idea 3: hashmap to get the complement value
        TC: O(n) - SC: O(n)
        """
        # Idea 2
        # left, right = 0, len(numbers) - 1
        # while left < right:
        #     currSum = numbers[left] + numbers[right]
        #     if currSum == target:
        #         return [left+1, right+1]
        #     elif currSum < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return [-1, -1]

        # Idea 3:
        complementary = dict()
        for i in range(len(numbers)):
            if target - numbers[i] in complementary:
                return [complementary[target - numbers[i]] + 1, i + 1]
            else:
                complementary[numbers[i]] = i
        return [-1, -1]

        