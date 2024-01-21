# select the min element and swap as we loop throug the array
from typing import List
class Solution:
    def selectionSort(self, nums:List[int] ) -> List[int]:
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1,len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
            # swap element
            nums[i],nums[min_index] = nums[min_index],nums[i]
        
        return nums
    
s = Solution()
nums = [1,4,8,6,6]
print(s.selectionSort(nums))
        
            
        