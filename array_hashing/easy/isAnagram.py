# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        if (len(s)!= len(t)):
            return False
        counter = [0]*26
        for i in s:
            counter[ord(i)-ord('a')] +=1
        for i in t:
            counter[ord(i)-ord('a')] -=1
            if(counter[ord(i)-ord('a')]<0):
                return False
        return True
    #Solution 1
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     for i in s:
    #         if i in t:
    #             t= t.replace(i,'',1)
    #         else:
    #             return False
    #     return True
    #method1    
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     sorted_t = sorted(t)
    #     sorted_s = sorted(s)
    #     print(sorted_s)
    #     return sorted_s == sorted_t

    #method2
    # def isAnagram(self,s: str,t: str)-> bool:
    #     if len(s) != len(t):
    #         return False
    #     counter = [0]*26
    #     for char_s, char_t in zip(s,t):
    #         counter[ord(char_s)-ord('a')] += 1
    #         counter[ord(char_t)-ord('a')] -= 1
    #     for i in range(len(counter)):
    #         if counter[i]!=0:
    #             return False
    #     return True



        