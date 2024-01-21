from typing import List
class Solution:
    def selectionSort(self,nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            minIndex = i
            for j in range(i+1,len(nums)):
               if nums[j] < nums[minIndex]:
                   minIndex = j
            #swap element
            nums[minIndex],nums[i] = nums[i],nums[minIndex]
        return nums
    
    def insertionSort(self,nums:List[int]) -> List[int]:
        for i in range(1,len(nums)):
            key = nums[i]
            j=i-1
            while j>=0 and nums[j] > key:
                nums[j+1]= nums[j]
                j -= 1
            nums[j+1] = key
        return nums
    
s = Solution()
print(s.insertionSort([6,7,1,2,35,44]))