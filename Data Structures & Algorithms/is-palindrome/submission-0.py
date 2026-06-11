class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        result = ''
        while l < r:
            for i in s:
                if i.isalnum():
                    result += i.lower()
            return result == result[::-1]
