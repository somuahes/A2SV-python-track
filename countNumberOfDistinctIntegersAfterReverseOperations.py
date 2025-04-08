class Solution(object):
    def countDistinctIntegers(self, nums):
        output = []
        for num in nums:
            output.append(num)
            reversedNum = int(str(num)[::-1])
            output.append(reversedNum)

        return len(set(output))
