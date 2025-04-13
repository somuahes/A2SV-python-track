class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
            else:
                i += 1
        for j in range(count):
            nums.append(0)
