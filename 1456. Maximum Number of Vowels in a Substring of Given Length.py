class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        actualWord = s[0:k]
        nVogals = 0

        for char in actualWord:
            if char in "aeiou":
                nVogals += 1

        maxVogals = nVogals

        for c in range(k, len(s)):

            if actualWord[0] in "aeiou":
                nVogals -= 1

            actualWord = actualWord[1:]

            if s[c] in "aeiou":
                nVogals += 1

            actualWord+= s[c]

            if nVogals > maxVogals:
                maxVogals = nVogals

            if nVogals == k:
                return k

            
        return maxVogals
