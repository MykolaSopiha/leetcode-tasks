class Solution:
    def mySqrt(self, x: int) -> int:
        return self.binaryFindSqrt(x, 0, x)
    
    def binaryFindSqrt(self, num: int, start: int, end: int):
        half           = int((end - start)/2)
        halfSquare     = half * half
        halfSquarePlus = (half + 1) * (half + 1)

        if halfSquare <= num and num < halfSquarePlus:
            return half
        elif halfSquare > num:
            return self.binaryFindSqrt(num, 0, half)
        else:
            return self.binaryFindSqrt(num, half, end)
