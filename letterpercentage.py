class Solution(object):
    def percentageLetter(self, s, letter):
       length=len(s)
       letters=s.count(letter)
       percentage=int((letters*100)/length)
       return percentage