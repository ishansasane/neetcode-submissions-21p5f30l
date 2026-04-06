from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Length of the next string
            j += 1  # Move past '#'
            res.append(s[j:j+length])
            i = j + length  # Move to the next encoded string
        return res
