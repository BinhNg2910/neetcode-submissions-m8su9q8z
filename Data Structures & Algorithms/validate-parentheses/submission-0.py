class Solution:
    def isValid(self, s: str) -> bool:
        """
        create stack to store the open brackets, each time meet a closed bracket, check with stack if it matched or not
        TC: O(n)
        SC: O(n)
        """
        brackets = list()
        for b in s:
            if b in ["(", "{", "["]:
                brackets.append(b)
            elif b == ")" and brackets and brackets[-1] == "(":
                brackets.pop()
            elif b == "}" and brackets and brackets[-1] == "{":
                brackets.pop()
            elif b == "]" and brackets and brackets[-1] == "[":
                brackets.pop()
            else:
                return False
        if brackets:
            return False
        return True
