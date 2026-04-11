class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Idea: using 2 hashtable to count freq of each word and compare with each other
        TC:
        SC:
        """
        return collections.Counter(s) == collections.Counter(t)