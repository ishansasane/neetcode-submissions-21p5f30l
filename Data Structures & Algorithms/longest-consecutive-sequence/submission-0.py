class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in s:
                nn = n + 1
                length = 1
                while nn in s:
                    length += 1
                    nn +=1
                res = max(res , length)
        return res


        