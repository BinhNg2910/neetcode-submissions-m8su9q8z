class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. using a list with 26 element to store frequency of each char 
        and use a key in hashtable
        TC: O(n*k)
        SC: O(n*k)
        with n is number of string, k is max length of word in strs
        """
        # def convertToKey(s: string) -> tuple:
        #     key = [0] * 26
        #     for c in s:
        #         key[ord(c) - ord("a")] += 1
        #     return tuple(key)

        # anaGr = defaultdict(list)
        # for s in strs:
        #     anaGr[convertToKey(s)].append(s)
        # return list(anaGr.values())
        
        """
        2. sort all characters with alphabet order then string as key
        TC: O(n * klogk)
        SC: O(n * k)
        """
        def generateKey(s: str) -> str:
            key = sorted(s)
            # print(s, key)
            return "".join(key)

        anaGr = defaultdict(list)
        for s in strs:
            anaGr[generateKey(s)].append(s)
        return list(anaGr.values())

