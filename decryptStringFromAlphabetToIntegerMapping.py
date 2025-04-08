class Solution(object):
    def freqAlphabets(self, s):
        i = 0
        output = []
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                num = int(s[i:i+2])
                letter = chr(96+num)
                output.append(letter)
                i += 3
            else:
                num = int(s[i])
                letter = chr(96+num)
                output.append(letter)
                i += 1
        return "".join(output)
