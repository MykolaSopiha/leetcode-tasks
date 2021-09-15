class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        result = ''
        a = list(a)
        b = list(b)
        while carry or a or b:
            _sum = int(carry)
            if a: _sum += int(a.pop())
            if b: _sum += int(b.pop()) 
            carry = _sum >= 2
            _sum %= 2
            result = str(_sum) + result
        return result