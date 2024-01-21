
# To swap element in the corect order one by one
from typing import List
class Solution:
    def insertionSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        for i in range(1,len(nums)):
            key = nums[i]
            j=i-1
            while j>=0 and key < nums[j]:
                nums[j+1] = nums[j]
                j = j-1
            nums[j+1] = key
        
        return nums

c= Solution()
nums = [1,3,8,5,4]
print(c.insertionSort(nums))
