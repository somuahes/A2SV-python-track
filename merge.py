class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=""
        length=min(len(word1),len(word2))
        for merge in range(length):
            merged+= word1[merge]+ word2[merge]

        merged+= word1[length:]+word2[length:]

        return merged