class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        c = 1
        while c < len(s):
            res += abs(ord(s[c]) - ord(s[c - 1]))
            c += 1
        return res
