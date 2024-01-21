# https://leetcode.com/problems/longest-increasing-subsequence/description/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub=[nums[0]]
        for num in nums:
            if num > sub[-1]:
                sub.append(num)
            else:
                i=0
                while num > sub[i]:
                    i+=1
                sub[i]=num
        return len(sub)



    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp =[1]*(len(nums))
    #     for i in range(1,len(nums)):
    #         for j in range(i):
    #             if nums[i]> nums[j]:
    #                 dp[i]= max(dp[i],dp[j]+1)
    #     return max(dp)


        