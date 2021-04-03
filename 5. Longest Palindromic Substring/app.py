class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        result = ''
        resultLen = 0

        for i in range(len(s)):

            # find odd palindrome
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen = r - l + 1

                if currLen > resultLen:
                    resultLen = currLen
                    result = s[l:r+1]

                l = l - 1
                r = r + 1
            
            # find even palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen = r - l + 1
                
                if currLen > resultLen:
                    resultLen = currLen
                    result = s[l:r+1]
                
                l = l - 1
                r = r + 1
        
        return result