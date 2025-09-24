from typing import List
import re




class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_match = "".join((re.findall(r"\d*\w*", s)))
        
        s_lower = s_match.lower()
        
        is_odd = len(s) % 2
        if is_odd:
            meeting_point = len(s) // 2
        else:
            meeting_point = (len(s) / 2) - 1
        
        
        for i in range(len(s_lower)):
            letter_front = s_lower[i]
            letter_back = s_lower[-1 * (i + 1)]
            
            if i == meeting_point and is_odd:
                return True
            
            elif i == meeting_point and not is_odd:
                if letter_front == letter_back:
                    return True
                else:
                    return False
            
            if letter_front != letter_back:
                return False

solution = Solution()

print(solution.isPalindrome("Was it a car or a cat I saw?"))