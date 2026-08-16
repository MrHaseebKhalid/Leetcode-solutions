from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == "" or magazine == "" or len(ransomNote) > len(magazine):
            return False
        
        for x in set(ransomNote):
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True

