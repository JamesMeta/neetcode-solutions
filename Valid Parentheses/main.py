class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for para in s:

            if para in parentheses:
                stack.append(para)
            
            else:

                if stack:

                    para_popped = stack.pop()
                    closing_required = parentheses[para_popped]

                    if para == closing_required:
                        pass
                    else:
                        return False
                
                else:
                    
                    return False
        
        return not stack



