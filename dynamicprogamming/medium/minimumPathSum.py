# https://leetcode.com/problems/minimum-path-sum/submissions/1143424072/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        dp= [[0]*cols for _ in range(rows)]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if i != rows -1 and j== cols-1:
                    dp[i][j]= dp[i+1][j]+grid[i][j]
                elif j != cols -1 and i== rows-1:
                    dp[i][j]= dp[i][j+1]+grid[i][j]
                elif i!= rows-1 and j!=cols-1:
                    dp[i][j]= grid[i][j]+ min(dp[i][j+1],dp[i+1][j])
                else:
                    dp[i][j]= grid[i][j]
        return dp[0][0]

           

        