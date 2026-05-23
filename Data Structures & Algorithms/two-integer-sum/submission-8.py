class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = {}
        for i , j in enumerate(nums):
            r = target - j
            if r in t:
                return[t[r],i]
            else:
                t[j] = i
        