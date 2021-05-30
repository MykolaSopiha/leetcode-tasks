class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        hasWord = False
        
        for i in range(len(s)):
            if s[len(s) - i - 1] == " ":
                if hasWord: break
            else:
                result = result + 1
                hasWord = True
        
        return result
