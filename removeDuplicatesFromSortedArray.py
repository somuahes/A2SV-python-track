class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        position = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[position] = nums[i]

                position += 1

        return position
