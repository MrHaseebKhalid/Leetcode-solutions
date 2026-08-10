class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0 ):
            rev_number = 0
            y = x
            while y > 0:
                a = y % 10
                rev_number = (rev_number * 10) + a
                y = y // 10
            
            return x == rev_number
        else: return False
