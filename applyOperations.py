class Solution(object):
    def applyOperations(self, nums):
        length = len(nums)

        for i in range(length-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        result = []
        zeros = []
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zeros.append(num)

        return result+zeros
