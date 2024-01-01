# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        L,R,ans = [0]*n,[0]*n,[0]*n
        L[0], R[n-1] =1,1
        for i in range(1,n,1):
            L[i]=L[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            R[i] = R[i+1]*nums[i+1]
        for i in range(n):
            ans[i] = L[i]*R[i]
        return ans
