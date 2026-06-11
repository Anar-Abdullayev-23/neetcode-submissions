class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = []
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            r.append(word1[i])
            r.append(word2[j])
            i += 1
            j += 1
        r.append(word1[i:])
        r.append(word2[j:])
        return ''.join(r)