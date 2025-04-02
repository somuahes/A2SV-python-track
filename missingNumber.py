class Solution(object):
    def missingNumber(self, nums):
        setNums = set(nums)
        length = len(nums)
        rangeNumbers = set(range(length+1))

        return (rangeNumbers-setNums).pop(
