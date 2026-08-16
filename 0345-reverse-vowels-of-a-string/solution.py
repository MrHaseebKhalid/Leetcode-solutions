class Solution:
    def reverseVowels(self, s: str) -> str:
        size = len(s)
        if size < 2: return s
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        s = list(s)
        x = 0
        y = size - 1
        while x < y:
            while s[x] not in vowels and x < y:
                x += 1
            while s[y] not in vowels and x < y:
                y -= 1
            s[x], s[y] = s[y] , s[x]
            x += 1
            y -= 1
        return "".join(s)
