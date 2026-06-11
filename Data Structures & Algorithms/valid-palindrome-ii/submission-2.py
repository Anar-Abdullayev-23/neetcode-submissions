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
                return s[l+1 : r+1] == s[l+1 : r+1][::-1] or s[l : r] == s[l : r][::-1]
            l += 1
            r -= 1
        return True