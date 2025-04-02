class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}
        for bracket in s:
            if bracket in brackets:
                top = stack.pop() if stack else "#"
                if brackets[bracket] != top:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0
