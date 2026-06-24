class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numeric_stack = []
        for c in tokens:
            if c.isdigit() or (c.startswith('-') and len(c) > 1):
                numeric_stack.append(int(c))
            else:
                num2 = numeric_stack.pop()
                num1 = numeric_stack.pop()

                if c == '+':
                    numeric_stack.append(num1+num2)
                elif c == '-':
                    numeric_stack.append(num1-num2)
                elif c == '*':
                    numeric_stack.append(num1*num2)
                else:
                    numeric_stack.append(int(num1/num2))
                
        return numeric_stack.pop()