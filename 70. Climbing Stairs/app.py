class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        oneStepBefore = 2
        twoStepsBefore = 1
        sumSteps = 0
        for _ in range(3, n+1):
            sumSteps = oneStepBefore + twoStepsBefore
            twoStepsBefore = oneStepBefore
            oneStepBefore = sumSteps
        return sumSteps
