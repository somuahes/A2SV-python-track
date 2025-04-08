class Solution(object):
    def findTheWinner(self, n, k):
        friendList = list(range(1, n+1))
        index = 0
        while len(friendList) > 1:
            index = (index+k-1) % len(friendList)
            friendList.pop(index)
        return friendList[0]
