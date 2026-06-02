class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def binarySearch(nums, target, add_to_index):
            median = len(nums) //2

            if len(nums) == 1 and nums[median] != target:
                if (target > nums[0]):
                    return add_to_index + 1
                else:
                    return add_to_index

            if nums[median] == target:
                return median + add_to_index
            elif nums[median] > target:
                return binarySearch(nums[:median], target, add_to_index)
            else:
                return binarySearch(nums[median:], target, add_to_index + median)

        
        return binarySearch(nums, target, 0)

        