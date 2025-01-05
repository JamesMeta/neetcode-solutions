from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        def quick_sort(arr):
            if len(arr) <= 1:
                return arr 
            pivot = arr[0]  
            left = [x for x in arr[1:] if x[1] < pivot[1]]  
            right = [x for x in arr[1:] if x[1] >= pivot[1]] 

            return quick_sort(left) + [pivot] + quick_sort(right)  
                


        int_freq = {}
        
        for num in nums:
            int_freq[num] = int_freq.get(num, 0) + 1
        
        sorted_freq = quick_sort(list(int_freq.items()))

        top_k_frequent_elements = []

        break_point = len(sorted_freq) - k

        for key, item in sorted_freq[break_point:]:
            top_k_frequent_elements.append(key)
        
        return top_k_frequent_elements


        

            


        

