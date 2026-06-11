class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        z = 1
        while l < r:
            if s[l] != s[r]:
                z -= 1
                if z < 0:
                    return False 
            l += 1
            r -= 1
        return True