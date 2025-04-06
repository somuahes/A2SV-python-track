class Solution(object):
    def commonChars(self, words):
        compared_word = list(words[0])

        for word in words[1:]:
            common = []
            for char in compared_word:
                if char in word:
                    common.append(char)
                    word = word.replace(char, "", 1)
            compared_word = common
        return compared_word
