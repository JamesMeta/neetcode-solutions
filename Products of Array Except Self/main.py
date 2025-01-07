from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_counter = 0
        zero_index = 0

        for i, num in enumerate(nums):

            if num != 0:
                product *= num

            if num == 0:
                zero_counter += 1
                zero_index = i
        
        if zero_counter > 1:
            return [0] * len(nums)
        
        elif zero_counter == 1:
            product_list = [0] * len(nums)
            product_list[zero_index] = int(product)
            return product_list
        
        else:
            return [product//num for num in nums]
        
            


    
        