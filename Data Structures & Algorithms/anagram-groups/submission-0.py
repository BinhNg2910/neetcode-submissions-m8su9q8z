class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. using a list with 26 element to store frequency of each char 
        and use a key in hashtable
        TC:
        SC:
        """
        def convertToKey(s: string) -> tuple:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord("a")] += 1
            return tuple(key)

        anaGr = defaultdict(list)
        for s in strs:
            anaGr[convertToKey(s)].append(s)
        return list(anaGr.values())
        
