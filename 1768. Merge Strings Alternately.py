class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        answer = ''
        for _ in range(min(len(word1), len(word2))):
            answer += word1[0] + word2[0]

            word1 = word1.replace(word1[0], '', 1)
            word2 = word2.replace(word2[0], '', 1)

        return answer + word1 + word2