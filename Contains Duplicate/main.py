from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique_values = {}

        for num in nums:
            if num in unique_values:
                return True
            else:
                unique_values[num] = num
            
        return False
         