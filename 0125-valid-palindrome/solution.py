class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for y in s.lower():
            if y.isalnum():
                a += y
        return a == a[::-1]
                
