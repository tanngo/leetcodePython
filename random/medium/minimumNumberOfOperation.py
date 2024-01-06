class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        dp =[-1]*10001
        def helper(x,y:int):
            if x <= y: 
                return y-x
            if dp[x] != -1:
                return dp[x]
            res = abs(x-y)
            res = min(res,1+x % 5 + helper(x//5,y))
            res = min(res,1+(5-x%5)+ helper(x//5+1,y))
            res = min(res,1+x % 11+helper(x//11,y))
            res = min(res, 1+ (11-x%11)+ helper(x//11+1,y))
            dp[x]=res
            return dp[x]
        
        return helper(x,y)


        
    
        
            
        