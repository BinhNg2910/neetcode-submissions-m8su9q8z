class MinStack:
    """
    Idea: create a list to store the element as a stack, using a global min variable to store the min and at each node in stack has a min variable so can get the min whenever it want
    - TC: O(1)
    - SC: O(n)
    1 3 0 2
    stack: (1, 1) (3, 1) (0, 0), (2, 0)
    """

    def __init__(self):
        self.minStack = list()
        self.globalMinVal = float('inf')
    def push(self, val: int) -> None:
        self.globalMinVal = min(self.globalMinVal, val)
        self.minStack.append((val, self.globalMinVal))

    def pop(self) -> None:
        self.minStack.pop()
        self.globalMinVal = self.minStack[-1][1] if self.minStack else float('inf')

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]
        
