class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = -1
        p2 = len(s)
        while p1 <= p2:
            p1 += 1
            p2 -= 1
            ch1, p1 = self.findAlnum(s, p1)
            ch2, p2 = self.findAlnum(s, p2, forward=False)
            print("{}:{} == {}:{}".format(p1, ch1.lower(), p2, ch2.lower()))
            if ch1.lower() != ch2.lower():
                print("{}:{} != {}:{}".format(p1, ch1.lower(), p2, ch2.lower()))
                return False
        return True

    def findAlnum(self, s, p, forward=True):
        while len(s) > p >= 0:
            if s[p].isalnum():
                return s[p], p
            p += (1 if forward else -1)
