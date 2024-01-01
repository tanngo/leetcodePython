# https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        max_streak =1
        for num in nums_set:
            #only run from local smallest element
            if num -1 not in nums_set:
                current_streak = 1
                currentElem = num
                while currentElem +1 in nums_set:
                    current_streak += 1
                    currentElem += 1
                max_streak = max(current_streak,max_streak)

        return max_streak


                
        