class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen = {}
        words = s.split(" ")

        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False

        for index,item in enumerate(pattern):

            if item not in seen:
                seen[item] = words[index]
            
            elif seen[item] != words[index]:
                return False

        return True

