class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        output = []
        excess = []
        for i in arr2:
            if i in arr1:
                frequency = arr1.count(i)
            for j in range(frequency):
                output.append(i)
        for i in arr1:
            if i not in arr2:
                excess.append(i)
                excess.sort()

        return output + excess
