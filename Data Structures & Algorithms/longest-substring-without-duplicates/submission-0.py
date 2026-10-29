class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        unique = set()
        maxLen = 0
        while right < len(s):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            maxLen = max(maxLen, right-left+1)
            right += 1
        return maxLen