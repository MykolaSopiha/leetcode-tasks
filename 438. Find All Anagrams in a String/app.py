from typing import Counter, DefaultDict, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = Counter(p)
        p_lenght = len(p)
        results = []
        window = DefaultDict(int)
        start = 0
        
        for end in range(len(s)):
            letter = s[end]
            window[letter] += 1
            
            if end - start + 1 == p_lenght:
                if pattern == window:
                    results.append(start)
                
                window[s[start]] -= 1
                if window[s[start]] == 0:
                    del window[s[start]]
                
                start += 1
        
        return results