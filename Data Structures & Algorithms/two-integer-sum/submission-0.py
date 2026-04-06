class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = {}
        for i , n in enumerate(nums):
            remain = target - n
            if remain in t:
                return [ t[remain],i]
            else:
                t[n] = i
        