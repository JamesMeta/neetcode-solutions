from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {"+", "-", "*", "/"}

        stack = []
        answer = 0
        for token in tokens:

            if token in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(str(int(eval(num2 + token + num1))))
            
            else:
                stack.append(token)
    
        answer = int(stack[0])
        return answer
            
        