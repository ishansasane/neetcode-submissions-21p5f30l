
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = {}
        for i in nums:
            if i in t:
                t[i] += 1
            else:
                t[i] = 1
        
        # Sort the items by frequency (value) in descending order
        sorted_items = sorted(t.items(), key=lambda x: x[1], reverse=True)
        
        # Take the top k keys (frequent elements)
        return [item[0] for item in sorted_items[:k]]
