class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        output = []
        for i in range(len(candies)):
            total = candies[i]+extraCandies
            if total >= maximum:
                output.append(True)
            else:
                output.append(False)
        return output
