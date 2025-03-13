class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        sorted_a=sorted(a)
        sorted_b=sorted(b)
        length=len(sorted_a)
        for i in range (length):
            if sorted_a[i]!=sorted_b[i]:
                return False
            
        return True