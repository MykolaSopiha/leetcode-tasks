from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lettersMaps = []
        
        for word in words:
            wordLetterMap = dict()
            for letter in word:
                if letter in wordLetterMap:
                    wordLetterMap[letter] += 1
                else:
                    wordLetterMap[letter] = 1
            lettersMaps.append(wordLetterMap)
        
        result = []
        
        
        return result

solution = Solution()
solution.commonChars(["bella","label","roller"])