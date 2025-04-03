class Solution(object):
    def thirdMax(self, nums):
        if len(nums) >= 3:
            nums.sort()
            distinct = set(nums)
            distinctList = list(distinct)
            return distinctList[-3]
        else:
            return max(nums)
