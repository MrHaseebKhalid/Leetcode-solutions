class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {"I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        x = 0
        for i,a in enumerate(s[:n-1]):
            if roman_num[a] >= roman_num[s[i+1]]:
                x += roman_num[a]
            else:
                x -= roman_num[a]

        x += roman_num[s[n-1]]
        return x

