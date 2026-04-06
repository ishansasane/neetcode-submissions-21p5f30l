class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i , j in enumerate(nums):
            remain = target - j
            if remain in mapper:
                return [ mapper[remain] , i ]
            else:
                mapper[j] = i
            
        