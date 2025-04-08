class Solution(object):
    def maxScoreIndices(self, nums):
        countOne = nums.count(1)
        countZero = 0
        sumList = []
        for i in range(len(nums)+1):
            totalSum = countOne+countZero
            sumList.append(totalSum)
            if i < len(nums):
                if nums[i] == 0:
                    countZero += 1
                else:
                    countOne -= 1
        maximum = max(sumList)
        return [i for i, value in enumerate(sumList)if value == maximum]
