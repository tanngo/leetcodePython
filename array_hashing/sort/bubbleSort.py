#swap element as we iterate between the array\
from typing import List
class Solution:
    def bubbleSort(self, nums: List[int]) -> List[int]:
        swapped = False # if not swap then meaning the array is sorted 
        for i in range(len(nums)-1):
            for j in range(0,len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    swapped = True
                    nums[j+1],nums[j] = nums[j],nums[j+1]
            
            if not swapped:
                return nums
        return nums
    
s = Solution()
print(s.bubbleSort([1,5,3,9,2,5]))
                