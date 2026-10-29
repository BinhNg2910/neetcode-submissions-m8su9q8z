class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Idea: using a hashtable to count the number of each character, get the character has the most number in hashtable at each time then suppose to turn all rest character into the most amount character
        - there a left pointer to move when the hashtable length over the allowed amount k (which used to turn other character into thne most amount character)
        TC: O(n * 26)
        SC: O(1)
        """
        left, right = 0, 0
        cnt = collections.defaultdict(int)
        largestAmt = 0
        maxLen = 0
        while right < len(s):
            cnt[s[right]] += 1
            largestAmt = max(largestAmt, cnt[s[right]])
            while left < right and right - left + 1 - largestAmt > k:
                cnt[s[left]] -= 1
                largestAmt = max(cnt.values()) # reset the largest amt in dict
                left += 1
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen

