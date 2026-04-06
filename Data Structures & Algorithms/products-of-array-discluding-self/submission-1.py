class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            ans[i] = left
            left *=nums[i]
        left = 1
        for i in range(len(nums)-1 , -1 ,-1 ):
            ans[i] *= left
            left *= nums[i]
        return ans        