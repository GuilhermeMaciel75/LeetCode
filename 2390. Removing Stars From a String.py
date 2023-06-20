class Solution:
    def removeStars(self, s: str) -> str:
        finalword = ''
        for char in s:
            if char == '*':
                finalword = finalword[:-1]
            else:
                finalword += char

        return finalword
