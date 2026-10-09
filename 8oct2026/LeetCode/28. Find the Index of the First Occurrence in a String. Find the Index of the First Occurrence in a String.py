##Leetcode Submission link :
##https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/2166031178

class Solution(object):
    def strStr(self, haystack, needle):
   
         if  needle in haystack :
            return haystack.find(needle)
         else :
            return -1
        
