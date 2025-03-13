
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        seta=set(a)
        setb=set(b)
        uni=seta.union(setb)
        return len(uni)