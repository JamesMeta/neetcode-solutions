from typing import List


class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        prev_diff = {}
        
        for i, num in enumerate(numbers):
            
            if num in prev_diff:
                return [prev_diff[num], i + 1]
            
            diff = target - num
            
            prev_diff[diff] = i + 1
        
        return []
            
sol = Solution()

print(sol.twoSum([1,2,3,4], 3))