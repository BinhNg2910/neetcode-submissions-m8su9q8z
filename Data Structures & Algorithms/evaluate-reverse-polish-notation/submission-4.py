class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = list()
        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                b, a = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                else:
                    if a/b < 0:
                        stack.append(math.ceil(a / b))
                    else:
                        stack.append(math.floor(a / b))
        return stack[0]
                    
