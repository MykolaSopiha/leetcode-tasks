class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x <= 3: return 1
        return self.binaryFindSqrt(x, 1, x)
    
    def binaryFindSqrt(self, num: int, start: int, end: int):
        half           = start + int((end - start)/2)
        halfSquare     = half * half
        halfSquarePlus = (half + 1) * (half + 1)

        if halfSquare <= num and num < halfSquarePlus:
            return half
        elif halfSquare > num:
            return self.binaryFindSqrt(num, 1, half)
        else:
            return self.binaryFindSqrt(num, half, end)
