from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_maps = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            key_maps[key].append(word)
        return list(key_maps.values())
        