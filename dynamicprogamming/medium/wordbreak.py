class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp= [False]*(len(s)+1)
        words = set(wordDict)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break;

        return dp[len(s)]
    # Method 2
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     memo = [None] *(len(s)+1)
    #     words = set(wordDict)
    #     def helper(s,words,start,memo):
    #         if start == len(s):
    #             return True
    #         if  memo[start] != None:
    #             return memo[start]
    #         for end in range(start+1,len(s)+1):
    #             if s[start:end] in words and helper(s,words,end,memo):
    #                 memo[start] = True
    #                 return True
    #         memo[start] = False
    #         return False
    #     return helper(s,words,0,memo)

    # Method1    
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     words = set(wordDict)
    #     queue = deque([0])
    #     seen  = set()
    #     while queue:
    #         print(seen)
    #         start = queue.popleft()
    #         if start == len(s):
    #             return True
            
    #         for end in range(start+1,len(s)+1):
    #             if end in seen:
    #                 continue
                
    #             if s[start:end] in words:
    #                 queue.append(end)
    #                 seen.add(end)
    #     return False

