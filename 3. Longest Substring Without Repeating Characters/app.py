class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLength = 0

        for end in range(len(s)):
            if s[end] in s[start:end]:
                while s[end] in s[start:end]:
                    start += 1
            else:
                maxLength = max(maxLength, end - start + 1)

        return maxLength