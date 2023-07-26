class Solution(object):
    def lengthOfLastWord(s):
       words = s.split()
       print(words)
       return len(words[-1])
    
print(Solution.lengthOfLastWord("sdsfs 12345 1"))