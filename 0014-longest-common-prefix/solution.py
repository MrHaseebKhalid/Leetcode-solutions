class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        n = len(strs)
        lc_prefix = ""

        if n != 0:
            for c1,c2 in zip(strs[0],strs[n-1]):
                if c1 != c2:
                    break
                lc_prefix += c1
        return lc_prefix

