from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0 

        maximum = max(nums)
        minimum = min(nums)

        counting_pos = [0] * (maximum + 1)
        counting_neg = [0] * (abs(minimum))

        for num in nums:

            if num == 0:
                counting_pos[0] = 1

            if num > 0:
                counting_pos[num] = 1
            
            if num < 0:
                counting_neg[num] = 1

        counting_neg.extend(counting_pos)
        counting = counting_neg.copy()       

        longest_sequence = 0
        current_sequence = 0

        for num in counting:
            
            if num == 1:
                current_sequence += 1
            else:              
                current_sequence = 0
            

            if current_sequence > longest_sequence:
                    longest_sequence = current_sequence
        
        return longest_sequence

        