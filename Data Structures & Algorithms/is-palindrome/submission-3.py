class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Idea: using 2 pointers to check from left to right and right to left
        """
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and right > left:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
