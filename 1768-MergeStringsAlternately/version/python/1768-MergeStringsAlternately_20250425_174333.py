# Last updated: 4/25/2025, 5:43:33 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged = ""
        word1, word2 = list(word1), list(word2)
        for i in range(min(len(word1),len(word2))):
            merged += word1.pop(0) + word2.pop(0)
        return(merged + "".join(word1 + word2))